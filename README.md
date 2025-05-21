SSH Brute-Force Testing on Windows: 

1. Objective
Perform a controlled SSH brute-force password attack simulation on a Windows machine from a Kali/Linux attacker machine using Python and Paramiko.


2. Prerequisites
3. 
Attacker machine: Kali Linux or any Linux with Python3 and Paramiko installed
Target machine: Windows 10/11 with OpenSSH Server installed and running
Network: Both machines must be reachable via IP
Password list: A file (passwords.txt) with candidate passwords, one per line


4. Setting Up OpenSSH Server on Windows
3.1 Install OpenSSH Server
Go to Settings → Apps → Optional Features

Click Add a feature

Search for OpenSSH Server and click Install


3.2 Start and Enable SSH Service
Open PowerShell as Administrator and run:
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'
New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH SSH Server' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22

3.3 Verify SSH Service Status

Get-Service sshd
Should show Status : Running


4. Verify Network Connectivity
From the attacker machine, test connection:
ping <target_ip>
nmap -p 22 <target_ip>

Ensure port 22 is open.


5. Manual SSH Login Test
Try manual login from attacker machine:
ssh <username>@<target_ip>
Confirm you can connect with the correct password.

If the connection resets or refuses, fix SSH service or firewall first.

Creating the Required Files for SSH Brute-Force Testing:
Create a dedicated folder on Desktop:
 Name the folder ssh_attack to keep all related files organized and easily accessible.

Within the ssh_attack folder, create two files:
ssh_bruteforce.py — This will contain the Python script to perform the brute-force attack.
passwords.txt — This file will hold the list of candidate passwords, each on its own line.

Save the Python script (ssh_bruteforce.py) and the password list (passwords.txt) inside the ssh_attack folder.


6. Prepare Password List
Create passwords.txt with one password per line


7. Create Python Brute-Force Script


9. Running the Script
Run the script in terminal:
python3 ~/Desktop/ssh_attack/ssh_bruteforce.py

Enter the target IP and username when prompted.


The script will attempt each password in passwords.txt.


9. Understanding the "Connection reset by peer" Error
If you see:
Socket exception: Connection reset by peer (104)

Possible Causes & Solutions:
Too many login attempts too quickly: Increase delay between attempts (e.g., 15-30 seconds).
Windows Firewall blocking your attempts: Temporarily disable firewall or add an inbound rule allowing SSH port 22.
SSH service not running or misconfigured: Restart sshd service on Windows
Incorrect IP or port: Confirm target IP and SSH port are correct.



