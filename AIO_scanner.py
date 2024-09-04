import os

def run_gobuster_scan(target):
    options = {
        "1": "Directory scan (e.g., /admin, /login)",
        "2": "Subdomain scan",
        "3": "DNS scan (for domain enumeration)",
        "4": "VHost scan",
        "5": "Custom wordlist scan"
    }

    print("\nChoose a Gobuster scan type:")
    for key, value in options.items():
        print(f"{key}: {value}")
    
    choice = input("\nEnter the number of the Gobuster scan type you want to run: ")

    if choice == "1":
        wordlist = input("Enter the path to your wordlist (e.g., /usr/share/wordlists/dirb/common.txt): ")
        command = f"gobuster dir -u {target} -w {wordlist}"
    elif choice == "2":
        wordlist = input("Enter the path to your subdomain wordlist (e.g., /usr/share/wordlists/subdomains.txt): ")
        command = f"gobuster dns -d {target} -w {wordlist}"
    elif choice == "3":
        dns_server = input("Enter the DNS server (optional, press Enter to skip): ")
        if dns_server:
            command = f"gobuster dns -d {target} -w /usr/share/wordlists/dns/subdomains-top1million-110000.txt -s {dns_server}"
        else:
            command = f"gobuster dns -d {target} -w /usr/share/wordlists/dns/subdomains-top1million-110000.txt"
    elif choice == "4":
        wordlist = input("Enter the path to your virtual host wordlist (e.g., /usr/share/wordlists/vhosts.txt): ")
        command = f"gobuster vhost -u {target} -w {wordlist}"
    elif choice == "5":
        wordlist = input("Enter the path to your custom wordlist: ")
        scan_type = input("Choose scan type: 'dir', 'dns', or 'vhost': ")
        if scan_type in ["dir", "dns", "vhost"]:
            command = f"gobuster {scan_type} -u {target} -w {wordlist}"
        else:
            print("Invalid scan type.")
            return
    else:
        print("Invalid option selected.")
        return

    print(f"\nRunning: {command}")
    os.system(command)

def run_dirb_scan(target):
    options = {
        "1": "Default directory scan",
        "2": "Custom wordlist scan"
    }

    print("\nChoose a Dirb scan type:")
    for key, value in options.items():
        print(f"{key}: {value}")

    choice = input("\nEnter the number of the Dirb scan type you want to run: ")

    if choice == "1":
        command = f"dirb {target}"
    elif choice == "2":
        wordlist = input("Enter the path to your wordlist (e.g., /usr/share/wordlists/dirb/common.txt): ")
        command = f"dirb {target} {wordlist}"
    else:
        print("Invalid option selected.")
        return

    print(f"\nRunning: {command}")
    os.system(command)

if __name__ == "__main__":
    print("Select a tool to run:")
    print("1: Gobuster")
    print("2: Dirb")

    tool_choice = input("\nEnter the number of the tool you want to use: ")

    # Ask for the target domain or IP
    target_input = input("\nEnter the domain or IP address you want to scan: ")

    if tool_choice == "1":
        run_gobuster_scan(target_input)
    elif tool_choice == "2":
        run_dirb_scan(target_input)
    else:
        print("Invalid selection.")
