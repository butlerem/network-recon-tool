from highlight import highlight_info
from scanners import run_nmap, web_enum
from colorama import Fore, Style
import json

def main():
    target = input("Enter the target IP or domain: ").strip()
    if not target:
        print(Fore.RED + "[!] No target provided. Exiting." + Style.RESET_ALL)
        return
    
    #Run nmap scan
    print(Fore.BLUE + "[*] Running Nmap scan on target..." + Style.RESET_ALL)
    try:
        nmap_results = run_nmap(target)
        print(Fore.GREEN + "[+] Nmap scan completed." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[!] Error running Nmap: {e}" + Style.RESET_ALL)
        return
    
    print(Fore.YELLOW + "\n[*] Highlighting results from Nmap..." + Style.RESET_ALL)
    nmap_highlights = highlight_info(nmap_results)
    print(Fore.CYAN + json.dumps(nmap_highlights, indent=4) + Style.RESET_ALL)

    #Perform web content enumeration
    print(Fore.BLUE + f"[*] Fetching web content from http://{target}..." + Style.RESET_ALL)
    try:
        web_results = web_enum(target)
        print(Fore.GREEN + "[+] Web content fetched successfully." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[!] Error fetching web content: {e}" + Style.RESET_ALL)
        return
    
    print(Fore.YELLOW + "\n[*] Highlighting results from web content..." + Style.RESET_ALL)
    web_highlights = highlight_info(web_results)
    print(Fore.CYAN + json.dumps(web_highlights, indent=4) + Style.RESET_ALL)

    print(Fore.YELLOW + "\n[*] Final combined results:" + Style.RESET_ALL)
    combined_results = {
        "Nmap Results": nmap_highlights,
        "Web Content Results": web_highlights
    }
    print(Fore.CYAN + json.dumps(combined_results, indent=4) + Style.RESET_ALL)

if __name__ == "__main__":
    main()