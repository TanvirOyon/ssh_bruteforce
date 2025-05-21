🔐 SSH Brute-Force Simulation Tool
This is a Python-based SSH brute-force attack simulator designed for penetration testing training, cybersecurity demonstrations, and ethical hacking labs. The script leverages the paramiko library to attempt SSH login using a list of passwords from a local text file.

⚠️ DISCLAIMER
This tool is intended strictly for authorized educational and ethical use only.
Do not use this tool against any server or system you do not own or have explicit permission to test.
Unauthorized access is illegal and punishable under national and international laws.

📁 Project Structure
bash
Copy
Edit
ssh_attack/
├── ssh_bruteforce.py     # Main Python script for brute-force attempts
└── passwords.txt         # List of passwords to test
🚀 Features
✅ Lightweight and easy-to-read brute-force logic

🔑 SSH login attempts using paramiko

⏱️ Optional delay between tries to reduce lockout risk

🛡️ Error handling for common SSH/network issues

📜 Console log for each login attempt and result

🛠️ Requirements
Python 3.6+

paramiko

Install required dependency:

pip install paramiko
▶️ How to Run
Clone this repository or create the folder manually:

git clone https://github.com/TanvirOyon/ssh_bruteforce
cd ssh_bruteforce
Or manually place both ssh_bruteforce.py and passwords.txt in a folder named ssh_attack on your Desktop.

Run the script from terminal:

cd ~/Desktop/ssh_attack
python3 ssh_bruteforce.py
When prompted, enter:

Target IP address

Target SSH username

💻 Example Output

Enter target IP address: 192.168.1.100
Enter target username: admin

[INFO] Loaded 20 passwords from 'passwords.txt'.
Starting brute-force attack on 192.168.1.100 with user 'admin'...

Attempt 1/20: Trying password '123456'
[FAILURE] Authentication failed.

Attempt 7/20: Trying password 'letmein'
[SUCCESS] Login succeeded with password: 'letmein'
📌 Notes
Use longer delays (e.g., 10–15 seconds) between attempts to simulate real-world attacks and reduce detection/lockout risk.

You can customize passwords.txt with stronger, domain-specific, or more realistic credentials.

The tool stops immediately if a successful login occurs.

🛡️ Legal Notice
This software is developed only for:

Ethical hacking labs

Red team/internal assessments (with permission)

Academic cybersecurity education

Do not use this tool on unauthorized systems.
Doing so may violate national and international laws.

By using this tool, you agree to assume full responsibility and operate strictly within legal and ethical boundaries.

📬 Questions or feedback? Feel free to open an issue or contribute to the project.
