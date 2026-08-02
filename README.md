# Nmap Scanner - By Marco3BH

Simple and functional Nmap automation script written in Python. Perfect for penetration testing and network reconnaissance.

## Features
- Quick TCP scan (top 1000 ports)
- Full TCP scan (all ports)
- UDP scan (top 100 ports)
- Aggressive scan (OS detection + version + scripts)
- Automatic folder creation for results
- Root privilege check
- Interactive menu

## Installation

git clone https://github.com/marco3bh/nmap_scanner
cd nmap_scanner
chmod +x nmap_scanner.py

## Usage

sudo python3 nmap_scanner.py *ip to scan

example: sudo python3 nmap_scanner.py 192.000.000.000
