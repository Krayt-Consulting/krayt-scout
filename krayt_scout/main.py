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

import argparse
from krayt_scout import dns_checker, port_scanner, reporter, tls_checker


def run_tls_check(target: str) -> None:
    """Run TLS configuration and certificate analysis."""
    tls_info = tls_checker.get_certificate_info(target)
    reporter.pretty_print_tls(tls_info)


def run_dns_scan(target: str) -> None:
    """Fetch DNS records and test for zone transfer."""
    print(f"\n🔍 Running DNS checks for {target}...")
    dns_records = dns_checker.get_dns_records(target)
    for rtype, records in dns_records.items():
        print(f"{rtype} Records: {records or 'None'}")

    print("\n🛡️ Checking for zone transfer vulnerabilities...")
    zones = dns_checker.check_zone_transfer(target)
    if zones:
        print(f"[!] Zone transfer ALLOWED on: {zones}")
    else:
        print("[+] No zone transfer vulnerabilities found.")


def run_port_scan(target: str) -> None:
    """Run port scan and display results."""
    print(f"\n🔌 Scanning ports on {target}...")
    results = port_scanner.run_port_scan(target)
    reporter.pretty_print_ports(results)


def run_all_scans(target: str) -> None:
    """Run all scan types."""
    run_dns_scan(target)
    run_port_scan(target)
    run_tls_check(target)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        prog="krayt-scout", description="Krayt Scout - Lightweight Cyber Recon Tool"
    )
    parser.add_argument("target", help="Target domain or IP")
    parser.add_argument(
        "--dns", action="store_true", help="Run DNS record + zone transfer checks"
    )
    parser.add_argument(
        "--ports", action="store_true", help="Run port scan on common ports"
    )
    parser.add_argument(
        "--tls", action="store_true", help="Run TLS certificate and config check"
    )
    parser.add_argument("--all", action="store_true", help="Run all scans")
    return parser.parse_args()


def main() -> None:
    """Main CLI entrypoint."""
    args = parse_args()

    if args.all:
        run_all_scans(args.target)
    else:
        if not args.dns and not args.ports:
            print("[!] No scan type selected. Use --dns, --ports, or --all.")
            return

        if args.dns:
            run_dns_scan(args.target)

        if args.ports:
            run_port_scan(args.target)

        if args.tls:
            run_tls_check(args.target)


if __name__ == "__main__":
    main()
