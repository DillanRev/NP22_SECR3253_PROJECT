import subprocess
import sys
import platform

targets = {"Linux Server": "127.0.0.1", "Cisco Router": "192.168.56.102"}

def check_ping(hostname, ip):
    print(f"Testing connection to {hostname} ({ip})...")
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    timeout_param = '-w' if platform.system().lower() == 'windows' else '-W'
    
    timeout_val = '1000' if platform.system().lower() == 'windows' else '1'
    
    response = subprocess.run(
        ['ping', param, '1', timeout_param, timeout_val, ip], 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE
    )
    
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
