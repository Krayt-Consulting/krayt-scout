"""
Krayt Scout - Lightweight Cyber Recon Tool
Built by Krayt Consulting (https://krayt.pw)

A Python-powered cyber reconnaissance tool for DNS, port scanning, and TLS inspection.
"""

__version__ = "0.1.1"
__author__ = "Krayt Consulting"
__email__ = "admin@krayt.pw"

# public API
__all__ = [
    "dns_checker",
    "port_scanner",
    "tls_checker",
    "reporter",
]

from krayt_scout import dns_checker, port_scanner, reporter, tls_checker
