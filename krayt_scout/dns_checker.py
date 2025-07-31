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
# Krayt Scout - DNS Scanner Module
# Built by Krayt Consulting (https://krayt.pw)
# ─────────────────────────────────────────────────────────────────────────────

import dns.resolver
import dns.query
import dns.zone
import dns.exception
import socket


def get_dns_records(domain):
    record_types = ["A", "MX", "TXT", "NS"]
    results = {}
    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            results[record_type] = [r.to_text() for r in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout):
            results[record_type] = []
    return results


def check_zone_transfer(domain):
    try:
        ns_records = dns.resolver.resolve(domain, "NS")
        vulnerable_servers = []

        for ns in ns_records:
            ns_name = str(ns).rstrip(".")
            try:
                ns_ip = socket.gethostbyname(ns_name)  # Resolve NS to IP
                zone = dns.zone.from_xfr(dns.query.xfr(ns_ip, domain, timeout=5))
                if zone:
                    vulnerable_servers.append(ns_name)
            except (dns.exception.DNSException, socket.error, Exception):
                continue  # Skip on failure
        return vulnerable_servers
    except dns.exception.DNSException:
        return []
