import re

def highlight_info(data):
    patterns = {
        "IP Address": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
        "Username": r"(?i)(user(name)?|login):?\s*\w+",
        "Password": r"(?i)password:?\s*\w+",
        "Domain": r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b"
    }
    highlighted = {}
    for key, pattern in patterns.items():
        highlighted[key] = re.findall(pattern, data)
    return highlighted
