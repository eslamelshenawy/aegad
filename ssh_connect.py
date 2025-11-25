import paramiko
import sys

def connect_ssh(host, username, key_file, key_password):
    """
    Connect to SSH server using RSA key
    """
    try:
        # Load the private key - try RSA first
        print("Loading SSH key...")
        try:
            key = paramiko.RSAKey.from_private_key_file(key_file, password=key_password)
            print("[SUCCESS] RSA key loaded")
        except Exception as e:
            # Try other key types
            try:
                key = paramiko.Ed25519Key.from_private_key_file(key_file, password=key_password)
                print("[SUCCESS] Ed25519 key loaded")
            except:
                try:
                    key = paramiko.ECDSAKey.from_private_key_file(key_file, password=key_password)
                    print("[SUCCESS] ECDSA key loaded")
                except Exception as e:
                    print(f"[FAILED] Could not load key: {e}")
                    return None

        # Create SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect
        print(f"Connecting to {host}...")
        client.connect(
            hostname=host,
            username=username,
            pkey=key,
            timeout=15,
            allow_agent=False,
            look_for_keys=False
        )

        print(f"[SUCCESS] Connected to {host}")
        return client

    except Exception as e:
        print(f"[FAILED] Connection failed: {e}")
        return None

def get_sftp(client):
    """
    Get SFTP client from SSH connection
    """
    try:
        sftp = client.open_sftp()
        print("[SUCCESS] SFTP session opened")
        return sftp
    except Exception as e:
        print(f"[FAILED] SFTP failed: {e}")
        return None

if __name__ == "__main__":
    # Server credentials
    HOST = '50.6.43.189'
    USERNAME = 'pkqczdte'
    KEY_FILE = 'E:/osama/id_rsa'
    KEY_PASSWORD = '$wt%I&n!rwme'

    print("\n" + "="*60)
    print("SSH CONNECTION TEST")
    print("="*60)
    print(f"Host: {HOST}")
    print(f"Username: {USERNAME}")
    print(f"Key: {KEY_FILE}")
    print("="*60 + "\n")

    # Connect
    client = connect_ssh(HOST, USERNAME, KEY_FILE, KEY_PASSWORD)

    if client:
        # Get SFTP
        sftp = get_sftp(client)

        if sftp:
            # List files in public_html
            print("\nListing files in public_html/:")
            try:
                files = sftp.listdir('public_html')
                for f in files[:10]:  # Show first 10 files
                    print(f"  - {f}")
                if len(files) > 10:
                    print(f"  ... and {len(files) - 10} more files")
            except Exception as e:
                print(f"Error listing files: {e}")

            # Close connections
            sftp.close()

        client.close()
        print("\n[SUCCESS] Connection test completed")
        print("="*60)
    else:
        print("\n[FAILED] Could not establish connection")
        sys.exit(1)
