# Changelog

All notable changes to this project will be documented in this file.

## [0.1.1] - 2025-01-07

### Changed
- Dropped Python 3.10/3.11 support, now requires Python 3.12+
- Updated to use `type` statement (Python 3.12 feature)
- Modernized exception handling with specific exception types
- Replaced deprecated `datetime.utcnow()` with `datetime.now(timezone.utc)`

### Added
- Comprehensive type hints across all modules
- `py.typed` marker file for type checker support
- `pyproject.toml` for modern Python packaging
- Docstrings for all public functions

### Fixed
- Improved TLS certificate info formatting
- Better error handling in DNS, port scanning, and TLS modules
- Removed bare `except` statements

### Removed
- Emoji characters from output (replaced with text indicators)

## [0.1.0] - Initial Release

### Added
- DNS record checking and zone transfer detection
- Port scanning with nmap and fallback methods
- TLS certificate inspection and validation
- Rich console output formatting
