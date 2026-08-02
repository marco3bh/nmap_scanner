#!/usr/bin/env python3
#Author: Made by Marco3BH

import sys
import subprocess
import os

def check_root():
    if os.geteuid() != 0:
        print("[-] Need root privileges")
        print("[*] Run: sudo python3 myscanner.py <IP>")
        return False
    return True

if len(sys.argv) < 2:
    print("Usage: sudo {} [ip]".format(sys.argv[0]))
    print("ip: IP address of the target")
    sys.exit(1)

ip = sys.argv[1]

if not check_root():
    sys.exit(1)

if not os.path.exists("nmap"):
    os.makedirs("nmap")

print("\n" + "=" * 50)
print("TARGET: {}".format(ip))
print("=" * 50)

print("\nWhat to scan?")
print("1. Quick scan only (top 1000 ports)")
print("2. Quick + Full scan")
print("3. Quick + Full + UDP scan")
print("4. All scans")

choice = input("\nChoice (1-4): ")

scans = {
    "quick": ["nmap", "-sC", "-sV", "-T4", "--top-ports", "1000", ip, "-oA", "nmap/tcp_quick", "-v"],
    "full": ["nmap", "-sC", "-sV", "-p-", "-T4", ip, "-oA", "nmap/tcp_full", "-v"],
    "udp": ["nmap", "-sU", "--top-ports", "100", ip, "-oA", "nmap/udp_quick", "-v"],
    "aggressive": ["nmap", "-A", "-T4", "-p-", ip, "-oA", "nmap/aggressive", "-v"]
}

if choice == "1":
    to_run = ["quick"]
elif choice == "2":
    to_run = ["quick", "full"]
elif choice == "3":
    to_run = ["quick", "full", "udp"]
elif choice == "4":
    to_run = ["quick", "full", "udp", "aggressive"]
else:
    print("[-] Invalid choice")
    sys.exit(1)

for scan_name in to_run:
    print("\n[*] Running {} scan...".format(scan_name))
    subprocess.run(scans[scan_name])
    print("[+] {} scan done!".format(scan_name))

print("\n" + "=" * 50)
print("ALL SCANS COMPLETED!")
print("=" * 50)
print("Results saved in nmap/ folder")
print("View: cat nmap/*.nmap")