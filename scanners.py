import subprocess
import requests

def run_nmap(target):
    print("[*] Running Nmap scan...")
    result = subprocess.run(["nmap", "-sV", "-oN", "scan_result.txt", target], capture_output=True, text=True)
    with open("scan_result.txt", "r") as f:
        return f.read()

def web_enum(target):
    try:
        print(f"[*] Checking web content at http://{target}")
        response = requests.get(f"http://{target}", timeout=5)
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error fetching web content: {str(e)}"
