# SECR3253 Network Programming - Group Automation Project

**Project Status: COMPLETED**

## Team Members & Collaboration Roles

* **DILLAN REVADA (A23CS0290)** - *Lead:* Made foundational infrastructure by creating the Dockerfile, docker-compose.yml, inventory.yaml, ansible.cfg, and .gitignore files to ensure a stable, reproducible deployment environment. Developed and maintained the main_playbook.yml to orchestrate all team modules, while managing legacy dependency resolution to ensure compatibility with constrained lab environments. Authored all project documentation, including the comprehensive README.md and requirements.txt. Developed the pre_flight.py port-verification engine and the display_parser.py JSON aggregation dashboard, while providing the technical oversight required to perform final repository merges and structural integration of all team contributions.
* **DANIEL TRI HENDARTO TANRA (A23CS4040)** - *Network Engineer:* Handled initial Cisco IOS configurations, including GigabitEthernet IP assignments, local user privilege escalation, and MOTD banner deployment.
* **ABDELRAHMAN OSAMA SAID ABDELMODY (A23CS4001)** - *Systems Engineer:* Developed Linux automation tasks for host metadata, tracking CPU architecture, memory allocation, and system timestamps.
* **KHALID (A23CS0290)** - *Network Engineer:* Managed core routing and interface analytics, including static IPv4 route propagation, interface descriptions, and hardware facts retrieval.
* **MUHAMMAD ANGWIN SAYRESTIAN (A20EC0313)** - *Systems Engineer:* Automated continuous Linux health metrics, tracking disk utilization, active user sessions, and high-cpu top 5 processes.

---

## Project Overview

A comprehensive network automation project utilizing **Ansible**, **Docker**, and **Python** to provision a Cisco CSR1000v router and aggregate live health metrics from a Debian-based container.

## Project Requirements Fulfilled

**Cisco Router Configuration:**
* [x] Configure IP Addresses & Interface Descriptions
* [x] Configure User Accounts & Banner Message
* [x] Configure Static Routes
* [x] Retrieve Device Information



**Ubuntu/Debian Linux Server Analytics:**
* [x] Hostname, Date, and Time
* [x] CPU and Memory (RAM) Usage
* [x] Disk Space Utilization
* [x] Logged-in Users & Top 5 Processes by CPU



---

## Architecture & System Documentation

* **`.github/workflows/`**: Contains CI/CD pipeline for YAML linting and syntax validation.
* **`ansible.cfg`**: Configures execution parameters, disabling strict SSH host key checking for seamless automation.
* **`inventory.yaml`**: The infrastructure registry. Maps the `cisco_router` (192.168.56.102) to the `ios` network OS, securely handling `ansible_become` variables for privilege escalation via `cisco123!`.
* **`main_playbook.yml`**: Orchestrates the execution flow, targeting Cisco hardware first, then pivoting to Linux subsystem metrics.
* **`router_tasks.yml`**: Network module suite utilizing legacy-compatible `ios_config` modules for Ansible 2.9 compatibility.
* **`linux_stats_output.json`**: The aggregated JSON datastore built via `combine()` filters.
* **`display_parser.py`**: Custom Python parser that ingests JSON metrics and renders a human-readable health dashboard.
* **`Dockerfile`**: Lightweight Debian-based target environment for consistent system analytics.
* **`pre_flight.py`**: Network-socket verification script that validates reachability before playbook execution.

---


---

## Dependencies

To execute this automation stack, the following software environment is required:

* **Docker & Docker Compose**: Necessary to host the isolated Debian-based Linux test container.


* **Ansible (v2.9+)**: The core automation engine responsible for executing the network and system configuration playbooks.


* **Python 3**: Used for executing the `pre_flight.py` verification script and the `display_parser.py` analytics dashboard.

---

## How It Works

The project execution operates through a sequential automation loop:

1. **The Sandbox Phase**: Deployment of the target Linux environment via `docker-compose` to create an isolated, reachable test machine.


2. **The Pre-Flight Check**: Execution of `pre_flight.py` to perform active socket verification, ensuring both the VirtualBox Cisco router and the Docker container are reachable before starting the playbook.


3. **The Provisioning Phase**: Ansible reads `inventory.yaml` to establish secure connections. It first pushes network configurations to the Cisco router, utilizing `ios_config` modules for IP, banner, and static route deployment.


4. **The Analytics Phase**: Ansible pivots to the Docker container, executing shell-based system tasks to scrape hardware telemetry, including CPU, memory, and disk utilization, then saves the results to `linux_stats_output.json`.


5. **The Reporting Phase**: `display_parser.py` parses the generated JSON output and renders the finalized system health summary to the terminal.

## Quick Start & Deployment Guide

**1. Initialize the Target Infrastructure:**

```bash
docker-compose up -d --build

```

**2. Verify Network Reachability:**

```bash
python3 pre_flight.py

```

**3. Execute the Automation Stack:**

```bash
ansible-playbook main_playbook.yml

```

**4. Generate the Analytics Dashboard:**

```bash
python3 display_parser.py

```
