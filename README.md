# Automated Data Extraction for Pen Testing

## Overview

Hilite is a Python tool that extracts and highlights important information from scan results or logs. The tool works seamlessly with outputs from various scanning tools commonly used in security assessments to quickly parse relevant data.

## Features:

- Extracts and highlights IP addresses, domain names, email addresses, file paths, hashes, CVE references, usernames, passwords, and sensitive terms.
- Supports both interactive and piped inputs.
- Helps highlight key information in scan results from tools like Nmap, Whois, Nikto, CVE databases, and more.

## Installation

### Manual

Download hilite.py and save it to a folder of your choice.

Make the script executable (optional):

```bash
chmod +x hilite.py
```

Move the script to /usr/local/bin (optional, for global access):

```bash
sudo mv hilite.py /usr/local/bin/hilite
```

Run the tool:

```bash
    echo "Your scan output here" | hilite
```

Or

### Use in a Python Virtual Environment

Create a virtual environment and install the required package:

```bash
python3 -m venv venv
source venv/bin/activate
pip install colorama
```

Run hilite.py inside the virtual environment:

```bash
python hilite.py
```

## Usage

To use hilite during a scan, simply pipe the output of the scan tool (like nmap, whois, etc.) directly into the script. For example:

```bash
nmap -sV target.com | hilite
```

Or, if you haven't moved the script to /usr/local/bin, you can run it directly using:

```bash
echo "Your scan output here" | python3 hilite.py
```

This will automatically highlight and display critical information like IP addresses, usernames, passwords, file paths, CVE references, and more directly from the scan output.

## License

MIT License. See LICENSE file for more details.
