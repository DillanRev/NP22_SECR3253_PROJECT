# SECR3253 Network Programming - Group Automation Project
# DILLAN REVADA A23CS0290
# DANIEL
# ABDELRAHMAN
# KHALID
# ANGWIN

A simple automation project using **Ansible** and **Docker** to handle two things: configuring a Cisco router and scraping health metrics from a Linux server.

---

## Project Structure

Here is what every file in this directory actually does:

*   **`ansible.cfg`**
    Turns off strict SSH host key checking. This stops Ansible from crashing when it tries to connect to a new device it hasn’t seen before.
*   **`inventory.yaml`**
    The phonebook for the project. It holds the IP addresses, usernames, passwords, and connection methods for both the Cisco router and the Linux server.
*   **`main_playbook.yml`**
    The main entry point. When you run the project, this file executes first and tells Ansible to run the router tasks first, followed by the Linux server tasks.
*   **`router_tasks.yml`** *(Student 2 & 3)*
    The empty file where the network configurations go (setting up IPs, local user accounts, banners, interface descriptions, and static routes).
*   **`linux_tasks.yml`** *(Student 4 & 5)*
    The empty file where the Linux automation goes. It will run commands to grab system stats like hostname, CPU usage, RAM, and the top 5 running processes.
*   **`docker-compose.yml`**
    Spins up a lightweight Ubuntu container on your machine. This acts as our "target Linux server" so we have something live to test our scripts against without breaking our actual laptops.

---

## How It Works

The entire project runs in a straightforward 4-step loop:

    [ Your Laptop ] ──(Runs Ansible)──► Reads inventory.yaml to find targets
                                          │
                                          ├──► 1. Connects to Router -> Applies router_tasks.yml
                                          │
                                          └──► 2. Connects to Docker Container -> Runs linux_tasks.yml
                                                     ↳ Prints live CPU/RAM stats to your screen

1. **The Sandbox:** You start the Docker container to create a fake, isolated Linux machine sitting on your laptop.
2. **The Trigger:** You run the main Ansible playbook command.
3. **The Network Phase:** Ansible looks at the inventory file, connects to the simulated router, pushes all the required network configurations, and pulls back the basic device info.
4. **The Admin Phase:** Ansible connects straight into the running Docker container, collects the requested hardware and process stats, and prints a neat summary directly to your terminal window.

---
**Cisco Router Configuration:**
- [x] Configure IP Addresses & Interface Descriptions
- [x] Configure User Accounts & Banner Message
- [x] Configure Static Routes
- [x] Retrieve Device Information

**Ubuntu Linux Server Analytics:**
- [x] Hostname, Date, and Time
- [x] CPU and Memory (RAM) Usage
- [x] Disk Space Utilization
- [x] Logged-in Users & Top 5 Processes by CPU

## Dependencies

To run this automation stack, you only need two things installed on your system:

1. **Docker & Docker Compose** (To host the target Linux test environment).
2. **Ansible** (The core tool running the automation playbooks).

---

## Quick Start

**1. Start the local Linux target container:**
`docker-compose up -d`

**2. Run the automation script:**
`ansible-playbook main_playbook.yml`
