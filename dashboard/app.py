# NIDS Project - Web Dashboard

import sys
sys.path.insert(0, '/home/lucifer/NIDS-Project')

from flask import Flask, render_template_string
from database.db import get_all_alerts

app = Flask(__name__)

# HTML template for the dashboard
HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>NIDS Dashboard</title>
    <meta http-equiv="refresh" content="10">
    <style>
        body {
            background: #0d1117;
            color: #c9d1d9;
            font-family: monospace;
            padding: 30px;
        }
        h1 { color: #58a6ff; }
        .stats {
            display: flex;
            gap: 20px;
            margin: 20px 0;
        }
        .card {
            background: #161b22;
            border: 1px solid #30363d;
            border-radius: 8px;
            padding: 20px;
            min-width: 150px;
            text-align: center;
        }
        .card h2 { color: #f85149; margin: 0; font-size: 2em; }
        .card p  { margin: 5px 0 0; color: #8b949e; }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th {
            background: #161b22;
            color: #58a6ff;
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #30363d;
        }
        td {
            padding: 10px 12px;
            border-bottom: 1px solid #21262d;
        }
        tr:hover { background: #161b22; }
        .badge-portscan {
            background: #f85149;
            color: white;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.8em;
        }
        .badge-bruteforce {
            background: #d29922;
            color: white;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.8em;
        }
        .refresh { color: #8b949e; font-size: 0.85em; }
    </style>
</head>
<body>
    <h1>🛡️ NIDS - Network Intrusion Detection Dashboard</h1>
    <p class="refresh">Auto-refreshes every 10 seconds</p>

    <div class="stats">
        <div class="card">
            <h2>{{ total }}</h2>
            <p>Total Alerts</p>
        </div>
        <div class="card">
            <h2>{{ port_scans }}</h2>
            <p>Port Scans</p>
        </div>
        <div class="card">
            <h2>{{ brute_force }}</h2>
            <p>Brute Force</p>
        </div>
    </div>

    <table>
        <tr>
            <th>#</th>
            <th>Type</th>
            <th>Source IP</th>
            <th>Details</th>
            <th>Time</th>
        </tr>
        {% for alert in alerts %}
        <tr>
            <td>{{ alert[0] }}</td>
            <td>
                {% if alert[1] == 'PORT_SCAN' %}
                    <span class="badge-portscan">PORT SCAN</span>
                {% else %}
                    <span class="badge-bruteforce">BRUTE FORCE</span>
                {% endif %}
            </td>
            <td>{{ alert[2] }}</td>
            <td>{{ alert[3] }}</td>
            <td>{{ alert[4] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
'''

@app.route('/')
def dashboard():
    alerts = get_all_alerts()
    total = len(alerts)
    port_scans = sum(1 for a in alerts if a[1] == 'PORT_SCAN')
    brute_force = sum(1 for a in alerts if a[1] == 'BRUTE_FORCE')

    return render_template_string(HTML,
        alerts=alerts,
        total=total,
        port_scans=port_scans,
        brute_force=brute_force
    )

if __name__ == '__main__':
    print("Dashboard running at: http://127.0.0.1:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)