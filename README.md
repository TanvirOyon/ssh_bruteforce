# 🔐 SSH Brute-Force Simulation Tool

This is a Python-based SSH brute-force attack simulator designed for penetration testing training, and cybersecurity demonstrations. The script uses the `paramiko` library to attempt SSH login with multiple passwords from a text file.

> ⚠️ **DISCLAIMER:**  
> This tool is created strictly for **authorized educational use**. Never use this tool against any server or system that you do not own or have explicit permission to test. Unauthorized access is illegal and punishable by law.

---

## 📁 Project Structure
ssh_attack/
├── ssh_bruteforce.py # Python script for SSH brute-force attempts
└── passwords.txt # List of passwords to test

---

## 🚀 Features

- Simple brute-force logic for educational use
- Uses `paramiko` to establish SSH connections
- Supports delay between login attempts to avoid lockouts
- Handles common SSH errors gracefully
- Clean logging of each attempt and result

---

## 🛠️ Requirements

- Python 3.6 or higher
- `paramiko` library

Install requirements with:

pip install paramiko
---

▶️ How to Run
Clone this repository or copy the folder to your desktop:

git clone https://github.com/TanvirOyon/ssh_bruteforce
Navigate to the project directory:

cd ~/Desktop/ssh_attack
Make sure the passwords.txt file exists in the same directory.

Run the script:

python3 ssh_bruteforce.py
Enter the target IP address and username when prompted.

💻 Example Output

Enter target IP address: 192.168.1.100
Enter target username: admin

[INFO] Loaded 20 passwords from 'passwords.txt'.
Starting brute-force attack on 192.168.1.100 with user 'admin'...

Attempt 1/20: Trying password '123456'
[FAILURE] Authentication failed.
...
Attempt 7/20: Trying password 'letmein'

[SUCCESS] Login succeeded with password: 'letmein'
---

📌 Notes
Use longer delays (delay_seconds) to simulate realistic attacks and avoid account lockouts.

You can update the password list in passwords.txt with stronger or more specific passwords.

🛡️ Legal Notice
This tool is meant strictly for authorized testing, academic research, or personal lab environments.
Unauthorized access to systems you do not own or manage is a criminal offense.

By using this tool, you agree to use it only within legal and ethical boundaries.
