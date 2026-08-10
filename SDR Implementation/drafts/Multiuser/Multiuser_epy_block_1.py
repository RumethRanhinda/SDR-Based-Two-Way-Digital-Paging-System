"""
Embedded Python Block: EchoWave Core (Fixed Source ID)
"""

import numpy as np
from gnuradio import gr
import pmt
import sys
import datetime
from PyQt5 import QtWidgets, QtCore, QtGui

class blk(gr.sync_block):
    def __init__(self, node_id_hex='A1'):
        """
        Args:
            node_id_hex: The fixed 1-byte address for this node (Hex String, e.g., 'A1').
        """
        gr.sync_block.__init__(self,
            name='EchoWave Core',
            in_sig=None,
            out_sig=None)

        self.node_id_hex = node_id_hex

        # Register Message Ports
        self.message_port_register_in(pmt.intern("msg_in"))
        self.message_port_register_in(pmt.intern("feedback_in"))
        self.message_port_register_out(pmt.intern("addr_out"))
        self.message_port_register_out(pmt.intern("msg_out"))

        # Register Handlers
        self.set_msg_handler(pmt.intern("msg_in"), self.handle_msg_in)
        self.set_msg_handler(pmt.intern("feedback_in"), self.handle_feedback)

        # Initialize GUI
        self.qapp = QtWidgets.QApplication.instance()
        if not self.qapp:
            self.qapp = QtWidgets.QApplication(sys.argv)
        
        # Pass the fixed ID to the Window
        self.gui = EchoWaveWindow(self, f"Node {node_id_hex}", node_id_hex)
        self.gui.show()
        
        # Ghost Window Fix
        self.cleanup_timer = QtCore.QTimer()
        self.cleanup_timer.timeout.connect(self.hide_ghost_window)
        self.cleanup_timer.start(200)

    def hide_ghost_window(self):
        for w in QtWidgets.QApplication.topLevelWidgets():
            if isinstance(w, QtWidgets.QMainWindow) and w != self.gui:
                w.hide()
        self.cleanup_timer.stop()

    def process_user_input(self, dst_hex, text):
        """ 
        Process input from GUI.
        Source ID is now fixed from block param (self.node_id_hex).
        """
        try:
            # Parse Hex to Int (0-255)
            src_val = int(self.node_id_hex, 16) # Uses the fixed parameter
            dst_val = int(dst_hex, 16)
            
            # 1. Address PDU: [Dest, Source]
            addr_list = [dst_val, src_val]
            pmt_addr = pmt.cons(pmt.make_dict(), pmt.init_u8vector(2, addr_list))
            self.message_port_pub(pmt.intern("addr_out"), pmt_addr)
            
            # 2. Message PDU: UTF-8 Bytes
            msg_bytes = [x for x in text.encode('utf-8')]
            pmt_msg = pmt.cons(pmt.make_dict(), pmt.init_u8vector(len(msg_bytes), msg_bytes))
            self.message_port_pub(pmt.intern("msg_out"), pmt_msg)
            
            return True
        except ValueError:
            print(f"Error: Invalid Hex Address (Src: {self.node_id_hex}, Dst: {dst_hex})")
            return False

    def handle_msg_in(self, pdu):
        try:
            # Extract Payload
            payload = bytes(pmt.to_python(pmt.cdr(pdu)))
            
            if len(payload) == 0:
                return

            msg_str = payload.decode('utf-8', errors='ignore')
            if len(msg_str.strip()) == 0: return

            # Extract Metadata
            meta = pmt.to_python(pmt.car(pdu))
            source_id = "UNKNOWN"
            if isinstance(meta, dict) and 'src_id' in meta:
                source_id = f"{meta['src_id']:02X}"
            
            self.gui.signal_rx_msg.emit(source_id, msg_str)
        except Exception:
            pass

    def handle_feedback(self, pdu):
        try:
            status = pmt.symbol_to_string(pmt.cdr(pdu))
            is_success = "ACK" in status
            self.gui.signal_ack.emit(is_success)
        except Exception:
            self.gui.signal_ack.emit(False)

    def work(self, input_items, output_items):
        return 0

