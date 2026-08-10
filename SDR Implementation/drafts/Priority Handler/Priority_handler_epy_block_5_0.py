"""
Embedded Python Block: MAC Priority Arbiter (Timer-Based Aging)
"""
import numpy as np
from gnuradio import gr
import pmt
import threading
import time

class blk(gr.basic_block):
    def __init__(self, aging_interval_ms=200):
        """
        Args:
            aging_interval_ms: How often (in ms) to boost the priority of waiting packets.
                               Default 200ms means a packet drops from Priority 5 -> 4 after 0.2s.
        """
        gr.basic_block.__init__(self, name='MAC Arbiter (Timer Aging)', in_sig=None, out_sig=None)

        self.aging_interval = aging_interval_ms / 1000.0
        self.last_aging_time = time.time()

        # Unified Queue. Stores dictionaries: {'msg': pmt_msg, 'prio': int}
        self.tx_queue = []

        self.lock = threading.Lock()
        self.stop_thread = False

        self.message_port_register_in(pmt.intern('data_in'))
        self.message_port_register_in(pmt.intern('ack_in'))
        self.message_port_register_out(pmt.intern('pdu_out'))

        self.set_msg_handler(pmt.intern('data_in'), self.handle_data)
        self.set_msg_handler(pmt.intern('ack_in'), self.handle_ack)

        self.tx_thread = threading.Thread(target=self.run_tx_loop)
        self.tx_thread.daemon = True
        self.tx_thread.start()

    def __del__(self):
        self.stop_thread = True
        if self.tx_thread.is_alive(): self.tx_thread.join()

    def get_priority_from_msg(self, msg, default_val):
        """ Extract 'priority' field from PMT Metadata """
        try:
            meta = pmt.car(msg)
            if pmt.is_dict(meta):
                p_val = pmt.dict_ref(meta, pmt.intern("priority"), pmt.PMT_NIL)
                if not pmt.eq(p_val, pmt.PMT_NIL):
                    return pmt.to_long(p_val)
        except: pass
        return default_val

    def handle_data(self, msg):
        """ Data from Sender Block (User defined priority 0-10) """
        if not pmt.is_pair(msg): return
        prio = self.get_priority_from_msg(msg, 5) # Default to mid-priority if missing
        
        with self.lock:
            self.tx_queue.append({'msg': msg, 'prio': prio})

    def handle_ack(self, msg):
        """ ACKs from Receiver Block (Always Priority 0) """
        if not pmt.is_pair(msg): return
        # ACKs are critical, always 0
        with self.lock:
            self.tx_queue.append({'msg': msg, 'prio': 0})

    def run_tx_loop(self):
        while not self.stop_thread:
            current_time = time.time()
            msg_to_send = None
            
            # === 1. AGING LOGIC (Timer Based) ===
            if (current_time - self.last_aging_time) > self.aging_interval:
                with self.lock:
                    if len(self.tx_queue) > 0:
                        # Decrement priority of EVERY packet currently waiting
                        # (Lower number = Higher Priority)
                        for item in self.tx_queue:
                            # ACKs (Prio 0) stay at 0 or go negative, which is fine
                            item['prio'] -= 1
                
                self.last_aging_time = current_time

            # === 2. SENDING LOGIC ===
            with self.lock:
                if len(self.tx_queue) > 0:
                    # Sort: Ascending order (Lowest number = Highest Priority)
                    # Python's sort is stable (preserves FIFO for ties)
                    self.tx_queue.sort(key=lambda x: x['prio'])
                    
                    # Pop the most important message
                    item = self.tx_queue.pop(0)
                    msg_to_send = item['msg']
            
            # === 3. HARDWARE OUTPUT ===
            if msg_to_send:
                self.message_port_pub(pmt.intern('pdu_out'), msg_to_send)
                # Small gap to prevent hardware buffer overrun
                time.sleep(0.005) 
            else:
                # Sleep if idle to save CPU
                time.sleep(0.002)
