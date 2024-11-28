from highlight import highlight_info
from colorama import Fore, Style
import sys

def main():
    #Read raw output from stdin (pipe or paste)
    print(Fore.YELLOW + "Paste or pipe the tool's output into this script. Press Ctrl+D (Linux/Mac) or Ctrl+Z (Windows) when done:" + Style.RESET_ALL)
    try:
        raw_output = sys.stdin.read()  # Read until EOF
        if not raw_output.strip():
            print(Fore.RED + "[!] No input provided. Exiting." + Style.RESET_ALL)
            return
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Interrupted. Exiting." + Style.RESET_ALL)
        return

    #Display the original output
    print(Fore.GREEN + "\n[*] Original Output:" + Style.RESET_ALL)
    print(raw_output)

    #Highlight critical information
    print(Fore.GREEN + "\n[*] Highlighting critical information..." + Style.RESET_ALL)
    highlights = highlight_info(raw_output)

    #Display the highlighted summary
    print(Fore.CYAN + "\nHighlighted Summary:" + Style.RESET_ALL)
    for key, values in highlights.items():
        print(Fore.YELLOW + f"\n{key}:" + Style.RESET_ALL)
        if values:
            for value in values:
                print(Fore.CYAN + f"  - {value}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "  (None found)" + Style.RESET_ALL)

if __name__ == "__main__":
    main()