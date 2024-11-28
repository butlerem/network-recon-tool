from utils.scanner import scan_network

if __name__ == "__main__":
    target = input("Enter the target IP or domain: ")
    output = scan_network(target)
    print(output)
