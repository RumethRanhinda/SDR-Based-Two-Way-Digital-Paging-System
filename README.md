# SDR-Based Two-Way Digital Paging System

## Overview
This repository contains the implementation of a two-way digital communication system using Software-Defined Radio (SDR). Built with GNU Radio and Nuand bladeRF hardware, the project implements reliable digital packet transmission protocols, including Stop-and-Wait ARQ and Pure ALOHA. The system is designed for two-computer communication simulations, featuring custom Python blocks for robust message queuing and half-duplex channel management.

## System Architecture
The system architecture separates the transmission and reception paths to allow for independent node operation across two physical computers.
- **Transmitter (Tx) Node:** Handles message queuing, sequence numbering, and modulation.
- **Receiver (Rx) Node:** Demodulates incoming signals, verifies sequence numbers, and triggers acknowledgment signals (ACKs). 

## Hardware & Software Requirements
- **Hardware:** Nuand bladeRF (xA4 and xA9 models)
- **Software:** 
  - GNU Radio
  - Python 3.x
  - bladeRF drivers and utilities

## Features & Protocols
- **Stop-and-Wait ARQ:** Ensures reliable packet delivery by requiring an acknowledgment before sending the next packet. Incorporates a timeout and retransmission mechanism.
- **Pure ALOHA:** Implements basic channel access logic for uncoordinated transmission.
- **Half-Duplex Channel Management:** Custom Python blocks utilize pause logic to prevent collisions and manage the switch between Tx and Rx modes.
- **Manual Gain Control:** Configured to prevent signal clipping and maintain optimal SNR during transmission.

## Setup & Configuration

### 1. Firmware & FPGA Bitstream
To ensure compatibility with modern drivers, the bladeRF hardware must be running firmware version **2.6.0**.
1. Flash the updated firmware to the bladeRF.
2. Load the corresponding FPGA bitstream for your specific model (`hostedxA4.rbf` or `hostedxA9.rbf`) before executing the flowgraphs.

### 2. GNU Radio Configuration
1. Clone this repository.
2. Open the `.grc` flowgraph files in GNU Radio Companion.
3. Verify that the sample rates match exactly between the Tx and Rx blocks.
4. Adjust the manual gain settings depending on the physical distance between the two SDR nodes to prevent signal loss.

## Usage
1. Connect the bladeRF hardware to both Node A and Node B.
2. Load the correct FPGA bitstreams on both machines.
3. Run the receiver flowgraph on Node B.
4. Run the transmitter flowgraph on Node A.
5. Monitor the console output for sequence numbers, ACKs, and retransmission events.
