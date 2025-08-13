# Packet Sniffer Tool

A simple **Packet Sniffer** built using Python and Scapy that captures and analyzes network traffic.  
It displays **Source IP**, **Destination IP**, **Protocol**, and **Packet Summary** in real time.

---

## Features
- Captures live network packets.
- Displays:
  - Source and Destination IP addresses
  - Protocol used
  - Packet Summary
- Handles non-IP packets gracefully.
- Works on **Windows, Linux, and macOS**.
- Runs until manually stopped.

---

## Technologies Used
- **Python 3**
- **Scapy** (for packet capturing)
- **Npcap / libpcap** (for low-level packet access)

---

## Installation

### 1. Install Python packages
```bash
pip install scapy
```
### 2. Install packet capture backend
Windows: Install Npcap (select WinPcap API-compatible mode).

Linux/macOS: Install libpcap:

```bash
sudo apt install libpcap-dev   # Debian/Ubuntu
brew install libpcap           # macOS
```

---

## Usage
Windows:

```bash
python packet_sniffer.py
```
(Run in Administrator Command Prompt)

Linux/macOS:

```bash
sudo python3 packet_sniffer.py
```
---

## Knowledge Gained
- Understanding of network packet structure.

- Practical use of Scapy for packet sniffing.

- Cross-platform compatibility challenges in networking tools.

- Basics of IP protocol and non-IP packet handling.

- The importance of administrative privileges for packet capture.

---

## Ethical Use
This tool is for educational purposes only.
Unauthorized packet sniffing can be illegal and unethical.
Use only on networks you own or have permission to analyze.

---

## Example Output:
```
==================================================
Time: 2025-08-13 23:05:22
Source IP: 192.168.1.10
Destination IP: 93.184.216.34
Protocol: 6
Summary: IP / TCP 192.168.1.10:52345 > example.com:http S
```
