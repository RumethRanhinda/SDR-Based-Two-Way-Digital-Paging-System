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
 
### Recommended Environment
It is highly recommended to run this system on **Ubuntu**. GNU Radio and SDR hardware drivers tend to be significantly more stable, performant, and easier to configure in a native Linux environment compared to Windows.

## Flowgraph Descriptions (.grc Files)
The repository is structured around separate flowgraphs for testing different MAC protocols and nodes. 

- **`[arq_tx_name].grc`**: The transmitter flowgraph for the Stop-and-Wait ARQ protocol. It handles queueing messages, appending sequence numbers, and pausing channel access until an ACK is received or a timeout occurs.
- **`[arq_rx_name].grc`**: The receiver flowgraph for ARQ. It demodulates the signal, verifies sequence numbers, filters out duplicate packets, and triggers the ACK response.
- **`[aloha_tx_name].grc`**: The transmitter flowgraph for the Pure ALOHA implementation, demonstrating uncoordinated channel access without acknowledgment requirements.
- **`[aloha_rx_name].grc`**: The receiver flowgraph for the Pure ALOHA system.

## Setup & Configuration

### 1. Installing bladeRF Drivers (Ubuntu)
Open your terminal and execute the following commands to install the Nuand PPA, the necessary drivers, and the `gr-osmosdr` package required for GNU Radio integration:

```bash
sudo add-apt-repository ppa:nuand/bladerf
sudo apt-get update
# Install bladeRF tools and specific FPGA packages for xA4/xA9
sudo apt-get install bladerf libbladerf-dev bladerf-fpga-hostedxa4 bladerf-fpga-hostedxa9
# Install osmoSDR to link the bladeRF with GNU Radio
sudo apt-get install gr-osmosdr
```

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

### 2. Firmware & FPGA Bitstream
1. To ensure compatibility with modern drivers, the bladeRF hardware must be running firmware version 2.6.0.
2. Flash the updated firmware to the bladeRF. Load the corresponding FPGA bitstream for your specific model (`hostedxA4.rbf` or `hostedxA9.rbf`) using the `bladeRF-cli` before executing the flowgraphs.

### 3. GNU Radio Configuration
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
