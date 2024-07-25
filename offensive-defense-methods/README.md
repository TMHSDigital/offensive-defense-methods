# Offensive Security Techniques

This repository provides examples of offensive security techniques, including ethical hacking (penetration testing), digital counter-intelligence, and the use of AI and machine learning for anomaly detection and automated responses.

## Table of Contents
1. [Ethical Hacking (Penetration Testing)](#ethical-hacking-penetration-testing)
2. [Digital Counter-Intelligence](#digital-counter-intelligence)
3. [Use of AI and Machine Learning](#use-of-ai-and-machine-learning)
4. [File and Directory Structure](#file-and-directory-structure)

## Ethical Hacking (Penetration Testing)

### Description
Penetration testing involves simulating attacks on a system to find vulnerabilities. This section demonstrates how to use Nmap for network scanning and a Python script for port scanning.

### Nmap Command for Network Scanning
```bash
# Basic Nmap scan to discover open ports
nmap -sS -p 1-65535 192.168.1.1
```

### Python Script for Port Scanning
```python
import nmap

# Initialize the Nmap PortScanner
nm = nmap.PortScanner()

# Scan the target IP address
target = '192.168.1.1'
nm.scan(target, '1-1024')

# Print the scan results
for host in nm.all_hosts():
    print(f'Scanning {host}')
    for proto in nm[host].all_protocols():
        print(f'Protocol: {proto}')
        lport = nm[host][proto].keys()
        for port in sorted(lport):
            print(f'Port: {port}\tState: {nm[host][proto][port]["state"]}')
```

## Digital Counter-Intelligence

### Description
Digital counter-intelligence involves tracking and monitoring attacker activities. This section demonstrates setting up a Cowrie honeypot to log brute force attacks and shell interaction performed by attackers.

### Setting Up Cowrie (Shell Commands)
```bash
# Install prerequisites
sudo apt-get update
sudo apt-get install -y git python3-virtualenv libssl-dev libffi-dev build-essential

# Clone the Cowrie repository
git clone http://github.com/cowrie/cowrie

# Set up the virtual environment
cd cowrie
virtualenv cowrie-env
source cowrie-env/bin/activate

# Install Cowrie dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Start Cowrie
bin/cowrie start
```

## Use of AI and Machine Learning

### Description
AI and ML can be used to detect anomalies and respond to threats in real-time. This section demonstrates how to build an anomaly detection model using scikit-learn and an automated response script to block malicious IPs.

### Anomaly Detection with Machine Learning
```python
import numpy as np
from sklearn.ensemble import IsolationForest

# Generate synthetic data for demonstration
X = np.random.rand(100, 2)
X_outliers = np.random.uniform(low=-1, high=1, size=(20, 2))
X = np.concatenate([X, X_outliers], axis=0)

# Fit the model
clf = IsolationForest(random_state=42, contamination=0.1)
clf.fit(X)

# Predict anomalies
y_pred = clf.predict(X)

# Output the results
for i, pred in enumerate(y_pred):
    if pred == -1:
        print(f"Anomaly detected at index {i}: {X[i]}")
```

### Automated Response: Blocking IPs with Python
```python
import os
import subprocess

# List of malicious IPs detected
malicious_ips = ['192.168.1.100', '10.0.0.5']

# Block each malicious IP using iptables
for ip in malicious_ips:
    command = f'sudo iptables -A INPUT -s {ip} -j DROP'
    subprocess.call(command, shell=True)
    print(f"Blocked IP: {ip}")
```

## File and Directory Structure

```plaintext
.
├── README.md
├── ethical_hacking
│   └── port_scanner.py
├── digital_counter_intelligence
│   └── setup_cowrie.sh
└── ai_ml
    ├── anomaly_detection.py
    └── block_ips.py
```

### ethical_hacking/port_scanner.py
Python script for port scanning using Nmap.

### digital_counter_intelligence/setup_cowrie.sh
Shell script for setting up the Cowrie honeypot.

### ai_ml/anomaly_detection.py
Python script for anomaly detection using machine learning.

### ai_ml/block_ips.py
Python script for blocking malicious IPs using iptables.

## Conclusion

This repository provides a foundational understanding and practical examples of offensive security techniques. Use these tools and scripts responsibly and within the bounds of legality and ethics.
