import paramiko
from datetime import datetime

HOST = '50.6.43.189'
USERNAME = 'pkqczdte'
KEY_FILE = 'E:/osama/id_rsa'
KEY_PASSWORD = '$wt%I&n!rwme'

def main():
    print("="*60)
    print("Creating Server Backup")
    print("="*60)

    try:
        key = paramiko.RSAKey.from_private_key_file(KEY_FILE, password=KEY_PASSWORD)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=HOST, username=USERNAME, pkey=key, timeout=15, allow_agent=False, look_for_keys=False)
        sftp = client.open_sftp()
        print("[OK] Connected!")

        # Backup functions.php
        functions_path = 'public_html/wp-content/themes/dlist/functions.php'
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        # Download current file
        local_backup = f'E:/osama/aegad-final-code/backups/functions_server_{timestamp}.php'
        sftp.get(functions_path, local_backup)
        print(f"[OK] Downloaded functions.php to: {local_backup}")

        # Create backup on server too
        server_backup = f'public_html/wp-content/themes/dlist/functions_backup_{timestamp}.php'

        with sftp.file(functions_path, 'r') as f:
            content = f.read()

        with sftp.file(server_backup, 'w') as f:
            f.write(content)

        print(f"[OK] Server backup created: {server_backup}")

        sftp.close()
        client.close()
        print("\n[DONE] All backups created!")

    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()