# --- Standardized GUI Class ---
class EchoWaveWindow(QtWidgets.QWidget):
    signal_rx_msg = QtCore.pyqtSignal(str, str)
    signal_ack = QtCore.pyqtSignal(bool)

    def __init__(self, block_ref, win_title, my_fixed_id):
        super().__init__()
        self.block = block_ref
        self.history = {} 
        self.current_chat_id = None 
        self.win_title = win_title
        self.my_id = my_fixed_id # This is now fixed/read-only
        
        self.signal_rx_msg.connect(self.on_receive_message)
        self.signal_ack.connect(self.on_ack_received)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(f"EchoWave - {self.win_title}")
        self.resize(950, 650)
        self.setStyleSheet("font-family: Segoe UI, Arial; font-size: 14px;")
        
        main_layout = QtWidgets.QHBoxLayout(self)
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)

        # Sidebar
        sidebar = QtWidgets.QWidget()
        sidebar.setFixedWidth(280)
        sidebar.setStyleSheet("background-color: #111b21; color: #e9edef; border-right: 1px solid #333;")
        sidebar_layout = QtWidgets.QVBoxLayout(sidebar)
        
        brand = QtWidgets.QLabel("EchoWave")
        brand.setStyleSheet("font-size: 24px; font-weight: bold; color: #00a884; margin: 15px 0;")
        sidebar_layout.addWidget(brand)

        # Connection Group
        conn_group = QtWidgets.QGroupBox("CONFIGURATION")
        conn_group.setStyleSheet("QGroupBox { border: 1px solid #333; margin-top: 10px; padding-top: 10px; font-weight: bold; color: #8696a0; }")
        conn_layout = QtWidgets.QVBoxLayout(conn_group)
        
        # Row 1: Read-Only ID Display
        row1 = QtWidgets.QHBoxLayout()
        row1.addWidget(QtWidgets.QLabel("NODE ID:"))
        self.id_display = QtWidgets.QLabel(self.my_id)
        self.id_display.setStyleSheet("font-weight: bold; color: #00a884; font-size: 16px;")
        row1.addWidget(self.id_display)
        conn_layout.addLayout(row1)

        # Row 2: Target Input
        row2 = QtWidgets.QHBoxLayout()
        row2.addWidget(QtWidgets.QLabel("TO ID:"))
        self.dst_addr_input = QtWidgets.QLineEdit()
        self.dst_addr_input.setMaxLength(2)
        self.dst_addr_input.setPlaceholderText("Hex (e.g. B1)")
        self.dst_addr_input.setStyleSheet("background: #2a3942; color: white; border: none; padding: 5px;")
        self.dst_addr_input.returnPressed.connect(self.manual_connect)
        row2.addWidget(self.dst_addr_input)
        conn_layout.addLayout(row2)

        self.connect_btn = QtWidgets.QPushButton("INIT LINK")
        self.connect_btn.setStyleSheet("background-color: #00a884; color: white; border-radius: 5px; padding: 8px; font-weight: bold;")
        self.connect_btn.clicked.connect(self.manual_connect)
        conn_layout.addWidget(self.connect_btn)
        
        sidebar_layout.addWidget(conn_group)
        
        # Contact List
        sidebar_layout.addWidget(QtWidgets.QLabel("Active Feeds:"))
        self.contact_list = QtWidgets.QListWidget()
        self.contact_list.setStyleSheet("background-color: transparent; border: none; color: #d1d7db;")
        self.contact_list.itemClicked.connect(self.switch_conversation_from_list)
        sidebar_layout.addWidget(self.contact_list)

        # Right Panel
        right_panel = QtWidgets.QWidget()
        right_panel.setStyleSheet("background-color: #0b141a;") 
        right_layout = QtWidgets.QVBoxLayout(right_panel)
        right_layout.setContentsMargins(0,0,0,0)

        # Header
        header = QtWidgets.QWidget()
        header.setStyleSheet("background-color: #202c33; padding: 10px;")
        header.setFixedHeight(60)
        h_layout = QtWidgets.QHBoxLayout(header)
        
        self.chat_title = QtWidgets.QLabel("Select a Link")
        self.chat_title.setStyleSheet("font-size: 16px; font-weight: bold; color: white; background: transparent;")
        
        self.clear_btn = QtWidgets.QPushButton("Clear History")
        self.clear_btn.setStyleSheet("color: #ef5350; background: transparent; border: 1px solid #ef5350; padding: 5px; border-radius: 4px;")
        self.clear_btn.clicked.connect(self.clear_current_history)
        
        h_layout.addWidget(self.chat_title)
        h_layout.addStretch()
        h_layout.addWidget(self.clear_btn)

        # Chat Area
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("border: none; background: transparent;")
        
        self.chat_container = QtWidgets.QWidget()
        self.chat_layout = QtWidgets.QVBoxLayout(self.chat_container)
        self.chat_layout.addStretch()
        self.scroll_area.setWidget(self.chat_container)

        # Input Area
        self.footer = QtWidgets.QWidget()
        self.footer.setStyleSheet("background-color: #202c33; padding: 10px;")
        self.footer.setVisible(False)
        f_layout = QtWidgets.QHBoxLayout(self.footer)
        
        self.msg_input = QtWidgets.QLineEdit()
        self.msg_input.setPlaceholderText("Type a message")
        self.msg_input.setStyleSheet("background-color: #2a3942; color: white; border: none; padding: 12px; border-radius: 8px;")
        self.msg_input.returnPressed.connect(self.send_message)
        
        self.send_btn = QtWidgets.QPushButton("➤")
        self.send_btn.setFixedSize(45, 40)
        self.send_btn.setStyleSheet("background-color: #00a884; color: white; border-radius: 8px; font-size: 18px;")
        self.send_btn.clicked.connect(self.send_message)
        
        f_layout.addWidget(self.msg_input)
        f_layout.addWidget(self.send_btn)

        right_layout.addWidget(header)
        right_layout.addWidget(self.scroll_area)
        right_layout.addWidget(self.footer)

        main_layout.addWidget(sidebar)
        main_layout.addWidget(right_panel)

    def manual_connect(self):
        target = self.dst_addr_input.text().strip().upper()
        if len(target) > 0:
            if len(target) > 2: target = target[:2]
            self.open_conversation(target)

    def open_conversation(self, target_id):
        self.current_chat_id = target_id
        self.chat_title.setText(f"Feed: {target_id}")
        self.footer.setVisible(True)
        self.ensure_contact_exists(target_id)
        self.render_history(target_id)

    def ensure_contact_exists(self, addr):
        items = [self.contact_list.item(i).text() for i in range(self.contact_list.count())]
        if addr not in items:
            self.contact_list.addItem(addr)

    def switch_conversation_from_list(self, item):
        self.dst_addr_input.setText(item.text())
        self.open_conversation(item.text())

    def clear_current_history(self):
        if self.current_chat_id:
            self.history[self.current_chat_id] = []
            self.render_history(self.current_chat_id)

    def render_history(self, chat_id):
        while self.chat_layout.count() > 1:
            item = self.chat_layout.takeAt(1)
            if item.widget(): item.widget().deleteLater()
        
        msgs = self.history.get(chat_id, [])
        for m in msgs:
            self.add_bubble(m['text'], m['is_sender'], m['time'], m['status'])

    def save_to_history(self, chat_id, text, is_sender, status=""):
        if chat_id not in self.history: self.history[chat_id] = []
        entry = {'text': text, 'is_sender': is_sender, 'time': datetime.datetime.now().strftime("%H:%M"), 'status': status}
        self.history[chat_id].append(entry)

    def send_message(self):
        text = self.msg_input.text().strip()
        dst = self.current_chat_id 
        if not text or not dst: return

        # SRC is now handled internally via self.block.node_id_hex
        if self.block.process_user_input(dst, text):
            self.save_to_history(dst, text, True, "pending")
            self.add_bubble(text, True, datetime.datetime.now().strftime("%H:%M"), "pending")
            self.msg_input.clear()

    def on_receive_message(self, source, msg):
        self.save_to_history(source, msg, False)
        self.ensure_contact_exists(source)
        if source == self.current_chat_id:
            self.add_bubble(msg, False, datetime.datetime.now().strftime("%H:%M"), "")

    def on_ack_received(self, success):
        if self.current_chat_id in self.history:
            chat_log = self.history[self.current_chat_id]
            for i in range(len(chat_log)-1, -1, -1):
                if chat_log[i]['is_sender'] and chat_log[i]['status'] == "pending":
                    chat_log[i]['status'] = "success" if success else "fail"
                    self.render_history(self.current_chat_id)
                    break

    def add_bubble(self, text, is_sender, time, status):
        row = QtWidgets.QWidget()
        row.setStyleSheet("background: transparent;")
        layout = QtWidgets.QHBoxLayout(row)
        
        bubble = QtWidgets.QFrame()
        b_layout = QtWidgets.QVBoxLayout(bubble)
        
        if is_sender:
            bubble.setStyleSheet("background-color: #005c4b; border-radius: 10px; margin-left: 50px;")
            layout.addStretch()
            layout.addWidget(bubble)
        else:
            bubble.setStyleSheet("background-color: #202c33; border-radius: 10px; margin-right: 50px;")
            layout.addWidget(bubble)
            layout.addStretch()
            
        lbl = QtWidgets.QLabel(text)
        lbl.setWordWrap(True)
        lbl.setStyleSheet("color: #e9edef; font-size: 14px; background: transparent; border: none;")
        b_layout.addWidget(lbl)
        
        meta = QtWidgets.QHBoxLayout()
        meta.addStretch()
        t_lbl = QtWidgets.QLabel(time)
        t_lbl.setStyleSheet("color: #8696a0; font-size: 11px; background: transparent; border: none;")
        meta.addWidget(t_lbl)
        
        if is_sender:
            icon = "🕒"
            color = "#8696a0"
            if status == "success": 
                icon = "✓✓"
                color = "#53bdeb"
            elif status == "fail": 
                icon = "!"
                color = "red"
            
            s_lbl = QtWidgets.QLabel(icon)
            s_lbl.setStyleSheet(f"color: {color}; font-size: 11px; font-weight: bold; background: transparent; border: none;")
            meta.addWidget(s_lbl)
            
        b_layout.addLayout(meta)
        self.chat_layout.addWidget(row)
        QtCore.QTimer.singleShot(10, lambda: self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum()))
