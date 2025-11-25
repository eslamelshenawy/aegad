import paramiko

HOST = '50.6.43.189'
USERNAME = 'pkqczdte'
KEY_FILE = 'E:/osama/id_rsa'
KEY_PASSWORD = '$wt%I&n!rwme'

def main():
    key = paramiko.RSAKey.from_private_key_file(KEY_FILE, password=KEY_PASSWORD)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=HOST, username=USERNAME, pkey=key, timeout=15, allow_agent=False, look_for_keys=False)
    sftp = client.open_sftp()

    # Check child theme style.css
    try:
        with sftp.file('public_html/wp-content/themes/dlist-developer/style.css', 'r') as f:
            content = f.read().decode('utf-8')
        print("=== dlist-developer/style.css ===")
        print(f"Size: {len(content)} chars")
        if 'listing-with-sidebar__listing' in content:
            print("FOUND: listing-with-sidebar__listing")
            # Print relevant lines
            for i, line in enumerate(content.split('\n')):
                if 'listing-with-sidebar__listing' in line:
                    print(f"Line {i}: {line[:100]}")
    except:
        print("dlist-developer/style.css not found")

    # Check main theme customizations
    try:
        with sftp.file('public_html/wp-content/themes/dlist/style.css', 'r') as f:
            content = f.read().decode('utf-8')
        print("\n=== dlist/style.css ===")
        print(f"Size: {len(content)} chars")
        if 'listing-with-sidebar__listing' in content:
            print("FOUND: listing-with-sidebar__listing")
    except:
        print("dlist/style.css not found")

    sftp.close()
    client.close()

if __name__ == "__main__":
    main()
