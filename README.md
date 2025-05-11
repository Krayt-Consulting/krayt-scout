# 🐍 Krayt Scout

**Krayt Scout** is a lightweight, Python-powered cyber recon tool built by [Krayt Consulting](https://krayt.pw) for small businesses and professionals. It performs essential external security checks—quickly and clearly.

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Krayt Consulting](https://img.shields.io/badge/built%20by-Krayt%20Consulting-black.svg)](https://krayt.pw)

---

## ✨ Features

- 🔍 **DNS Recon**: A, MX, TXT, NS records + zone transfer checks  
- 🔌 **Port Scanning**: Common port scan with Nmap or fallback
- 🔐 **TLS Inspection**: Cert validity, cipher, and protocol detection
- 🕵️‍♀️ **Modular CLI**: Choose what to scan (`--dns`, `--ports`, `--tls`, or `--all`)
- 🎨 **Pretty Output**: Clean formatting powered by [`rich`](https://github.com/Textualize/rich)

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/Krayt-Consulting/krayt-scout.git
cd krayt-scout

# Create a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run a full scan
python -m krayt_scout.main scanme.nmap.org --all

