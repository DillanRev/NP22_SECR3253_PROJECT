import subprocess
import sys

targets = {"Linux Server": "127.0.0.1", "Cisco Router": "192.168.1.100"}

def check_ping(hostname, ip):
    print(f"Testing connection to {hostname} ({ip})...")
    response = subprocess.run(['ping', '-c', '1', '-W', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if response.returncode == 0:
        print(f"[OK] {hostname} is reachable.\n")
        return True
    else:
        print(f"[FAIL] {hostname} is offline! Check Docker/GNS3.\n")
        return False

print("=== STARTING PRE-FLIGHT CHECKS ===")
all_pass = True
for name, ip in targets.items():
    if not check_ping(name, ip):
        all_pass = False

if not all_pass:
    print("Pre-flight failed. Aborting Ansible execution.")
    sys.exit(1)
else:
    print("All systems go. Ready to execute Ansible playbook.")
    sys.exit(0)
