import random
from datetime import datetime, timedelta

def make_logs():
    """Creates log file that include brute force attack."""
    
    print("Creating Server_Activity.log...")
    
    # Clear any old file
    with open("Server_Activity.log", "w") as f:
        f.write("")  # Empty the file
    
    lines = []
    
    # Normal traffic (status 200 = success)
    base_time = datetime.now() - timedelta(hours=1)
    
    # Add 15 normal logins
    for i in range(15):
        ip = f"192.168.1.{random.randint(100, 200)}"
        time = base_time + timedelta(seconds=random.randint(0, 3600))
        lines.append(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [{ip}] [200] [User] [Login OK]")
    
    # BRUTE FORCE ATTACK - 10 failed logins from same IP
    attack_ip = "45.33.1.20"
    attack_start = base_time + timedelta(minutes=30)
    
    # 10 rapid failed attempts (every 2 seconds)
    for i in range(10):
        time = attack_start + timedelta(seconds=i*2)
        lines.append(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [{attack_ip}] [401] [admin] [Login FAILED]")
    
    # Add more normal traffic
    for i in range(10):
        ip = f"192.168.1.{random.randint(100, 200)}"
        time = attack_start + timedelta(minutes=5, seconds=random.randint(0, 300))
        lines.append(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [{ip}] [200] [User] [Login OK]")
    
    # Sort by time and save
    lines.sort()
    
    with open("Server_Activity.log", "w") as f:
        f.write("\n".join(lines))
    
    print(f"Created Server_Activity.log with {len(lines)} lines")
    print(f" Attack IP {attack_ip} has 10 failed logins (401 status)")

if __name__ == "__main__":
    make_logs()