"""
Embedded Python Block: Receiver (Reads Length)
"""
import numpy as np
from gnuradio import gr
import pmt
import struct

class blk(gr.basic_block):
    def __init__(self, my_addr_hex='A1'):
        gr.basic_block.__init__(self, name='Receiver / ACK Generator', in_sig=None, out_sig=None)
        
        try:
            self.my_addr = int(my_addr_hex, 16)
        except ValueError:
            self.my_addr = 0xA1
        
        self.reassembly_buffer = {}
        self.expected_seq = {} 

        self.message_port_register_in(pmt.intern('pdu_in'))
        self.message_port_register_out(pmt.intern('msg_out'))
        self.message_port_register_out(pmt.intern('ack_out'))
        self.message_port_register_out(pmt.intern('ack_reply_out'))
        self.set_msg_handler(pmt.intern('pdu_in'), self.handle_msg)

    def handle_msg(self, msg):
        if not pmt.is_pair(msg): return
        full_packet = list(pmt.u8vector_elements(pmt.cdr(msg)))
        
        # Header is now 7 bytes >BBBHBB
        if len(full_packet) < 7: return 

        try:
            # Unpack 7 bytes: Dest, Src, Flag, Seq, Fin, LEN
            dest, src, flag, seq, fin, data_len = struct.unpack('>BBBHBB', bytes(full_packet[:7]))
            
            # === CRITICAL FIX ===
            # Only read 'data_len' bytes. Ignore everything else.
            # If the buffer has 64 bytes but data_len is 5, we only take 5.
            end_idx = 7 + data_len
            if end_idx > len(full_packet): end_idx = len(full_packet)
            
            payload = full_packet[7 : end_idx]
        except:
            return 

        if dest != self.my_addr: return

        if flag == 1:
            self.message_port_pub(pmt.intern('ack_out'), msg)
            return

        if src not in self.expected_seq:
            self.expected_seq[src] = seq 
            self.reassembly_buffer[src] = []

        expected = self.expected_seq[src]

        if seq == expected:
            self.reassembly_buffer[src].append(bytes(payload))
            self.expected_seq[src] = (expected + 1) & 0xFFFF
            self.send_ack(src, self.expected_seq[src])
            
            if fin == 1:
                self.push_to_gui(src)
                
        elif seq < expected:
            self.send_ack(src, expected)

    def send_ack(self, target_node, next_required_seq):
        # Header: Dest, Src, Flag=1, Seq, FIN=0, Len=0
        header = struct.pack('>BBBHBB', target_node, self.my_addr, 1, next_required_seq, 0, 0)
        out_pmt = pmt.cons(pmt.make_dict(), pmt.init_u8vector(len(header), list(header)))
        self.message_port_pub(pmt.intern('ack_reply_out'), out_pmt)

    def push_to_gui(self, src):
        try:
            full_msg_bytes = b''.join(self.reassembly_buffer[src])
            
            # Now we don't need aggressive cleaning because we sliced the data perfectly.
            # But standard decode is still good practice.
            clean_bytes = list(full_msg_bytes)
            
            meta = pmt.make_dict()
            meta = pmt.dict_add(meta, pmt.intern("src_id"), pmt.from_long(src))
            
            out_pmt = pmt.cons(meta, pmt.init_u8vector(len(clean_bytes), clean_bytes))
            self.message_port_pub(pmt.intern('msg_out'), out_pmt)
            
            self.reassembly_buffer[src] = []
        except: pass
