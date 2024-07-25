import os
import subprocess

# List of malicious IPs detected
malicious_ips = ['192.168.1.100', '10.0.0.5']

# Block each malicious IP using iptables
for ip in malicious_ips:
    command = f'sudo iptables -A INPUT -s {ip} -j DROP'
    subprocess.call(command, shell=True)
    print(f"Blocked IP: {ip}")
