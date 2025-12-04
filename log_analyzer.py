from datetime import datetime
import re


def analyze_logs():
    """
    This function reads the Server_Activity.log file and checks for brute force attacks.
    """

    print("Starting security analysis...")

    # Dictionary to count failed logins per IP
    failed_counts = {}

    # Regex pattern matching the generator's log format
    pattern = re.compile(r"^\[(?P<time>[^\]]+)\]\s+\[(?P<ip>[^\]]+)\]\s+\[(?P<status>\d+)\]\s+\[(?P<user>[^\]]+)\]\s+\[(?P<msg>[^\]]+)\]$")

    try:
        # Open and read the log file
        with open("Server_Activity.log", "r") as log_file:
            for line in log_file:
                line = line.strip()
                if not line:
                    continue

                m = pattern.match(line)
                if not m:
                    # Skip lines silently 
                    continue

                status = int(m.group('status'))
                if status == 401:
                    ip = m.group('ip')
                    failed_counts[ip] = failed_counts.get(ip, 0) + 1

    except FileNotFoundError:
        print("Error: Could not find Server_Activity.log")
        return
    
    # Check for brute force attacks
    # Rule: More than 5 failed attempts from same IP
    attacks_found = []
    for ip, count in failed_counts.items():
        if count >= 5:
            attacks_found.append({"ip": ip, "count": count})
    
    # Create the security report
    report_file = open("report.txt", "w")
    
    # Write report header
    report_file.write("=" * 60 + "\n")
    report_file.write("SECURITY ANALYSIS REPORT\n")
    report_file.write("=" * 60 + "\n\n")
    
    # Write analysis details
    report_file.write("Report Details:\n")
    report_file.write("-" * 40 + "\n")
    report_file.write(f"Analysis Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    report_file.write(f"Log File: Server_Activity.log\n")
    report_file.write(f"Detection Rule: IPs with 5+ failed login attempts\n\n")
    
    # Write findings
    report_file.write("Analysis Results:\n")
    report_file.write("-" * 40 + "\n")
    
    if attacks_found:
        report_file.write("HIGH SEVERITY - BRUTE FORCE ATTACKS DETECTED:\n\n")
        
        for attack in attacks_found:
            report_file.write(f"ATTACKING IP: {attack['ip']}\n")
            report_file.write(f"Failed Attempts: {attack['count']}\n")
            report_file.write(f"Severity Level: CRITICAL\n")
            report_file.write(f"Recommended Action: Block this IP at firewall\n")
            report_file.write(f"Reason: Brute force password attack detected\n")
            report_file.write("-" * 40 + "\n")
    else:
        report_file.write("No brute force attacks detected.\n\n")
    
    # Write summary
    report_file.write("\nSummary:\n")
    report_file.write("-" * 40 + "\n")
    report_file.write(f"Total IPs checked: {len(failed_counts)}\n")
    report_file.write(f"Total failed logins found: {sum(failed_counts.values())}\n")
    report_file.write(f"Brute force attacks detected: {len(attacks_found)}\n")
    
    report_file.close()
    
    # Print results to screen
    print("\n" + "=" * 50)
    print("ANALYSIS COMPLETE")
    print("=" * 50)
    
    if attacks_found:
        print(f"HIGH ALERT: Found {len(attacks_found)} brute force attack(s)!")
        for attack in attacks_found:
            print(f"  - IP {attack['ip']}: {attack['count']} failed attempts")
    else:
        print("No brute force attacks detected.")
    
    print(f"\nReport saved to: report.txt")

# Running the function after script is executed
if __name__ == "__main__":
    analyze_logs()