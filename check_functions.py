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

    with sftp.file('public_html/wp-content/themes/dlist/functions.php', 'r') as f:
        content = f.read().decode('utf-8')

    # Save locally
    with open('E:/osama/aegad-final-code/current_functions.php', 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Downloaded: {len(content)} chars")

    # Count CSS blocks
    import re
    css_blocks = re.findall(r'<style[^>]*>.*?</style>', content, re.DOTALL)
    print(f"CSS blocks: {len(css_blocks)}")

    # Check for elementor-element-7fd6f4bb mentions
    mentions = content.count('elementor-element-7fd6f4bb')
    print(f"elementor-element-7fd6f4bb mentions: {mentions}")

    sftp.close()
    client.close()

if __name__ == "__main__":
    main()
