# NIDS Project - Basic Alert Test

print("NIDS Project Started Successfully!")

# Store a suspicious IP address
ip_address = "192.168.1.1"
print("Suspicious IP:", ip_address)

# List of ports scanned by the IP
ports = [22, 80, 443, 8080, 3306]
print("Total ports scanned:", len(ports))

# Trigger alert if more than 4 ports are scanned from same IP
if len(ports) > 4:
    print("ALERT! Possible Port Scan Detected!")
else:
    print("Traffic looks normal.")