#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Lets See how this works
# Author: Rumeth Samarasinghe
# GNU Radio version: 3.10.12.0

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import blocks
from gnuradio import blocks, gr
from gnuradio import channels
from gnuradio.filter import firdes
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import gr, pdu
import Multiuser_epy_block_0 as epy_block_0  # embedded python block
import Multiuser_epy_block_0_0 as epy_block_0_0  # embedded python block
import Multiuser_epy_block_0_1 as epy_block_0_1  # embedded python block
import Multiuser_epy_block_1 as epy_block_1  # embedded python block
import Multiuser_epy_block_1_0 as epy_block_1_0  # embedded python block
import Multiuser_epy_block_1_1 as epy_block_1_1  # embedded python block
import Multiuser_epy_block_3 as epy_block_3  # embedded python block
import Multiuser_epy_block_3_0 as epy_block_3_0  # embedded python block
import Multiuser_epy_block_3_1 as epy_block_3_1  # embedded python block
import Multiuser_epy_block_4_0 as epy_block_4_0  # embedded python block
import Multiuser_epy_block_4_0_0 as epy_block_4_0_0  # embedded python block
import Multiuser_epy_block_4_0_1 as epy_block_4_0_1  # embedded python block
import sip
import threading



class Multiuser(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Lets See how this works", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Lets See how this works")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Multiuser")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.qpsk = qpsk = digital.constellation_rect([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j] , [0, 1, 3, 2],
        4, 2, 2, 1, 1).base()
        self.nfilts = nfilts = 32
        self.access_key = access_key = '1110000101011010111010001001001111100001010110101110100010010011'
        self.variable_adaptive_algorithm_0_1 = variable_adaptive_algorithm_0_1 = digital.adaptive_algorithm_cma( qpsk, .0001, 4).base()
        self.variable_adaptive_algorithm_0_0 = variable_adaptive_algorithm_0_0 = digital.adaptive_algorithm_cma( qpsk, .0001, 4).base()
        self.variable_adaptive_algorithm_0 = variable_adaptive_algorithm_0 = digital.adaptive_algorithm_cma( qpsk, .0001, 4).base()
        self.user_3 = user_3 = '00'
        self.user_2 = user_2 = 'A1'
        self.user_1 = user_1 = 'B1'
        self.time_offset = time_offset = 1
        self.taps = taps = [0.6,0.4+0.2j,0.3-0.5j]
        self.sps_1 = sps_1 = 4
        self.sps_0 = sps_0 = 4
        self.samp_rate = samp_rate = 48e3
        self.rrc_taps_1 = rrc_taps_1 = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 11*sps*nfilts)
        self.rrc_taps_0 = rrc_taps_0 = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 11*sps*nfilts)
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 11*sps*nfilts)
        self.qpsk_1 = qpsk_1 = digital.constellation_rect([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j] , [0, 1, 3, 2],
        4, 2, 2, 1, 1).base()
        self.qpsk_0 = qpsk_0 = digital.constellation_rect([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j] , [0, 1, 3, 2],
        4, 2, 2, 1, 1).base()
        self.phase_bw_1 = phase_bw_1 = 62.8e-3
        self.phase_bw_0 = phase_bw_0 = 62.8e-3
        self.phase_bw = phase_bw = 62.8e-3
        self.noise_volt = noise_volt = 100e-6
        self.nfilts_1 = nfilts_1 = 32
        self.nfilts_0 = nfilts_0 = 32
        self.max_dev_2 = max_dev_2 = 0.05
        self.max_dev_1 = max_dev_1 = 0.05
        self.max_dev_0_1 = max_dev_0_1 = 0.05
        self.max_dev_0_0 = max_dev_0_0 = 0.05
        self.max_dev_0 = max_dev_0 = 0.05
        self.max_dev = max_dev = 0.05
        self.hdr_format_1 = hdr_format_1 = digital.header_format_default(access_key, 0)
        self.hdr_format_0 = hdr_format_0 = digital.header_format_default(access_key, 0)
        self.hdr_format = hdr_format = digital.header_format_default(access_key, 0)
        self.freq_offset = freq_offset = 0
        self.freq = freq = 2.4e9
        self.excess_bw_1 = excess_bw_1 = 0.35
        self.excess_bw_0 = excess_bw_0 = 0.35
        self.excess_bw = excess_bw = 0.35
        self.damp_fac_1 = damp_fac_1 = 0.707
        self.damp_fac_0 = damp_fac_0 = 0.707
        self.damp_fac = damp_fac = 0.707
        self.access_key_1 = access_key_1 = '1110000101011010111010001001001111100001010110101110100010010011'
        self.access_key_0 = access_key_0 = '1110000101011010111010001001001111100001010110101110100010010011'

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_time_sink_x_0_0_1 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "I am quite hungry", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_1.enable_tags(True)
        self.qtgui_time_sink_x_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_1_win)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "I am quite hungry", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "I am quite hungry", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_const_sink_x_1_0_3 = qtgui.const_sink_c(
            1024, #size
            "RX constallation", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_1_0_3.set_update_time(0.10)
        self.qtgui_const_sink_x_1_0_3.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_1_0_3.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_1_0_3.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1_0_3.enable_autoscale(False)
        self.qtgui_const_sink_x_1_0_3.enable_grid(False)
        self.qtgui_const_sink_x_1_0_3.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1_0_3.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1_0_3.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1_0_3.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1_0_3.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1_0_3.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1_0_3.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1_0_3.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_1_0_3_win = sip.wrapinstance(self.qtgui_const_sink_x_1_0_3.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_1_0_3_win)
        self.qtgui_const_sink_x_1_0_2 = qtgui.const_sink_c(
            1024, #size
            "RX constallation", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_1_0_2.set_update_time(0.10)
        self.qtgui_const_sink_x_1_0_2.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_1_0_2.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_1_0_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1_0_2.enable_autoscale(False)
        self.qtgui_const_sink_x_1_0_2.enable_grid(False)
        self.qtgui_const_sink_x_1_0_2.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1_0_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1_0_2.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1_0_2.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1_0_2.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1_0_2.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1_0_2.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1_0_2.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_1_0_2_win = sip.wrapinstance(self.qtgui_const_sink_x_1_0_2.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_1_0_2_win)
        self.qtgui_const_sink_x_1_0_0_1 = qtgui.const_sink_c(
            1024, #size
            "TX Constallation", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_1_0_0_1.set_update_time(0.10)
        self.qtgui_const_sink_x_1_0_0_1.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_1_0_0_1.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_1_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1_0_0_1.enable_autoscale(True)
        self.qtgui_const_sink_x_1_0_0_1.enable_grid(True)
        self.qtgui_const_sink_x_1_0_0_1.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1_0_0_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1_0_0_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1_0_0_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1_0_0_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_1_0_0_1_win = sip.wrapinstance(self.qtgui_const_sink_x_1_0_0_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_1_0_0_1_win)
        self.qtgui_const_sink_x_1_0_0_0 = qtgui.const_sink_c(
            1024, #size
            "TX Constallation", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_1_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_1_0_0_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_1_0_0_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1_0_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_1_0_0_0.enable_grid(True)
        self.qtgui_const_sink_x_1_0_0_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_1_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_1_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_1_0_0_0_win)
        self.qtgui_const_sink_x_1_0_0 = qtgui.const_sink_c(
            1024, #size
            "TX Constallation", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_1_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_1_0_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_1_0_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1_0_0.enable_autoscale(True)
        self.qtgui_const_sink_x_1_0_0.enable_grid(True)
        self.qtgui_const_sink_x_1_0_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_1_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_1_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_1_0_0_win)
        self.qtgui_const_sink_x_1_0 = qtgui.const_sink_c(
            1024, #size
            "RX constallation", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_1_0.set_update_time(0.10)
        self.qtgui_const_sink_x_1_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_1_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1_0.enable_autoscale(False)
        self.qtgui_const_sink_x_1_0.enable_grid(False)
        self.qtgui_const_sink_x_1_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_1_0_win = sip.wrapinstance(self.qtgui_const_sink_x_1_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_1_0_win)
        self.pdu_tagged_stream_to_pdu_0_1 = pdu.tagged_stream_to_pdu(gr.types.byte_t, 'packet_len')
        self.pdu_tagged_stream_to_pdu_0_0_0_1 = pdu.tagged_stream_to_pdu(gr.types.byte_t, 'packet_len')
        self.pdu_tagged_stream_to_pdu_0_0_0_0 = pdu.tagged_stream_to_pdu(gr.types.byte_t, 'packet_len')
        self.pdu_tagged_stream_to_pdu_0_0_0 = pdu.tagged_stream_to_pdu(gr.types.byte_t, 'packet_len')
        self.pdu_tagged_stream_to_pdu_0_0 = pdu.tagged_stream_to_pdu(gr.types.byte_t, 'packet_len')
        self.pdu_tagged_stream_to_pdu_0 = pdu.tagged_stream_to_pdu(gr.types.byte_t, 'packet_len')
        self.pdu_pdu_to_tagged_stream_2_1 = pdu.pdu_to_tagged_stream(gr.types.byte_t, 'packet_len')
        self.pdu_pdu_to_tagged_stream_2_0 = pdu.pdu_to_tagged_stream(gr.types.byte_t, 'packet_len')
        self.pdu_pdu_to_tagged_stream_2 = pdu.pdu_to_tagged_stream(gr.types.byte_t, 'packet_len')
        self.pdu_pdu_to_tagged_stream_1_1 = pdu.pdu_to_tagged_stream(gr.types.byte_t, 'packet_len')
        self.pdu_pdu_to_tagged_stream_1_0 = pdu.pdu_to_tagged_stream(gr.types.byte_t, 'packet_len')
        self.pdu_pdu_to_tagged_stream_1 = pdu.pdu_to_tagged_stream(gr.types.byte_t, 'packet_len')
        self.pdu_pdu_to_tagged_stream_0_1 = pdu.pdu_to_tagged_stream(gr.types.byte_t, 'packet_len')
        self.pdu_pdu_to_tagged_stream_0_0 = pdu.pdu_to_tagged_stream(gr.types.byte_t, 'packet_len')
        self.pdu_pdu_to_tagged_stream_0 = pdu.pdu_to_tagged_stream(gr.types.byte_t, 'packet_len')
        self.epy_block_4_0_1 = epy_block_4_0_1.blk(my_addr_hex=user_3)
        self.epy_block_4_0_0 = epy_block_4_0_0.blk(my_addr_hex=user_2)
        self.epy_block_4_0 = epy_block_4_0.blk(my_addr_hex=user_1)
        self.epy_block_3_1 = epy_block_3_1.blk(num_dummy_bytes=100)
        self.epy_block_3_0 = epy_block_3_0.blk(num_dummy_bytes=100)
        self.epy_block_3 = epy_block_3.blk(num_dummy_bytes=100)
        self.epy_block_1_1 = epy_block_1_1.blk(node_id_hex=user_3)
        self.epy_block_1_0 = epy_block_1_0.blk(node_id_hex=user_2)
        self.epy_block_1 = epy_block_1.blk(node_id_hex=user_1)
        self.epy_block_0_1 = epy_block_0_1.blk(max_payload_len=250, retry_limit=15, timeout_ms=100, base_backoff_ms=10)
        self.epy_block_0_0 = epy_block_0_0.blk(max_payload_len=250, retry_limit=15, timeout_ms=100, base_backoff_ms=10)
        self.epy_block_0 = epy_block_0.blk(max_payload_len=250, retry_limit=15, timeout_ms=100, base_backoff_ms=10)
        self.digital_symbol_sync_xx_0_1_0_1 = digital.symbol_sync_cc(
            digital.TED_GARDNER,
            sps,
            phase_bw,
            damp_fac,
            1.0,
            max_dev,
            4,
            digital.constellation_bpsk().base(),
            digital.IR_PFB_MF,
            32,
            rrc_taps)
        self.digital_symbol_sync_xx_0_1_0_0 = digital.symbol_sync_cc(
            digital.TED_GARDNER,
            sps,
            phase_bw,
            damp_fac,
            1.0,
            max_dev,
            4,
            digital.constellation_bpsk().base(),
            digital.IR_PFB_MF,
            32,
            rrc_taps)
        self.digital_symbol_sync_xx_0_1_0 = digital.symbol_sync_cc(
            digital.TED_GARDNER,
            sps,
            phase_bw,
            damp_fac,
            1.0,
            max_dev,
            4,
            digital.constellation_bpsk().base(),
            digital.IR_PFB_MF,
            32,
            rrc_taps)
        self.digital_protocol_formatter_async_0_1 = digital.protocol_formatter_async(hdr_format)
        self.digital_protocol_formatter_async_0_0 = digital.protocol_formatter_async(hdr_format)
        self.digital_protocol_formatter_async_0 = digital.protocol_formatter_async(hdr_format)
        self.digital_map_bb_0_0_1 = digital.map_bb([0, 1, 3, 2])
        self.digital_map_bb_0_0_0 = digital.map_bb([0, 1, 3, 2])
        self.digital_map_bb_0_0 = digital.map_bb([0, 1, 3, 2])
        self.digital_linear_equalizer_0_1_0_1 = digital.linear_equalizer(15, 4, variable_adaptive_algorithm_0, True, [ ], 'corr_est')
        self.digital_linear_equalizer_0_1_0_0 = digital.linear_equalizer(15, 4, variable_adaptive_algorithm_0, True, [ ], 'corr_est')
        self.digital_linear_equalizer_0_1_0 = digital.linear_equalizer(15, 4, variable_adaptive_algorithm_0, True, [ ], 'corr_est')
        self.digital_diff_decoder_bb_0_0_1 = digital.diff_decoder_bb(4, digital.DIFF_DIFFERENTIAL)
        self.digital_diff_decoder_bb_0_0_0 = digital.diff_decoder_bb(4, digital.DIFF_DIFFERENTIAL)
        self.digital_diff_decoder_bb_0_0 = digital.diff_decoder_bb(4, digital.DIFF_DIFFERENTIAL)
        self.digital_crc_check_0_0_1 = digital.crc_check(32, 0x4C11DB7, 0xFFFFFFFF, 0xFFFFFFFF, True, True, False, False, 0)
        self.digital_crc_check_0_0_0 = digital.crc_check(32, 0x4C11DB7, 0xFFFFFFFF, 0xFFFFFFFF, True, True, False, False, 0)
        self.digital_crc_check_0_0 = digital.crc_check(32, 0x4C11DB7, 0xFFFFFFFF, 0xFFFFFFFF, True, True, False, False, 0)
        self.digital_crc_append_0_1 = digital.crc_append(32, 0x4C11DB7, 0xFFFFFFFF, 0xFFFFFFFF, True, True, False, 0)
        self.digital_crc_append_0_0 = digital.crc_append(32, 0x4C11DB7, 0xFFFFFFFF, 0xFFFFFFFF, True, True, False, 0)
        self.digital_crc_append_0 = digital.crc_append(32, 0x4C11DB7, 0xFFFFFFFF, 0xFFFFFFFF, True, True, False, 0)
        self.digital_costas_loop_cc_0_0_1 = digital.costas_loop_cc(phase_bw, 4, False)
        self.digital_costas_loop_cc_0_0_0 = digital.costas_loop_cc(phase_bw, 4, False)
        self.digital_costas_loop_cc_0_0 = digital.costas_loop_cc(phase_bw, 4, False)
        self.digital_correlate_access_code_xx_ts_0_0_1 = digital.correlate_access_code_bb_ts("1110000101011010111010001001001111100001010110101110100010010011",
          2, 'packet_len')
        self.digital_correlate_access_code_xx_ts_0_0_0 = digital.correlate_access_code_bb_ts("1110000101011010111010001001001111100001010110101110100010010011",
          2, 'packet_len')
        self.digital_correlate_access_code_xx_ts_0_0 = digital.correlate_access_code_bb_ts("1110000101011010111010001001001111100001010110101110100010010011",
          2, 'packet_len')
        self.digital_constellation_modulator_0_1 = digital.generic_mod(
            constellation=qpsk,
            differential=True,
            samples_per_symbol=sps,
            pre_diff_code=True,
            excess_bw=excess_bw,
            verbose=False,
            log=False,
            truncate=False)
        self.digital_constellation_modulator_0_0 = digital.generic_mod(
            constellation=qpsk,
            differential=True,
            samples_per_symbol=sps,
            pre_diff_code=True,
            excess_bw=excess_bw,
            verbose=False,
            log=False,
            truncate=False)
        self.digital_constellation_modulator_0 = digital.generic_mod(
            constellation=qpsk,
            differential=True,
            samples_per_symbol=sps,
            pre_diff_code=True,
            excess_bw=excess_bw,
            verbose=False,
            log=False,
            truncate=False)
        self.digital_constellation_decoder_cb_0_0_1 = digital.constellation_decoder_cb(qpsk)
        self.digital_constellation_decoder_cb_0_0_0 = digital.constellation_decoder_cb(qpsk)
        self.digital_constellation_decoder_cb_0_0 = digital.constellation_decoder_cb(qpsk)
        self.channels_channel_model_0_1 = channels.channel_model(
            noise_voltage=noise_volt,
            frequency_offset=freq_offset,
            epsilon=time_offset,
            taps=taps,
            noise_seed=0,
            block_tags=False)
        self.blocks_unpack_k_bits_bb_0_0_1 = blocks.unpack_k_bits_bb(2)
        self.blocks_unpack_k_bits_bb_0_0_0 = blocks.unpack_k_bits_bb(2)
        self.blocks_unpack_k_bits_bb_0_0 = blocks.unpack_k_bits_bb(2)
        self.blocks_uchar_to_float_0_0_1 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0_0_0 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0_0 = blocks.uchar_to_float()
        self.blocks_throttle2_0_1 = blocks.throttle( gr.sizeof_char*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_throttle2_0_0 = blocks.throttle( gr.sizeof_char*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_char*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_tagged_stream_mux_0_1 = blocks.tagged_stream_mux(gr.sizeof_char*1, 'packet_len', 0)
        self.blocks_tagged_stream_mux_0_0 = blocks.tagged_stream_mux(gr.sizeof_char*1, 'packet_len', 0)
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_char*1, 'packet_len', 0)
        self.blocks_repack_bits_bb_1_0_0_0_1 = blocks.repack_bits_bb(1, 8, "packet_len", False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_1_0_0_0_0 = blocks.repack_bits_bb(1, 8, "packet_len", False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_1_0_0_0 = blocks.repack_bits_bb(1, 8, "packet_len", False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_1 = blocks.repack_bits_bb(8, 1, "packet_len", False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(8, 1, "packet_len", False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, 1, "packet_len", False, gr.GR_MSB_FIRST)
        self.blocks_pack_k_bits_bb_0_0_1 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0_0_0 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0_0 = blocks.pack_k_bits_bb(8)
        self.blocks_message_debug_0_1 = blocks.message_debug(True, gr.log_levels.info)
        self.blocks_message_debug_0_0 = blocks.message_debug(True, gr.log_levels.info)
        self.blocks_message_debug_0 = blocks.message_debug(True, gr.log_levels.info)
        self.blocks_add_xx_0 = blocks.add_vcc(1)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.digital_crc_append_0, 'out'), (self.digital_protocol_formatter_async_0, 'in'))
        self.msg_connect((self.digital_crc_append_0_0, 'out'), (self.digital_protocol_formatter_async_0_0, 'in'))
        self.msg_connect((self.digital_crc_append_0_1, 'out'), (self.digital_protocol_formatter_async_0_1, 'in'))
        self.msg_connect((self.digital_crc_check_0_0, 'ok'), (self.epy_block_4_0, 'pdu_in'))
        self.msg_connect((self.digital_crc_check_0_0_0, 'ok'), (self.epy_block_4_0_0, 'pdu_in'))
        self.msg_connect((self.digital_crc_check_0_0_1, 'ok'), (self.epy_block_4_0_1, 'pdu_in'))
        self.msg_connect((self.digital_protocol_formatter_async_0, 'header'), (self.pdu_pdu_to_tagged_stream_0, 'pdus'))
        self.msg_connect((self.digital_protocol_formatter_async_0, 'payload'), (self.pdu_pdu_to_tagged_stream_1, 'pdus'))
        self.msg_connect((self.digital_protocol_formatter_async_0_0, 'header'), (self.pdu_pdu_to_tagged_stream_0_0, 'pdus'))
        self.msg_connect((self.digital_protocol_formatter_async_0_0, 'payload'), (self.pdu_pdu_to_tagged_stream_1_0, 'pdus'))
        self.msg_connect((self.digital_protocol_formatter_async_0_1, 'header'), (self.pdu_pdu_to_tagged_stream_0_1, 'pdus'))
        self.msg_connect((self.digital_protocol_formatter_async_0_1, 'payload'), (self.pdu_pdu_to_tagged_stream_1_1, 'pdus'))
        self.msg_connect((self.epy_block_0, 'packet_out'), (self.digital_crc_append_0, 'in'))
        self.msg_connect((self.epy_block_0, 'feedback_out'), (self.epy_block_1, 'feedback_in'))
        self.msg_connect((self.epy_block_0_0, 'packet_out'), (self.digital_crc_append_0_0, 'in'))
        self.msg_connect((self.epy_block_0_0, 'feedback_out'), (self.epy_block_1_0, 'feedback_in'))
        self.msg_connect((self.epy_block_0_1, 'packet_out'), (self.digital_crc_append_0_1, 'in'))
        self.msg_connect((self.epy_block_0_1, 'feedback_out'), (self.epy_block_1_1, 'feedback_in'))
        self.msg_connect((self.epy_block_1, 'addr_out'), (self.epy_block_0, 'addr_in'))
        self.msg_connect((self.epy_block_1, 'msg_out'), (self.epy_block_0, 'msg_in'))
        self.msg_connect((self.epy_block_1_0, 'msg_out'), (self.epy_block_0_0, 'msg_in'))
        self.msg_connect((self.epy_block_1_0, 'addr_out'), (self.epy_block_0_0, 'addr_in'))
        self.msg_connect((self.epy_block_1_1, 'addr_out'), (self.epy_block_0_1, 'addr_in'))
        self.msg_connect((self.epy_block_1_1, 'msg_out'), (self.epy_block_0_1, 'msg_in'))
        self.msg_connect((self.epy_block_3, 'pdu_out'), (self.blocks_message_debug_0, 'print'))
        self.msg_connect((self.epy_block_3, 'pdu_out'), (self.pdu_pdu_to_tagged_stream_2, 'pdus'))
        self.msg_connect((self.epy_block_3_0, 'pdu_out'), (self.blocks_message_debug_0_0, 'print'))
        self.msg_connect((self.epy_block_3_0, 'pdu_out'), (self.pdu_pdu_to_tagged_stream_2_0, 'pdus'))
        self.msg_connect((self.epy_block_3_1, 'pdu_out'), (self.blocks_message_debug_0_1, 'print'))
        self.msg_connect((self.epy_block_3_1, 'pdu_out'), (self.pdu_pdu_to_tagged_stream_2_1, 'pdus'))
        self.msg_connect((self.epy_block_4_0, 'ack_reply_out'), (self.digital_crc_append_0, 'in'))
        self.msg_connect((self.epy_block_4_0, 'ack_out'), (self.epy_block_0, 'ack_in'))
        self.msg_connect((self.epy_block_4_0, 'msg_out'), (self.epy_block_1, 'msg_in'))
        self.msg_connect((self.epy_block_4_0_0, 'ack_reply_out'), (self.digital_crc_append_0_0, 'in'))
        self.msg_connect((self.epy_block_4_0_0, 'ack_out'), (self.epy_block_0_0, 'ack_in'))
        self.msg_connect((self.epy_block_4_0_0, 'msg_out'), (self.epy_block_1_0, 'msg_in'))
        self.msg_connect((self.epy_block_4_0_1, 'ack_reply_out'), (self.digital_crc_append_0_1, 'in'))
        self.msg_connect((self.epy_block_4_0_1, 'ack_out'), (self.epy_block_0_1, 'ack_in'))
        self.msg_connect((self.epy_block_4_0_1, 'msg_out'), (self.epy_block_1_1, 'msg_in'))
        self.msg_connect((self.pdu_tagged_stream_to_pdu_0, 'pdus'), (self.epy_block_3, 'pdu_in'))
        self.msg_connect((self.pdu_tagged_stream_to_pdu_0_0, 'pdus'), (self.epy_block_3_0, 'pdu_in'))
        self.msg_connect((self.pdu_tagged_stream_to_pdu_0_0_0, 'pdus'), (self.digital_crc_check_0_0, 'in'))
        self.msg_connect((self.pdu_tagged_stream_to_pdu_0_0_0_0, 'pdus'), (self.digital_crc_check_0_0_0, 'in'))
        self.msg_connect((self.pdu_tagged_stream_to_pdu_0_0_0_1, 'pdus'), (self.digital_crc_check_0_0_1, 'in'))
        self.msg_connect((self.pdu_tagged_stream_to_pdu_0_1, 'pdus'), (self.epy_block_3_1, 'pdu_in'))
        self.connect((self.blocks_add_xx_0, 0), (self.channels_channel_model_0_1, 0))
        self.connect((self.blocks_pack_k_bits_bb_0_0, 0), (self.digital_correlate_access_code_xx_ts_0_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0_0_0, 0), (self.digital_correlate_access_code_xx_ts_0_0_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0_0_1, 0), (self.digital_correlate_access_code_xx_ts_0_0_1, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.blocks_throttle2_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_1, 0), (self.blocks_throttle2_0_1, 0))
        self.connect((self.blocks_repack_bits_bb_1_0_0_0, 0), (self.pdu_tagged_stream_to_pdu_0_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_1_0_0_0_0, 0), (self.pdu_tagged_stream_to_pdu_0_0_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_1_0_0_0_1, 0), (self.pdu_tagged_stream_to_pdu_0_0_0_1, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.pdu_tagged_stream_to_pdu_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0_0, 0), (self.pdu_tagged_stream_to_pdu_0_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0_1, 0), (self.pdu_tagged_stream_to_pdu_0_1, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.blocks_throttle2_0_0, 0), (self.digital_constellation_modulator_0_0, 0))
        self.connect((self.blocks_throttle2_0_1, 0), (self.digital_constellation_modulator_0_1, 0))
        self.connect((self.blocks_uchar_to_float_0_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_uchar_to_float_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.blocks_uchar_to_float_0_0_1, 0), (self.qtgui_time_sink_x_0_0_1, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0_0, 0), (self.blocks_pack_k_bits_bb_0_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0_0_0, 0), (self.blocks_pack_k_bits_bb_0_0_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0_0_1, 0), (self.blocks_pack_k_bits_bb_0_0_1, 0))
        self.connect((self.channels_channel_model_0_1, 0), (self.digital_symbol_sync_xx_0_1_0, 0))
        self.connect((self.channels_channel_model_0_1, 0), (self.digital_symbol_sync_xx_0_1_0_0, 0))
        self.connect((self.channels_channel_model_0_1, 0), (self.digital_symbol_sync_xx_0_1_0_1, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0, 0), (self.digital_diff_decoder_bb_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0_0, 0), (self.digital_diff_decoder_bb_0_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0_1, 0), (self.digital_diff_decoder_bb_0_0_1, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.qtgui_const_sink_x_1_0_0, 0))
        self.connect((self.digital_constellation_modulator_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.digital_constellation_modulator_0_0, 0), (self.qtgui_const_sink_x_1_0_0_0, 0))
        self.connect((self.digital_constellation_modulator_0_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.digital_constellation_modulator_0_1, 0), (self.qtgui_const_sink_x_1_0_0_1, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_0_0, 0), (self.blocks_repack_bits_bb_1_0_0_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_0_0, 0), (self.blocks_uchar_to_float_0_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_0_0_0, 0), (self.blocks_repack_bits_bb_1_0_0_0_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_0_0_0, 0), (self.blocks_uchar_to_float_0_0_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_0_0_1, 0), (self.blocks_repack_bits_bb_1_0_0_0_1, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_0_0_1, 0), (self.blocks_uchar_to_float_0_0_1, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.digital_constellation_decoder_cb_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.qtgui_const_sink_x_1_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0_0, 0), (self.digital_constellation_decoder_cb_0_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0_0, 0), (self.qtgui_const_sink_x_1_0_2, 0))
        self.connect((self.digital_costas_loop_cc_0_0_1, 0), (self.digital_constellation_decoder_cb_0_0_1, 0))
        self.connect((self.digital_costas_loop_cc_0_0_1, 0), (self.qtgui_const_sink_x_1_0_3, 0))
        self.connect((self.digital_diff_decoder_bb_0_0, 0), (self.digital_map_bb_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0_0_0, 0), (self.digital_map_bb_0_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0_0_1, 0), (self.digital_map_bb_0_0_1, 0))
        self.connect((self.digital_linear_equalizer_0_1_0, 0), (self.digital_costas_loop_cc_0_0, 0))
        self.connect((self.digital_linear_equalizer_0_1_0_0, 0), (self.digital_costas_loop_cc_0_0_0, 0))
        self.connect((self.digital_linear_equalizer_0_1_0_1, 0), (self.digital_costas_loop_cc_0_0_1, 0))
        self.connect((self.digital_map_bb_0_0, 0), (self.blocks_unpack_k_bits_bb_0_0, 0))
        self.connect((self.digital_map_bb_0_0_0, 0), (self.blocks_unpack_k_bits_bb_0_0_0, 0))
        self.connect((self.digital_map_bb_0_0_1, 0), (self.blocks_unpack_k_bits_bb_0_0_1, 0))
        self.connect((self.digital_symbol_sync_xx_0_1_0, 0), (self.digital_linear_equalizer_0_1_0, 0))
        self.connect((self.digital_symbol_sync_xx_0_1_0_0, 0), (self.digital_linear_equalizer_0_1_0_0, 0))
        self.connect((self.digital_symbol_sync_xx_0_1_0_1, 0), (self.digital_linear_equalizer_0_1_0_1, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_0, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_0_0, 0), (self.blocks_tagged_stream_mux_0_0, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_0_1, 0), (self.blocks_tagged_stream_mux_0_1, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_1, 0), (self.blocks_tagged_stream_mux_0, 1))
        self.connect((self.pdu_pdu_to_tagged_stream_1_0, 0), (self.blocks_tagged_stream_mux_0_0, 1))
        self.connect((self.pdu_pdu_to_tagged_stream_1_1, 0), (self.blocks_tagged_stream_mux_0_1, 1))
        self.connect((self.pdu_pdu_to_tagged_stream_2, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_2_0, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.pdu_pdu_to_tagged_stream_2_1, 0), (self.blocks_repack_bits_bb_0_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Multiuser")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))
        self.set_rrc_taps_0(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))
        self.set_rrc_taps_1(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))
        self.digital_symbol_sync_xx_0_1_0.set_sps(self.sps)
        self.digital_symbol_sync_xx_0_1_0_0.set_sps(self.sps)
        self.digital_symbol_sync_xx_0_1_0_1.set_sps(self.sps)

    def get_qpsk(self):
        return self.qpsk

    def set_qpsk(self, qpsk):
        self.qpsk = qpsk
        self.digital_constellation_decoder_cb_0_0.set_constellation(self.qpsk)
        self.digital_constellation_decoder_cb_0_0_0.set_constellation(self.qpsk)
        self.digital_constellation_decoder_cb_0_0_1.set_constellation(self.qpsk)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))
        self.set_rrc_taps_0(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))
        self.set_rrc_taps_1(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_access_key(self):
        return self.access_key

    def set_access_key(self, access_key):
        self.access_key = access_key
        self.set_hdr_format(digital.header_format_default(self.access_key, 0))
        self.set_hdr_format_0(digital.header_format_default(self.access_key, 0))
        self.set_hdr_format_1(digital.header_format_default(self.access_key, 0))

    def get_variable_adaptive_algorithm_0_1(self):
        return self.variable_adaptive_algorithm_0_1

    def set_variable_adaptive_algorithm_0_1(self, variable_adaptive_algorithm_0_1):
        self.variable_adaptive_algorithm_0_1 = variable_adaptive_algorithm_0_1

    def get_variable_adaptive_algorithm_0_0(self):
        return self.variable_adaptive_algorithm_0_0

    def set_variable_adaptive_algorithm_0_0(self, variable_adaptive_algorithm_0_0):
        self.variable_adaptive_algorithm_0_0 = variable_adaptive_algorithm_0_0

    def get_variable_adaptive_algorithm_0(self):
        return self.variable_adaptive_algorithm_0

    def set_variable_adaptive_algorithm_0(self, variable_adaptive_algorithm_0):
        self.variable_adaptive_algorithm_0 = variable_adaptive_algorithm_0

    def get_user_3(self):
        return self.user_3

    def set_user_3(self, user_3):
        self.user_3 = user_3
        self.epy_block_1_1.node_id_hex = self.user_3

    def get_user_2(self):
        return self.user_2

    def set_user_2(self, user_2):
        self.user_2 = user_2
        self.epy_block_1_0.node_id_hex = self.user_2

    def get_user_1(self):
        return self.user_1

    def set_user_1(self, user_1):
        self.user_1 = user_1
        self.epy_block_1.node_id_hex = self.user_1

    def get_time_offset(self):
        return self.time_offset

    def set_time_offset(self, time_offset):
        self.time_offset = time_offset
        self.channels_channel_model_0_1.set_timing_offset(self.time_offset)

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.channels_channel_model_0_1.set_taps(self.taps)

    def get_sps_1(self):
        return self.sps_1

    def set_sps_1(self, sps_1):
        self.sps_1 = sps_1

    def get_sps_0(self):
        return self.sps_0

    def set_sps_0(self, sps_0):
        self.sps_0 = sps_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_1.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_1.set_samp_rate(self.samp_rate)

    def get_rrc_taps_1(self):
        return self.rrc_taps_1

    def set_rrc_taps_1(self, rrc_taps_1):
        self.rrc_taps_1 = rrc_taps_1

    def get_rrc_taps_0(self):
        return self.rrc_taps_0

    def set_rrc_taps_0(self, rrc_taps_0):
        self.rrc_taps_0 = rrc_taps_0

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps

    def get_qpsk_1(self):
        return self.qpsk_1

    def set_qpsk_1(self, qpsk_1):
        self.qpsk_1 = qpsk_1

    def get_qpsk_0(self):
        return self.qpsk_0

    def set_qpsk_0(self, qpsk_0):
        self.qpsk_0 = qpsk_0

    def get_phase_bw_1(self):
        return self.phase_bw_1

    def set_phase_bw_1(self, phase_bw_1):
        self.phase_bw_1 = phase_bw_1

    def get_phase_bw_0(self):
        return self.phase_bw_0

    def set_phase_bw_0(self, phase_bw_0):
        self.phase_bw_0 = phase_bw_0

    def get_phase_bw(self):
        return self.phase_bw

    def set_phase_bw(self, phase_bw):
        self.phase_bw = phase_bw
        self.digital_costas_loop_cc_0_0.set_loop_bandwidth(self.phase_bw)
        self.digital_costas_loop_cc_0_0_0.set_loop_bandwidth(self.phase_bw)
        self.digital_costas_loop_cc_0_0_1.set_loop_bandwidth(self.phase_bw)
        self.digital_symbol_sync_xx_0_1_0.set_loop_bandwidth(self.phase_bw)
        self.digital_symbol_sync_xx_0_1_0_0.set_loop_bandwidth(self.phase_bw)
        self.digital_symbol_sync_xx_0_1_0_1.set_loop_bandwidth(self.phase_bw)

    def get_noise_volt(self):
        return self.noise_volt

    def set_noise_volt(self, noise_volt):
        self.noise_volt = noise_volt
        self.channels_channel_model_0_1.set_noise_voltage(self.noise_volt)

    def get_nfilts_1(self):
        return self.nfilts_1

    def set_nfilts_1(self, nfilts_1):
        self.nfilts_1 = nfilts_1

    def get_nfilts_0(self):
        return self.nfilts_0

    def set_nfilts_0(self, nfilts_0):
        self.nfilts_0 = nfilts_0

    def get_max_dev_2(self):
        return self.max_dev_2

    def set_max_dev_2(self, max_dev_2):
        self.max_dev_2 = max_dev_2

    def get_max_dev_1(self):
        return self.max_dev_1

    def set_max_dev_1(self, max_dev_1):
        self.max_dev_1 = max_dev_1

    def get_max_dev_0_1(self):
        return self.max_dev_0_1

    def set_max_dev_0_1(self, max_dev_0_1):
        self.max_dev_0_1 = max_dev_0_1

    def get_max_dev_0_0(self):
        return self.max_dev_0_0

    def set_max_dev_0_0(self, max_dev_0_0):
        self.max_dev_0_0 = max_dev_0_0

    def get_max_dev_0(self):
        return self.max_dev_0

    def set_max_dev_0(self, max_dev_0):
        self.max_dev_0 = max_dev_0

    def get_max_dev(self):
        return self.max_dev

    def set_max_dev(self, max_dev):
        self.max_dev = max_dev

    def get_hdr_format_1(self):
        return self.hdr_format_1

    def set_hdr_format_1(self, hdr_format_1):
        self.hdr_format_1 = hdr_format_1

    def get_hdr_format_0(self):
        return self.hdr_format_0

    def set_hdr_format_0(self, hdr_format_0):
        self.hdr_format_0 = hdr_format_0

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset
        self.channels_channel_model_0_1.set_frequency_offset(self.freq_offset)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

    def get_excess_bw_1(self):
        return self.excess_bw_1

    def set_excess_bw_1(self, excess_bw_1):
        self.excess_bw_1 = excess_bw_1

    def get_excess_bw_0(self):
        return self.excess_bw_0

    def set_excess_bw_0(self, excess_bw_0):
        self.excess_bw_0 = excess_bw_0

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw

    def get_damp_fac_1(self):
        return self.damp_fac_1

    def set_damp_fac_1(self, damp_fac_1):
        self.damp_fac_1 = damp_fac_1

    def get_damp_fac_0(self):
        return self.damp_fac_0

    def set_damp_fac_0(self, damp_fac_0):
        self.damp_fac_0 = damp_fac_0

    def get_damp_fac(self):
        return self.damp_fac

    def set_damp_fac(self, damp_fac):
        self.damp_fac = damp_fac
        self.digital_symbol_sync_xx_0_1_0.set_damping_factor(self.damp_fac)
        self.digital_symbol_sync_xx_0_1_0_0.set_damping_factor(self.damp_fac)
        self.digital_symbol_sync_xx_0_1_0_1.set_damping_factor(self.damp_fac)

    def get_access_key_1(self):
        return self.access_key_1

    def set_access_key_1(self, access_key_1):
        self.access_key_1 = access_key_1

    def get_access_key_0(self):
        return self.access_key_0

    def set_access_key_0(self, access_key_0):
        self.access_key_0 = access_key_0




def main(top_block_cls=Multiuser, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
