#!/usr/bin/env python3
from colorama import Fore, Style
import sys
import re

keywords = {
    "Usernames": [
        "admin", "administrator", "root", "guest", "test", "user", "manager", "sysadmin"
    ],
    "Sensitive Terms": [
        "secret", "confidential", "token", "key", "internal", "private", "restricted", "password", "123456", "letmein", "qwerty", "admin123", "welcome", "changeme"
    ]
}

# General patterns for common data types
patterns = {
    "IP Address": r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",
    "Domain": r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b",
    "Email Address": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "File Path": r"(?:/[a-zA-Z0-9._-]+)+(?=\s|$|[.,:])",
    "Hash": r"\b[a-fA-F0-9]{32,128}\b",  # MD5, SHA-256, etc.
    "CVE Reference": r"\bCVE-\d{4}-\d{4,7}\b",
    "Banner": r"\b[a-zA-Z]+\b/[0-9.]+",
    "Passwords": r"\b(?:password|p|pass|pwd)\s*[:=]\s*([a-zA-Z0-9!@#$%^&*()_+-]+)\b"
}


#Keyword-based patterns
patterns.update({
    category: r"\b(?:{})\b".format("|".join(map(re.escape, words)))
    for category, words in keywords.items()
})

category_colors = {
    "IP Address": Fore.BLUE,
    "Domain": Fore.CYAN,
    "Email Address": Fore.LIGHTMAGENTA_EX,
    "File Path": Fore.GREEN,
    "Hash": Fore.MAGENTA,
    "CVE Reference": Fore.LIGHTWHITE_EX,
    "Banner": Fore.LIGHTBLUE_EX,
    "Usernames": Fore.YELLOW,
    "Passwords": Fore.RED,
    "Sensitive Terms": Fore.CYAN
}

def highlight_info(data):
    highlighted = {}
    for category, pattern in patterns.items():
        matches = re.findall(pattern, data)

        # Extract groups if necessary
        if matches and isinstance(matches[0], tuple):
            matches = [match[0] for match in matches]

        matches = list(set(matches))  # Deduplicate matches

        if matches:
            highlighted[category] = matches
    return highlighted


def main():
    #Detect if input is piped or interactive
    if not sys.stdin.isatty():
        raw_output = sys.stdin.read()
    else:
        print(Fore.LIGHTMAGENTA_EX + "Paste output here. Press Ctrl+D (Linux/Mac) or Ctrl+Z (Windows) when done:" + Style.RESET_ALL)
        try:
            raw_output = sys.stdin.read()
        except KeyboardInterrupt:
            print(Fore.RED + "\n[!] Interrupted. Exiting." + Style.RESET_ALL)
            return

    if not raw_output.strip():
        print(Fore.RED + "[!] No input provided. Exiting." + Style.RESET_ALL)
        return

    print(Fore.GREEN + "\n[*] Original Output:" + Style.RESET_ALL)
    print(raw_output)

    print(Fore.LIGHTMAGENTA_EX + "\n[*] Highlighting critical information..." + Style.RESET_ALL)
    highlights = highlight_info(raw_output)

    print(Fore.CYAN + "\nHighlighted Summary:" + Style.RESET_ALL)
    for category, matches in highlights.items():
        color = category_colors.get(category, Fore.WHITE) 
        print(color + f"\n{category}:" + Style.RESET_ALL)
        if matches:
            for match in matches:
                print(color + f"  - {match}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "  (None found)" + Style.RESET_ALL)

if __name__ == "__main__":
    main()