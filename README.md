# 🛡️ Network Intrusion Detection System (NIDS)

A real-time Network Intrusion Detection System built with Python that monitors
live network traffic and detects suspicious activity like port scans and SSH brute force attacks.

## Features
- Live packet capture using Scapy
- Port scan detection (rule-based with sliding time window)
- SSH brute force detection
- SQLite database for persistent alert logging
- Flask web dashboard with auto-refresh

## Tech Stack
Python | Scapy | Flask | SQLite

## Project Structure

NIDS-Project/
├── capture/        # Packet sniffer
├── detection/      # Detection rules
├── database/       # SQLite logging
└── dashboard/      # Flask web UI

## How to Run

### Start the sniffer
```bash
sudo python3 capture/sniffer.py
```

### Start the dashboard
```bash
python3 dashboard/app.py
```
Open browser at: http://127.0.0.1:5000