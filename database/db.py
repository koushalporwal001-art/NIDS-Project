# NIDS Project - Database Module
# Handles storing and retrieving alerts using SQLite

import sqlite3
import os

# Database file will be created in the database folder
DB_PATH = os.path.join(os.path.dirname(__file__), 'alerts.db')

def init_db():
    # Create database and alerts table if it doesn't exist
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alerts (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            alert_type  TEXT NOT NULL,
            src_ip      TEXT NOT NULL,
            details     TEXT,
            timestamp   DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()
    print("[DB] Database initialized successfully")

def save_alert(alert_type, src_ip, details):
    # Save a new alert to the database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO alerts (alert_type, src_ip, details)
        VALUES (?, ?, ?)
    ''', (alert_type, src_ip, details))

    conn.commit()
    conn.close()

def get_all_alerts():
    # Retrieve all alerts from database (newest first)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM alerts ORDER BY timestamp DESC')
    alerts = cursor.fetchall()

    conn.close()
    return alerts