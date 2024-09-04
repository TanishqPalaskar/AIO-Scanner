## Gobuster and Dirb Combined Directory & Subdomain Scanning Tool

This tool provides a simple interface to choose between Gobuster and Dirb for directory, subdomain, and DNS enumeration scans. It prompts the user for necessary inputs like target URL/IP and wordlist.

### Features:
- **Gobuster**:
  - Directory Scanning (`dir`): Brute-forces directories on web servers.
  - Subdomain Scanning (`dns`): Enumerates subdomains.
  - DNS Scanning: Performs DNS enumeration.
  - Virtual Host Scanning (`vhost`): Brute-forces virtual hosts.
  - Custom Wordlist: Allows you to input a custom wordlist for scanning.
- **Dirb**:
  - Default Directory Scanning: Uses Dirb's default wordlist to brute-force directories.
  - Custom Wordlist: Allows scanning with a custom wordlist.

### Usage:
1. Run the script.
2. Choose whether to use Gobuster or Dirb.
3. Input the target domain/IP and any required wordlist paths.
4. The tool will execute the appropriate Gobuster or Dirb scan and display the output.
