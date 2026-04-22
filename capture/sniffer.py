# NIDS Project - Packet Sniffer Module

import sys
import os

# Add the NIDS-Project root folder to Python path
sys.path.insert(0, '/home/lucifer/NIDS-Project')

# Initialize database on startup
from database.db import init_db
init_db()

from scapy.all import sniff, IP, TCP, UDP
from detection.rules import detect_port_scan, detect_brute_force

def process_packet(packet):

    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            flags = str(packet[TCP].flags)
            print(f"[TCP] {src_ip}:{src_port} --> {dst_ip}:{dst_port}")
            detect_port_scan(src_ip, dst_port)
            detect_brute_force(src_ip, dst_port, flags)

        elif UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            print(f"[UDP] {src_ip}:{src_port} --> {dst_ip}:{dst_port}")

print("NIDS Started - Monitoring Network Traffic...")
print("Press Ctrl+C to stop")
print("-" * 50)
sniff(prn=process_packet, count=0, store=0)