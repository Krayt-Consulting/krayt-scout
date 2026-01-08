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

import socket
import ssl
from typing import TypedDict, cast

# Type alias for X.509 Distinguished Name structure
type DistinguishedName = tuple[tuple[tuple[str, str], ...], ...]


class CertificateInfo(TypedDict):
    subject: str  # Now a formatted string
    issuer: str  # Now a formatted string
    not_before: str | None
    not_after: str | None
    tls_version: str | None
    cipher: tuple[str, str, int] | None


def _format_dn(dn: DistinguishedName) -> str:
    """Format a Distinguished Name tuple into a readable string."""
    if not dn:
        return "Unknown"

    parts = []
    for rdn_sequence in dn:
        for attr_type, attr_value in rdn_sequence:
            parts.append(f"{attr_type}={attr_value}")
    return ", ".join(parts)


def get_certificate_info(host: str, port: int = 443) -> CertificateInfo | None:
    """Fetches and parses TLS certificate info for a given host."""
    context = ssl.create_default_context()

    try:
        with socket.create_connection((host, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()
                tls_version = ssock.version()
                cipher = ssock.cipher()
    except (OSError, ssl.SSLError, socket.timeout) as e:
        print(f"[!] Failed to connect or fetch TLS info: {e}")
        return None

    if not cert:
        print("[!] No certificate received from peer")
        return None

    # Cast the cert dict values to expected types
    subject = cast(DistinguishedName, cert.get("subject", ()))
    issuer = cast(DistinguishedName, cert.get("issuer", ()))
    not_before = cert.get("notBefore")
    not_after = cert.get("notAfter")

    return {
        "subject": _format_dn(subject),
        "issuer": _format_dn(issuer),
        "not_before": not_before if isinstance(not_before, str) else None,
        "not_after": not_after if isinstance(not_after, str) else None,
        "tls_version": tls_version,
        "cipher": cipher,
    }
