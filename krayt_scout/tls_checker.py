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
        "cipher": cipher,
    }
