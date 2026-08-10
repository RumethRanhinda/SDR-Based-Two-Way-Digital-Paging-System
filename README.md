# SDR-Based Two-Way Digital Paging System

## Overview
This repository contains the implementation of a robust two-way digital communication system using Software-Defined Radio (SDR). Built with GNU Radio and Nuand bladeRF hardware, the project features a complete custom protocol stack for reliable text messaging between nodes. 

Designed for two-computer communication, the system integrates a graphical Pager GUI, utilizes custom Python blocks for robust message queuing, and implements intelligent half-duplex channel management to prevent collisions over the air.

---

## System Architecture
The system architecture separates the transmission, reception, and user interface paths to allow for independent, asynchronous node operation.

* **EchoWave Pager GUI:** A user-friendly graphical interface that handles message input, chat history, and visual delivery status (Pending/ACKed/Failed).
* **Transmitter (Tx) Path:** Manages message queuing, fragmentation, sequence numbering, PDU construction (including dummy byte prepending for pipeline flushing), and signal modulation.
* **Receiver (Rx) Path:** Demodulates incoming RF signals, verifies sequence numbers, drops duplicate packets, pushes data to the GUI, and triggers Priority-0 acknowledgment signals (ACKs).

---

## Features & Protocols
* **Stop-and-Wait ARQ:** Ensures reliable packet delivery. The sender pauses after transmission and waits for an ACK. Includes dynamic timeouts and automatic retransmission limits.
* **Pure ALOHA:** Implements basic channel access logic for uncoordinated multi-node transmission.
* **Half-Duplex Channel Management:** Custom MAC-layer logic senses the channel. If a node detects incoming data while trying to transmit, it pauses its ARQ loop, yields the channel, and resumes once clear.
* **Manual Gain Control:** Strictly configured to prevent signal clipping, avoid SDR "deafness," and maintain optimal SNR during burst transmissions.

---

## Flowgraph Descriptions
The repository is structured around separate `.grc` flowgraphs for testing different MAC protocols and nodes. 

| Flowgraph File | Description |
| :--- | :--- |
| `[arq_tx_name].grc` | Tx flowgraph for Stop-and-Wait ARQ. Queues messages, handles sequencing, and waits for ACKs. |
| `[arq_rx_name].grc` | Rx flowgraph for ARQ. Demodulates, filters duplicates, and automatically transmits ACKs. |
| `[aloha_tx_name].grc` | Tx flowgraph for Pure ALOHA, demonstrating uncoordinated channel access without ACKs. |
| `[aloha_rx_name].grc` | Rx flowgraph for the Pure ALOHA system. |

---

## Hardware & Software Requirements

### Hardware
* Nuand bladeRF (xA4 or xA9 models highly recommended)
* USB 3.0 connection

### Software Stack
* GNU Radio (v3.10+)
* Python 3.x (with PyQt5 for the GUI)
* SoapySDR and `libbladeRF` drivers

> **Recommended Environment:** It is highly recommended to run this system on **Ubuntu**. GNU Radio and SDR hardware drivers are significantly more stable, performant, and easier to configure in a native Linux environment compared to Windows.

---

## Setup & Configuration

### 1. Installing bladeRF Drivers (Ubuntu)
Open your terminal and execute the following commands to install the Nuand PPA, the necessary drivers, and the GNU Radio integration packages:

```bash
sudo add-apt-repository ppa:nuand/bladerf
sudo apt-get update
# Install bladeRF tools and specific FPGA packages for xA4/xA9
sudo apt-get install bladerf libbladerf-dev bladerf-fpga-hostedxa4 bladerf-fpga-hostedxa9
# Install osmoSDR/Soapy to link the bladeRF with GNU Radio
sudo apt-get install gr-osmosdr
```

---

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

### 2. Firmware & FPGA Bitstream
To ensure compatibility with modern drivers, the bladeRF hardware must be running firmware version **2.6.0**.
1. Flash the updated firmware to the bladeRF.
2. Load the corresponding FPGA bitstream for your specific model (`hostedxA4.rbf` or `hostedxA9.rbf`) before executing the flowgraphs.

### 3. Firmware & FPGA Bitstream
1. To ensure compatibility with modern drivers, the bladeRF hardware must be running firmware version 2.6.0.
2. Flash the updated firmware to the bladeRF. Load the corresponding FPGA bitstream for your specific model (`hostedxA4.rbf` or `hostedxA9.rbf`) using the `bladeRF-cli` before executing the flowgraphs.

### 4. GNU Radio Configuration
1. Clone this repository.
2. Open the `.grc` flowgraph files in GNU Radio Companion.
3. Verify that the sample rates match exactly between the Tx and Rx blocks.
4. Adjust the manual gain settings depending on the physical distance between the two SDR nodes to prevent signal loss.

---


## Usage
1. Connect the bladeRF hardware to both Node A and Node B.
2. Load the correct FPGA bitstreams on both machines.
3. Run the receiver flowgraph on Node B.
4. Run the transmitter flowgraph on Node A.
5. Monitor the console output for sequence numbers, ACKs, and retransmission events.

## Authors & Acknowledgments

![Design_team](Images/Design_team.jpg)

* **Team EchoWave** (Department of Electronic & Telecommunication Engineering, University of Moratuwa): *(From Left to Right)*  
  * Samarasinghe S.M.R.R. - 230566U
  * Eranga W.A.O. - 230175U
  * Gamage S.K. - 230195F
  * Tharushika G.K.E. - 230636K
