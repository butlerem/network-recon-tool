from highlight import highlight_info
from scanners import run_nmap, web_enum
from colorama import Fore, Style  # For colored output

def main():
    #Get the target from the user
    target = input("Enter the target IP or domain: ").strip()
    if not target:
        print(Fore.RED + "[!] No target provided. Exiting." + Style.RESET_ALL)
        return