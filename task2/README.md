This is Daniel's assignment:



For my part of the project, I was responsible for pushing the base configurations to the Cisco router: the IP address, the admin user account, and the warning banner. 



Here is how I approached the automation:

1\. Modules: I used the built-in `cisco.ios` modules (`ios\_user`, `ios\_banner`, and `ios\_config`). These are specifically designed for Cisco devices, which keeps the code clean and avoids having to send raw CLI commands.


2\. Credentials \& IP: Instead of guessing, I pulled the exact IP address (`192.168.1.100`) and the admin password directly from our `inventory.yaml` file to make sure my script matched our group's agreed-upon network design.


3\. Interface Mapping: To make sure the IP applied correctly, I verified our GNS3 simulation to confirm the router was using the `GigabitEthernet1` port, and coded that directly into the YAML task. 



By separating this into `router\_tasks.yml`, it keeps the main playbook clean and modular

