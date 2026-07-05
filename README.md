# SECR3253 Network Programming - Group Automation Project
# DILLAN REVADA A23CS0290
# DANIEL
# ABDELRAHMAN Osama Said Abdelmobdy A23CS4001
# KHALID  A23CS4042
# ANGWIN

A simple automation project using **Ansible** and **Docker** to handle two things: configuring a Cisco router and scraping health metrics from a Linux server.

---

## Project Structure

Here is what every file in this directory actually does:

*   **`.github/workflows/`**
    Contains our CI/CD pipeline. Automatically runs a syntax check on our Ansible YAML files every time a team member makes a Pull Request.
*   **`ansible.cfg`**
    Turns off strict SSH host key checking. This stops Ansible from crashing when it tries to connect to a new device it hasn’t seen before.
*   **`inventory.yaml`**
    The phonebook for the project. It holds the IP addresses, usernames, passwords, and connection methods for both the Cisco router and the Linux server.
*   **`main_playbook.yml`**
    The main entry point. When you run the project, this file executes first and tells Ansible to run the router tasks first, followed by the Linux server tasks.
*   **`router_tasks.yml`** *(Student 2 & 3)*
    The empty file where the network configurations go (setting up IPs, local user accounts, banners, interface descriptions, and static routes).
*   **`linux_tasks.yml`** *(Student 4 & 5)*
    The empty file where the Linux automation goes. It will run commands to grab system stats like hostname, CPU usage, RAM, and the top 5 running processes, outputting them to a JSON file.
*   **`display_parser.py`**
    A custom Python script that ingests the raw JSON output from the Linux server metrics and renders a human-readable system health dashboard directly to the terminal.
*   **`docker-compose.yml` & `Dockerfile`**
    Spins up a custom, lightweight Ubuntu container with SSH and Python pre-installed. This acts as our "target Linux server" so we have something live to test our scripts against without breaking our actual laptops.
*   **`pre_flight.py`**
    A Python script that pings our target devices (Router and Docker container) to verify they are awake before we allow Ansible to run.

---

## How It Works

The entire project runs in a 4 step loop:

    [ Computer ] ──(Runs Ansible)──► Reads inventory.yaml to find targets
                                          │
                                          ├──► 1. Connects to Router -> Applies router_tasks.yml
                                          │
                                          └──► 2. Connects to Docker Container -> Runs linux_tasks.yml
                                                     ↳ Saves data to linux_stats_output.json
                                                     ↳ display_parser.py reads JSON and prints stats to screen

1. **The Sandbox:** You start the Docker container to create a fake, isolated Linux machine sitting on your laptop.
2. **The Pre-Flight:** You run the Python script to ensure the network is reachable.
3. **The Trigger:** You run the main Ansible playbook command.
4. **The Network Phase:** Ansible looks at the inventory file, connects to the simulated router, pushes all the required network configurations, and pulls back the basic device info.
5. **The Admin Phase:** Ansible connects straight into the running Docker container, collects the requested hardware and process stats, and saves them locally. Finally, the Python parser executes to display the neat summary to your terminal window.

---

## Project Requirements Fulfilled

**Cisco Router Configuration:**
- [ ] Configure IP Addresses & Interface Descriptions
- [ ] Configure User Accounts & Banner Message
- [ ] Configure Static Routes
- [ ] Retrieve Device Information

**Ubuntu Linux Server Analytics:**
- [ ] Hostname, Date, and Time
- [ ] CPU and Memory (RAM) Usage
- [ ] Disk Space Utilization
- [ ] Logged-in Users & Top 5 Processes by CPU

---

## Dependencies

To run this automation stack, you only need two things installed on your system:

1. **Docker & Docker Compose** (To host the target Linux test environment).
2. **Ansible** (The core tool running the automation playbooks).

---

## Quick Start

**1. Start the local Linux target container:**
`docker-compose up -d --build`

**2. Verify the network is reachable:**
`python3 pre_flight.py`

**3. Run the automation script:**
`ansible-playbook main_playbook.yml`

**4. Generate the terminal dashboard:**
`python3 display_parser.py`
