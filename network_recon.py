from highlight import highlight_info
from scanners import run_nmap, web_enum
from colorama import Fore, Style

def main():
    target = input("Enter the target IP or domain: ").strip()
    if not target:
        print(Fore.RED + "[!] No target provided. Exiting." + Style.RESET_ALL)
        return
    
    #Run the nmap scan
    print(Fore.BLUE + "[*] Running Nmap scan on target..." + Style.RESET_ALL)
    try:
        nmap_results = run_nmap(target)
        print(Fore.GREEN + "[+] Nmap scan completed." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[!] Error running Nmap: {e}" + Style.RESET_ALL)
        return

    
    #Perform web content enumeration
    print(Fore.BLUE + f"[*] Fetching web content from http://{target}..." + Style.RESET_ALL)
    try:
        web_results = web_enum(target)
        print(Fore.GREEN + "[+] Web content fetched successfully." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[!] Error fetching web content: {e}" + Style.RESET_ALL)
        return
