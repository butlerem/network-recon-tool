import subprocess

def scan_network(target):
    command = f"nmap -Pn -p 1-1024 {target}"
    result = subprocess.run(command.split(), capture_output=True, text=True)
    return result.stdout
