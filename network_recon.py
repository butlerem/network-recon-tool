from highlight import highlight_info, category_colors
from colorama import Fore, Style
import sys

def main():
    #Detect if input is piped or interactive
    if not sys.stdin.isatty():
        raw_output = sys.stdin.read()
    else:
        print(Fore.YELLOW + "Paste the tool's output into this script. Press Ctrl+D (Linux/Mac) or Ctrl+Z (Windows) when done:" + Style.RESET_ALL)
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

    print(Fore.GREEN + "\n[*] Highlighting critical information..." + Style.RESET_ALL)
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