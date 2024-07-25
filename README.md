# Offensive Security Techniques

![GitHub stars](https://img.shields.io/github/stars/TMHSDigital/offensive-defense-methods?style=social)
![GitHub forks](https://img.shields.io/github/forks/TMHSDigital/offensive-defense-methods?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/TMHSDigital/offensive-defense-methods?style=social)
![GitHub issues](https://img.shields.io/github/issues/TMHSDigital/offensive-defense-methods)
![GitHub pull requests](https://img.shields.io/github/issues-pr/TMHSDigital/offensive-defense-methods)
![GitHub](https://img.shields.io/github/license/TMHSDigital/offensive-defense-methods)

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-Bash-blue?logo=gnu-bash&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--learn-orange?logo=scikit-learn&logoColor=white)

---

This repository provides examples of offensive security techniques, including ethical hacking (penetration testing), digital counter-intelligence, and the use of AI and machine learning for anomaly detection and automated responses.

## Table of Contents
1. [Ethical Hacking (Penetration Testing)](#ethical-hacking-penetration-testing)
2. [Digital Counter-Intelligence](#digital-counter-intelligence)
3. [Use of AI and Machine Learning](#use-of-ai-and-machine-learning)
4. [File and Directory Structure](#file-and-directory-structure)
5. [Disclaimer](#disclaimer)
6. [Contributing](#contributing)
7. [Resources](#resources)
8. [License](#license)

---

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

---

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

---

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

---

### ethical_hacking/port_scanner.py
Python script for port scanning using Nmap.

### digital_counter_intelligence/setup_cowrie.sh
Shell script for setting up the Cowrie honeypot.

### ai_ml/anomaly_detection.py
Python script for anomaly detection using machine learning.

### ai_ml/block_ips.py
Python script for blocking malicious IPs using iptables.

---

## Disclaimer

**IMPORTANT:** The techniques and tools provided in this repository are intended solely for educational purposes. Unauthorized use of these techniques and tools for malicious or unethical purposes is strictly prohibited. The authors of this repository are not responsible for any misuse or damage caused by the use of these techniques and tools.

---

## Contributing
Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more information.

---

## Resources
- [Books and Articles](resources/books.md)
- [Online Courses](resources/courses.md)
- [Tools and Utilities](resources/tools.md)

---

## License
This project is licensed under the "Do No Harm" License - see the [LICENSE](LICENSE) file for details.
```

### `LICENSE` File

``````
DO NO HARM LICENSE

Copyright (c) 2024 [TM Hospitality Strategies]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

The software is provided "as is", without warranty of any kind, express or
implied, including but not limited to the warranties of merchantability,
fitness for a particular purpose and noninfringement. In no event shall the
authors or copyright holders be liable for any claim, damages or other
liability, whether in an action of contract, tort or otherwise, arising from,
out of or in connection with the software or the use or other dealings in the
software.

## "Do No Harm" Clause

The software may not be used by any person or entity for systems, activities,
or projects that result in:
  1. physical injury or loss of life,
  2. environmental damage or destruction,
  3. unjust discrimination or oppression,
  4. violation of privacy or personal data,
  5. support of unlawful activities.

By using the software, you agree to be bound by this clause and use the software
only for lawful and ethical purposes.
```

### `CONTRIBUTING.md` File

```markdown
# Contributing to Offensive Security Techniques

Thank you for considering contributing to this repository! We welcome contributions in the form of bug reports, feature requests, code improvements, and documentation enhancements.

## How to Contribute

1. **Fork the Repository**
   - Click on the "Fork" button at the top right of this page to create a copy of this repository in your GitHub account.

2. **Clone the Repository**
   - Clone your forked repository to your local machine.
   ```bash
   git clone https://github.com/your-username/offensive-defense-methods.git
   cd offensive-defense-methods
   ```

3. **Create a Branch**
   - Create a new branch for your changes.
   ```bash
   git checkout -b my-feature-branch
   ```

4. **Make Changes**
   - Make your changes to the code, documentation, or other files.

5. **Commit Changes**
   - Commit your changes with a descriptive message

.
   ```bash
   git add .
   git commit -m "Description of the changes"
   ```

6. **Push Changes**
   - Push your changes to your forked repository.
   ```bash
   git push origin my-feature-branch
   ```

7. **Create a Pull Request**
   - Go to the original repository on GitHub and create a pull request from your forked repository.

## Code Style

- Follow PEP 8 for Python code.
- Use descriptive variable names and comments.
- Ensure code is well-documented.

## Reporting Issues

- Check existing issues to avoid duplicates.
- Provide a clear and descriptive title.
- Include steps to reproduce the issue.

## Code of Conduct

Please adhere to the [Code of Conduct](CODE_OF_CONDUCT.md) in all your interactions with the project.

Thank you for your contributions!
```