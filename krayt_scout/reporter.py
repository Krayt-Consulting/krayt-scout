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
# Krayt Scout - Output Reporter
# Built by Krayt Consulting (https://krayt.pw)
# ─────────────────────────────────────────────────────────────────────────────

from rich.console import Console
from rich.table import Table
from collections import Counter
from rich.panel import Panel
from rich.text import Text
from datetime import datetime

console = Console()

def pretty_print_tls(info: dict) -> None:
    """Prints TLS configuration and cert validity with styling."""
    if not info:
        console.print("[bold red][!] No TLS info available.[/bold red]")
        return

    # TLS Section
    tls_text = Text()
    tls_text.append("TLS Version: ", style="bold")
    tls_text.append(f"{info['tls_version']}\n", style="green")

    tls_text.append("Cipher Suite: ", style="bold")
    tls_text.append(f"{info['cipher'][0]} ", style="cyan")
    tls_text.append(f"({info['cipher'][1]})\n", style="dim")

    console.print(Panel(tls_text, title="🔐 TLS Configuration", expand=False))

    # Certificate Section
    cert_text = Text()
    cert_text.append("Subject: ", style="bold")
    cert_text.append(f"{info['subject']}\n", style="cyan")

    cert_text.append("Issuer: ", style="bold")
    cert_text.append(f"{info['issuer']}\n", style="cyan")

    cert_text.append("Valid From: ", style="bold")
    cert_text.append(f"{info['not_before']}\n", style="green")

    cert_text.append("Valid Until: ", style="bold")
    cert_text.append(f"{info['not_after']}\n", style="green")

    # Expiry Warning
    try:
        exp_date = datetime.strptime(info["not_after"], "%b %d %H:%M:%S %Y %Z")
        days_left = (exp_date - datetime.utcnow()).days
        if days_left < 0:
            cert_text.append(f"🔴 Certificate has EXPIRED! ({-days_left} days ago)\n", style="bold red")
        elif days_left < 30:
            cert_text.append(f"🟠 Certificate expires soon: {days_left} days left\n", style="yellow")
        else:
            cert_text.append(f"🟢 Certificate is valid: {days_left} days remaining\n", style="green")
    except Exception:
        cert_text.append("⚠️ Could not parse expiration date\n", style="red")

    console.print(Panel(cert_text, title="📄 Certificate Info", expand=False))

def pretty_print_ports(port_results):
    summary = Counter(port_results.values())

    table = Table(title="Port Scan Results", show_lines=True)
    table.add_column("Port", style="bold")
    table.add_column("State", style="cyan")

    for port in sorted(port_results):
        state = port_results[port]
        style = {
            "open": "green",
            "filtered": "yellow",
            "closed": "dim"
        }.get(state, "white")

        table.add_row(str(port), f"[{style}]{state}[/{style}]")

    console.print(table)

    console.print(f"\n[bold green]Open:[/] {summary['open']}  "
                  f"[bold yellow]Filtered:[/] {summary['filtered']}  "
                  f"[bold dim]Closed:[/] {summary['closed']}")

