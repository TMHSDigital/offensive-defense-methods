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
