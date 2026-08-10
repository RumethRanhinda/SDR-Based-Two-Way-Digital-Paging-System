"""
Embedded Python Block: Sender (Queue + Persistent Seq + Len Header)
"""
import numpy as np
from gnuradio import gr
import pmt
import threading
import time
import struct
import random

class blk(gr.basic_block):
    def __init__(self, max_payload_len=250, retry_limit=10, timeout_ms=300, base_backoff_ms=50):
        gr.basic_block.__init__(self, name='Reliable Sender (Queue)', in_sig=None, out_sig=None)

        self.max_payload_len = max_payload_len
        self.retry_limit = retry_limit
        self.timeout = timeout_ms / 1000.0
        self.base_backoff = base_backoff_ms / 1000.0

        # Current Transmission State
        self.dest_addr = 0x00
        self.src_addr = 0x00 
        self.global_seq = 0 
        
        self.msg_fragments = []
        self.fragment_index = 0
        self.retry_count = 0
        self.state = "IDLE"
        self.last_send_time = 0
        
        # === QUEUE SYSTEM ===
        # Stores tuples: {'dest': dest, 'src': src, 'data': payload_bytes}
        self.tx_queue = []
        
        self.lock = threading.Lock()
        self.stop_thread = False

        self.message_port_register_in(pmt.intern('msg_in'))
        self.message_port_register_in(pmt.intern('addr_in'))
        self.message_port_register_in(pmt.intern('ack_in'))
        self.message_port_register_out(pmt.intern('packet_out'))
        self.message_port_register_out(pmt.intern('feedback_out'))

        self.set_msg_handler(pmt.intern('msg_in'), self.handle_msg)
        self.set_msg_handler(pmt.intern('addr_in'), self.handle_addr)
        self.set_msg_handler(pmt.intern('ack_in'), self.handle_ack)

        self.arq_thread = threading.Thread(target=self.run_arq_loop)
        self.arq_thread.daemon = True
        self.arq_thread.start()

    def __del__(self):
        self.stop_thread = True
        if self.arq_thread.is_alive(): self.arq_thread.join()

    def handle_addr(self, msg):
        """ Update the 'current' address registers. Used when a new message arrives. """
        if not pmt.is_pair(msg): return
        data = pmt.u8vector_elements(pmt.cdr(msg))
        if len(data) >= 2:
            with self.lock:
                self.dest_addr = data[0]
                self.src_addr = data[1]

    def handle_msg(self, msg):
        """ 
        Handle new message input.
        If BUSY, add to Queue. If IDLE, start transmitting.
        """
        if not pmt.is_pair(msg): return
        payload_bytes = pmt.u8vector_elements(pmt.cdr(msg))
        if len(payload_bytes) == 0: return
        
        with self.lock:
            # Create a job packet with the CURRENT addresses and payload
            # We must capture addresses NOW because self.dest_addr might change later
            job = {
                'dest': self.dest_addr,
                'src': self.src_addr,
                'data': payload_bytes
            }

            if self.state == "IDLE":
                # Start immediately
                self.load_job(job)
            else:
                # Add to queue
                self.tx_queue.append(job)

    def load_job(self, job):
        """ Helper: Loads a job into the active transmission buffers """
        # Restore the addresses for this specific message
        self.dest_addr = job['dest']
        self.src_addr = job['src']
        payload = job['data']
        
        self.msg_fragments = []
        for i in range(0, len(payload), self.max_payload_len):
            self.msg_fragments.append(payload[i : i + self.max_payload_len])

        self.fragment_index = 0
        self.retry_count = 0
        self.state = "SENDING"
        self.last_send_time = 0

    def check_queue(self):
        """ Called after success/fail. Checks if more work exists. """
        if len(self.tx_queue) > 0:
            # Pop next message and start
            next_job = self.tx_queue.pop(0)
            self.load_job(next_job)
        else:
            self.state = "IDLE"

    def handle_ack(self, msg):
        if self.state == "IDLE": return
        if not pmt.is_pair(msg): return
        
        try:
            ack_data = pmt.u8vector_elements(pmt.cdr(msg))
            if len(ack_data) < 7: return 
            if ack_data[2] != 1: return 

            requested_seq = (ack_data[3] << 8) | ack_data[4]

            with self.lock:
                next_seq = (self.global_seq + 1) & 0xFFFF
                if requested_seq == next_seq:
                    self.global_seq = next_seq
                    self.fragment_index += 1
                    self.retry_count = 0
                    
                    if self.fragment_index >= len(self.msg_fragments):
                        # === MSG DONE: SUCCESS ===
                        self.send_feedback(True)
                        # Check if there are more messages waiting
                        self.check_queue()
                    else:
                        self.state = "SENDING"
                        self.last_send_time = 0 
        except Exception: pass

    def send_packet(self):
        if self.fragment_index >= len(self.msg_fragments): return
        fragment = self.msg_fragments[self.fragment_index]
        ack_flag = 0
        fin_flag = 1 if (self.fragment_index == len(self.msg_fragments) - 1) else 0
        payload_len = len(fragment)

        header = struct.pack('>BBBHBB', self.dest_addr, self.src_addr, ack_flag, self.global_seq, fin_flag, payload_len)
        full_packet = list(header) + list(fragment)
        
        out_pmt = pmt.cons(pmt.make_dict(), pmt.init_u8vector(len(full_packet), full_packet))
        self.message_port_pub(pmt.intern('packet_out'), out_pmt)
        self.last_send_time = time.time()

    def send_feedback(self, success):
        status = "ACK" if success else "FAIL"
        self.message_port_pub(pmt.intern('feedback_out'), pmt.cons(pmt.PMT_NIL, pmt.intern(status)))

    def run_arq_loop(self):
        while not self.stop_thread:
            time.sleep(0.01)
            with self.lock:
                if self.state == "SENDING" or self.state == "WAIT_ACK":
                    wait_threshold = self.timeout
                    if self.retry_count > 0:
                        exponent = min(self.retry_count, 4)
                        wait_threshold += random.uniform(0, self.base_backoff * (2 ** (exponent - 1)))

                    if self.last_send_time == 0 or (time.time() - self.last_send_time) > wait_threshold:
                        if self.retry_count < self.retry_limit:
                            self.send_packet()
                            self.state = "WAIT_ACK"
                            if self.last_send_time != 0: self.retry_count += 1
                        else:
                            # === MSG DONE: FAILED ===
                            self.send_feedback(False)
                            # Even if failed, check queue for next message
                            self.check_queue()
