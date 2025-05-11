# ─────────────────────────────────────────────────────────────────────────────
# Krayt Scout - Lightweight Cyber Recon Tool
# Built by Krayt Consulting (https://krayt.pw)
#
# This software is intended for authorized use only. Do not use without
# explicit permission from the target system's owner.
#
# Contact: admin@krayt.pw | GitHub: https://github.com/Krayt-Consulting/krayt-scout
# License: MIT
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# Krayt Scout - Port Scanner Module
# Built by Krayt Consulting (https://krayt.pw)
# ─────────────────────────────────────────────────────────────────────────────

import socket
import nmap

# Common TCP ports
TOP_PORTS = [
    21, 22, 23, 25, 53, 80, 110, 135, 139, 143,
    443, 445, 993, 995, 1433, 1521, 1723, 3306, 3389, 5900,
    8080, 8443, 8888
]

def is_host_up(host, port=80, timeout=2):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except:
        return False

def scan_with_nmap(host, ports=None):
    scanner = nmap.PortScanner()
    port_range = ','.join(map(str, ports)) if ports else '1-1000'
    try:
        scanner.scan(hosts=host, arguments=f'-p {port_range} -T4')

        # Handle IP-keyed result fallback
        target = list(scanner.all_hosts())[0] if scanner.all_hosts() else None
        if not target or 'tcp' not in scanner[target]:
            return {}

        return scanner[target]['tcp']
    except Exception as e:
        print(f"[!] Nmap scan failed: {e}")
        return {}

def fallback_scan(host, ports, timeout=1):
    results = {}
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            results[port] = 'open' if result == 0 else 'closed'
            sock.close()
        except Exception:
            results[port] = 'error'
    return results

def run_port_scan(host, ports=TOP_PORTS, use_nmap=True):
    if not is_host_up(host):
        print(f"[!] Host {host} appears to be down.")
        return {}

    print(f"[*] Scanning {host} on {len(ports)} ports...")
    if use_nmap:
        results = scan_with_nmap(host, ports)
        return {p: d['state'] for p, d in results.items()}
    else:
        return fallback_scan(host, ports)


