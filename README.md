# Krayt Scout

**Krayt Scout** is a lightweight, Python-powered cyber recon tool built by [Krayt Consulting](https://krayt.pw) for small businesses and professionals. It performs essential external security checks—quickly and clearly.

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/)
[![Krayt Consulting](https://img.shields.io/badge/built%20by-Krayt%20Consulting-black.svg)](https://krayt.pw)

---

## Features

- **DNS Recon**: A, MX, TXT, NS records + zone transfer checks  
- **Port Scanning**: Common port scan with Nmap or fallback socket method
- **TLS Inspection**: Certificate validity, cipher suite, and protocol detection
- **Modular CLI**: Choose what to scan (`--dns`, `--ports`, `--tls`, or `--all`)
- **Clean Output**: Formatted reporting powered by [`rich`](https://github.com/Textualize/rich)

---

## Requirements

- Python 3.12 or higher
- Optional: `nmap` installed for enhanced port scanning

---

## Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/Krayt-Consulting/krayt-scout.git
cd krayt-scout

# Install in development mode
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```


---

## Quick Start

```bash
# Run a full scan on a target
krayt-scout scanme.nmap.org --all

# Or if installed in development mode
python -m krayt_scout.main scanme.nmap.org --all
```

---

## Usage

```bash
krayt-scout <target> [options]
```

### Command-Line Options

| Flag        | Description                                      |
|-------------|--------------------------------------------------|
| `--dns`     | Run DNS record + zone transfer checks            |
| `--ports`   | Scan top TCP ports (requires nmap or uses fallback) |
| `--tls`     | Fetch TLS certificate and protocol configuration |
| `--all`     | Run all scans                                    |

### Examples

```bash
# DNS reconnaissance only
krayt-scout example.com --dns

# Port scan only
krayt-scout example.com --ports

# TLS certificate check
krayt-scout example.com --tls

# Complete assessment
krayt-scout example.com --all
```

---

## Development

Krayt Scout uses modern Python tooling:

- **Type Checking**: `basedpyright` for strict type safety
- **Linting**: `ruff` for code quality
- **Testing**: `pytest` (tests coming soon)

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run type checking
basedpyright krayt_scout/

# Run linter
ruff check krayt_scout/
```

---

## Why Krayt Scout?

- Designed for **security audits**, **lightweight recon**, and **risk assessments**
- Built by professionals for **SMBs, IT teams, and security consultants**
- Easy to run, easy to interpret—no heavy setup or enterprise complexity
- Fully typed Python codebase for reliability and maintainability

---

## Legal Notice

**This software is intended for authorized security testing only.** Do not use Krayt Scout without explicit permission from the target system's owner. Unauthorized port scanning or network reconnaissance may violate laws in your jurisdiction.

---

## About Krayt Consulting

[Krayt Consulting](https://krayt.pw) provides cybersecurity services for small businesses, startups, and local firms. We help you secure what matters—without enterprise bloat.

**Contact**: ops@krayt.pw

---

## License

MIT License - see [LICENSE](LICENSE) for details.
