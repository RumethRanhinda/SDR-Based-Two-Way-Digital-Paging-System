"""
Embedded Python Block: PDU Scrambler / Descrambler (Additive)
"""

import numpy as np
from gnuradio import gr
import pmt

class blk(gr.basic_block):
    def __init__(self, seed=0xCAFE, max_len=4096):
        """
        Constructor.
        Args:
            seed: A fixed integer to seed the random number generator. 
                  MUST BE THE SAME on Tx and Rx.
            max_len: The maximum packet length we expect to scramble.
        """
        gr.basic_block.__init__(
            self,
            name='PDU Scrambler',
            in_sig=None,
            out_sig=None
        )
        self.seed = seed
        self.max_len = max_len
        
        # Pre-calculate the scrambling mask during initialization.
        # This ensures high performance during runtime.
        # We use a fixed seed so the sequence is always identical.
        rng = np.random.default_rng(self.seed)
        self.scramble_mask = rng.integers(0, 256, self.max_len, dtype=np.uint8)

        # Register message ports
        self.message_port_register_in(pmt.intern('pdu_in'))
        self.message_port_register_out(pmt.intern('pdu_out'))
        self.set_msg_handler(pmt.intern('pdu_in'), self.handle_msg)

    def handle_msg(self, msg):
        """
        XOR the input payload with the pre-generated mask.
        """
        if not pmt.is_pair(msg):
            return

        # 1. Extract Metadata and Data
        meta = pmt.car(msg)
        data_pmt = pmt.cdr(msg)
        
        try:
            input_data = np.array(pmt.u8vector_elements(data_pmt), dtype=np.uint8)
        except:
            return

        # 2. Safety Check on Length
        length = len(input_data)
        if length > self.max_len:
            # If packet is too big for our mask, resize mask (slow, but safe)
            # In a real deployed system, you might just drop it or expand the init max_len
            rng = np.random.default_rng(self.seed)
            self.scramble_mask = rng.integers(0, 256, length, dtype=np.uint8)
            self.max_len = length

        # 3. Perform XOR Scrambling (Whitening)
        # We take the first 'length' bytes of our pre-calculated mask
        scrambled_data = np.bitwise_xor(input_data, self.scramble_mask[:length])

        # 4. Output
        out_vector = pmt.init_u8vector(length, scrambled_data)
        self.message_port_pub(pmt.intern('pdu_out'), pmt.cons(meta, out_vector))
