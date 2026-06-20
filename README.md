# URL Endpoint Fuzzer

A Python tool for bug bounty hunters to generate URLs with common security testing endpoints.
<img width="1078" height="453" alt="Screenshot 2026-06-20 at 10 07 48 AM" src="https://github.com/user-attachments/assets/e2b349d2-fdfe-45fc-8b49-3e02142716a0" />

## Features
- 44+ common endpoints (.git, .env, /admin, /api, etc.)
- Cross-platform (Windows, Mac, Linux)
- Save output to file for use with fuzzing tools
- Auto-normalizes URLs (adds https://)

## Installation
```bash
git clone https://github.com/GAHLOTAA13/url-endpoint-fuzzer.git
cd url-endpoint-fuzzer
```

## Usage
```bash
python3 url_fuzzer.py
```

**Example:**
```
Enter URL: example.com

Output:
https://example.com/.git
https://example.com/.env
https://example.com/admin
...
```

## Requirements
- Python 3.x (no external dependencies)
- multiurl extension (for chrome and firefox)

## Use Cases
- Bug bounty reconnaissance
- Security testing
- Directory/endpoint enumeration
- Integration with ffuf, gobuster, or other fuzzing tools

## Disclaimer
For educational and authorized security testing only. Always obtain proper permission before testing.

## License
MIT License
