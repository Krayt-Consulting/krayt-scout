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
    21,
    22,
    23,
    25,
    53,
    80,
    110,
    135,
    139,
    143,
    443,
    445,
    993,
    995,
    1433,
    1521,
    1723,
    3306,
    3389,
    5900,
    8080,
    8443,
    8888,
]


def is_host_up(host: str, port: int = 80, timeout: float = 2) -> bool:
    """Check if a host is reachable by attempting a TCP connection."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except TimeoutError:
        return False


def scan_with_nmap(host: str, ports: list[int] | None = None) -> dict[int, str]:
    """Scan ports using Nmap for service detection and state information."""
    scanner = nmap.PortScanner()
    port_range = ",".join(map(str, ports)) if ports else "1-1000"
    try:
        scanner.scan(hosts=host, arguments=f"-p {port_range} -T4")

        # Handle IP-keyed result fallback
        target = list(scanner.all_hosts())[0] if scanner.all_hosts() else None
        if not target or "tcp" not in scanner[target]:
            return {}

        return scanner[target]["tcp"]
    except (nmap.PortScannerError, KeyError, IndexError) as e:
        print(f"[!] Nmap scan failed: {e}")
        return {}


def fallback_scan(host: str, ports: list[int], timeout: float = 1) -> dict[int, str]:
    """Perform basic TCP port scanning using raw sockets as fallback."""
    results = {}
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(timeout)
                result = sock.connect_ex((host, port))
                results[port] = "open" if result == 0 else "closed"
        except TimeoutError:
            results[port] = "error"
    return results


def run_port_scan(
    host: str, ports: list[int] = TOP_PORTS, use_nmap: bool = True
) -> dict[int, str]:
    """Execute port scan on target host using nmap or fallback method."""
    if not is_host_up(host):
        print(f"[!] Host {host} appears to be down.")
        return {}

    print(f"[*] Scanning {host} on {len(ports)} ports...")
    if use_nmap:
        results = scan_with_nmap(host, ports)
        return {p: d["state"] for p, d in results.items()}
    else:
        return fallback_scan(host, ports)
