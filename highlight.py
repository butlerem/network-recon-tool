import re
from colorama import Fore

keywords = {
    "Usernames": [
        "admin", "administrator", "root", "guest", "test", "user", "manager", "sysadmin"
    ],
    "Passwords": [
        "password", "123456", "letmein", "qwerty", "admin123", "welcome", "changeme"
    ],
    "Sensitive Terms": [
        "secret", "confidential", "token", "key", "internal", "private", "restricted"
    ]
}

# General patterns for common data types
patterns = {
    "IP Address": r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",
    "Domain": r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b",
    "Email Address": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "File Path": r"(?:/[a-zA-Z0-9._-]+)+|[a-zA-Z]:\\[a-zA-Z0-9._\\-]+",
    "Hash": r"\b[a-fA-F0-9]{32,128}\b",  # MD5, SHA-256, etc.
    "CVE Reference": r"\bCVE-\d{4}-\d{4,7}\b",
    "Banner": r"\b[a-zA-Z]+\b/[0-9.]+"
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
    """Extracts and highlights critical information from raw text."""
    highlighted = {}
    for category, pattern in patterns.items():
        matches = list(set(re.findall(pattern, data)))  # Deduplicate matches
        if matches:
            highlighted[category] = matches
    return highlighted