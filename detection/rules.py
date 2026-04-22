# NIDS Project - Detection Rules Module

from collections import defaultdict
import time
import sys
import os

sys.path.insert(0, '/home/lucifer/NIDS-Project')
from database.db import save_alert

ip_port_tracker = defaultdict(set)
ip_first_seen = {}
alerted_ips = set()

PORT_SCAN_THRESHOLD = 4
TIME_WINDOW = 30

def detect_port_scan(src_ip, dst_port):
    current_time = time.time()

    if src_ip in alerted_ips:
        return

    if src_ip not in ip_first_seen:
        ip_first_seen[src_ip] = current_time

    ip_port_tracker[src_ip].add(dst_port)
    time_elapsed = current_time - ip_first_seen[src_ip]
    unique_ports = len(ip_port_tracker[src_ip])

    if time_elapsed <= TIME_WINDOW:
        if unique_ports > PORT_SCAN_THRESHOLD:
            details = f"Ports Hit: {unique_ports} | Ports: {sorted(ip_port_tracker[src_ip])} | Time: {round(time_elapsed,2)}s"

            print(f"\n{'='*50}")
            print(f"[ALERT] Port Scan Detected!")
            print(f"        Source IP  : {src_ip}")
            print(f"        Ports Hit  : {unique_ports}")
            print(f"        Time       : {round(time_elapsed, 2)} seconds")
            print(f"        Ports List : {sorted(ip_port_tracker[src_ip])}")
            print(f"{'='*50}\n")

            # Save alert to database
            save_alert("PORT_SCAN", src_ip, details)

            alerted_ips.add(src_ip)
    else:
        ip_port_tracker[src_ip] = set()
        ip_first_seen[src_ip] = current_time


ssh_tracker = defaultdict(int)
SSH_THRESHOLD = 5

def detect_brute_force(src_ip, dst_port, flags):
    if dst_port == 22 and flags == 'S':
        ssh_tracker[src_ip] += 1

        if ssh_tracker[src_ip] > SSH_THRESHOLD:
            details = f"SSH attempts: {ssh_tracker[src_ip]}"

            print(f"\n{'='*50}")
            print(f"[ALERT] SSH Brute Force Detected!")
            print(f"        Source IP : {src_ip}")
            print(f"        Attempts  : {ssh_tracker[src_ip]}")
            print(f"{'='*50}\n")

            # Save alert to database
            save_alert("BRUTE_FORCE", src_ip, details)

            ssh_tracker[src_ip] = 0