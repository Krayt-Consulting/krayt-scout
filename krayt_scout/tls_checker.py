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
# Krayt Scout - TLS Checker Module
# Built by Krayt Consulting (https://krayt.pw)
# ─────────────────────────────────────────────────────────────────────────────

import ssl
import socket
from datetime import datetime
from typing import Optional


def get_certificate_info(host: str, port: int = 443) -> Optional[dict]:
    """Fetches and parses TLS certificate info for a given host."""
    context = ssl.create_default_context()

    try:
        with socket.create_connection((host, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()
                tls_version = ssock.version()
                cipher = ssock.cipher()
    except Exception as e:
        print(f"[!] Failed to connect or fetch TLS info: {e}")
        return None

    return {
        "subject": cert.get("subject", []),
        "issuer": cert.get("issuer", []),
        "not_before": cert.get("notBefore"),
        "not_after": cert.get("notAfter"),
        "tls_version": tls_version,
        "cipher": cipher
    }


def print_tls_summary(info: dict) -> None:
    """Formats and prints a summary of the certificate and TLS info."""
    if not info:
        print("[!] No TLS info available.")
        return

    print("\n🔐 TLS Configuration:")
    print(f"  TLS Version: {info['tls_version']}")
    print(f"  Cipher Suite: {info['cipher'][0]} ({info['cipher'][1]})")

    print("\n📄 Certificate Info:")
    print(f"  Subject: {info['subject']}")
    print(f"  Issuer: {info['issuer']}")
    print(f"  Valid From: {info['not_before']}")
    print(f"  Valid Until: {info['not_after']}")

    try:
        exp_date = datetime.strptime(info["not_after"], "%b %d %H:%M:%S %Y %Z")
        days_left = (exp_date - datetime.utcnow()).days
        if days_left < 0:
            print(f"  🔴 Certificate has EXPIRED! ({-days_left} days ago)")
        elif days_left < 30:
            print(f"  🟠 Certificate expires soon: {days_left} days remaining")
        else:
            print(f"  🟢 Certificate is valid: {days_left} days remaining")
    except Exception:
        print("  ⚠️ Could not parse expiration date")

