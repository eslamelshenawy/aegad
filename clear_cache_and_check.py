import paramiko

HOST = '50.6.43.189'
USERNAME = 'pkqczdte'
KEY_FILE = 'E:/osama/id_rsa'
KEY_PASSWORD = '$wt%I&n!rwme'

def main():
    print("="*60)
    print("Clearing Cache and Checking HTML")
    print("="*60)

    try:
        key = paramiko.RSAKey.from_private_key_file(KEY_FILE, password=KEY_PASSWORD)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=HOST, username=USERNAME, pkey=key, timeout=15, allow_agent=False, look_for_keys=False)
        print("[SUCCESS] Connected!")

        # مسح cache
        cache_paths = [
            'public_html/wp-content/cache/',
            'public_html/wp-content/uploads/cache/',
            'public_html/wp-content/w3tc-config/',
            'public_html/wp-content/et-cache/',
        ]

        for path in cache_paths:
            stdin, stdout, stderr = client.exec_command(f'rm -rf {path}* 2>/dev/null; echo "Cleared {path}"')
            print(stdout.read().decode())

        # جلب HTML الصفحة بـ curl
        print("\n" + "="*60)
        print("Fetching page HTML...")
        print("="*60)

        stdin, stdout, stderr = client.exec_command(
            'curl -s "https://sa.aegad.com/" | grep -o \'class="[^"]*directorist[^"]*"\' | head -20'
        )
        classes = stdout.read().decode()
        print("Directorist classes found:")
        print(classes if classes else "None found via curl")

        # جلب هيكل الماب
        print("\n" + "="*60)
        print("Looking for map container structure...")
        print("="*60)

        stdin, stdout, stderr = client.exec_command(
            '''curl -s "https://sa.aegad.com/" | grep -oE '<div[^>]*(map|filter|archive)[^>]*>' | head -15'''
        )
        structure = stdout.read().decode()
        print("Map/Filter divs:")
        print(structure if structure else "None found")

        # التحقق من أن الـ CSS موجود في head
        print("\n" + "="*60)
        print("Checking if our CSS is in page head...")
        print("="*60)

        stdin, stdout, stderr = client.exec_command(
            '''curl -s "https://sa.aegad.com/" | grep -o "aegad_map_fullwidth_design\|Aegad Map"'''
        )
        css_check = stdout.read().decode()
        if css_check:
            print("[OK] Our CSS is being loaded!")
        else:
            print("[WARNING] Our CSS might not be loading")

        # فحص ملف functions.php لوجود أخطاء
        print("\n" + "="*60)
        print("Checking functions.php for syntax errors...")
        print("="*60)

        stdin, stdout, stderr = client.exec_command(
            'cd public_html && php -l wp-content/themes/dlist/functions.php 2>&1'
        )
        php_check = stdout.read().decode()
        print(php_check)

        client.close()

    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
