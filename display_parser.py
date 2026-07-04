import json
import sys

def generate_dashboard(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)

        print("\n==================================================")
        print("      SYSTEM HEALTH REPORT (AUTO-GENERATED)")
        print("==================================================")
        print(f"Hostname:  {data.get('hostname', 'N/A')}")
        print(f"Date/Time: {data.get('time', 'N/A')}")
        
        print("\n--- CPU & MEMORY ---")
        print(f"CPU Info:  {data.get('cpu', 'N/A')}")
        print(f"RAM Usage: {data.get('ram', 'N/A')}")
        
        print("\n--- STORAGE ---")
        print("Disk Usage:")
        print(f"{data.get('disk', 'N/A')}")
        
        print("\n--- SYSTEM ACTIVITY ---")
        print("Active Users:")
        print(f"{data.get('users', 'N/A')}")
        
        print("\nTop 5 CPU Processes:")
        print(f"{data.get('processes', 'N/A')}")
        print("==================================================\n")

    except FileNotFoundError:
        print(f"[ERROR] Could not find {json_file}. Ensure Ansible ran successfully first.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("[ERROR] Failed to parse JSON data. Check Ansible output format.")
        sys.exit(1)

if __name__ == "__main__":
    # This expects Ansible to save the teammates' scraped data into this JSON file
    generate_dashboard('linux_stats_output.json')
