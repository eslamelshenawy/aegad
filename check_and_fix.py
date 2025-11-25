import paramiko
import requests

HOST = '50.6.43.189'
USERNAME = 'pkqczdte'
KEY_FILE = 'E:/osama/id_rsa'
KEY_PASSWORD = '$wt%I&n!rwme'

def main():
    print("="*60)
    print("Checking Server and Page Structure")
    print("="*60)

    # 1. التحقق من الكود على السيرفر
    try:
        key = paramiko.RSAKey.from_private_key_file(KEY_FILE, password=KEY_PASSWORD)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=HOST, username=USERNAME, pkey=key, timeout=15, allow_agent=False, look_for_keys=False)
        sftp = client.open_sftp()
        print("[SUCCESS] Connected to server!")

        # قراءة functions.php
        functions_path = 'public_html/wp-content/themes/dlist/functions.php'
        with sftp.file(functions_path, 'r') as f:
            content = f.read().decode('utf-8')

        # التحقق من وجود كود الماب
        if 'aegad_map_fullwidth_design' in content:
            print("[OK] Map code EXISTS in functions.php")
            # عرض جزء من الكود
            start = content.find('aegad_map_fullwidth_design')
            print(f"[INFO] Code starts at position: {start}")
        else:
            print("[ERROR] Map code NOT FOUND in functions.php!")

        sftp.close()
        client.close()

    except Exception as e:
        print(f"[ERROR] Server: {e}")

    # 2. فحص HTML الصفحة
    print("\n" + "="*60)
    print("Fetching page HTML to find correct CSS classes...")
    print("="*60)

    try:
        response = requests.get('https://sa.aegad.com/', timeout=30, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        html = response.text

        # البحث عن classes الماب
        classes_to_find = [
            'directorist-archive-contents',
            'directorist-archive-map',
            'directorist-search-form',
            'directorist-col-lg-4',
            'directorist-col-lg-8',
            'atbdp-map',
            'gm-style',
            'directorist-row',
            'directorist-archive-sidebar',
        ]

        print("\nFound classes in HTML:")
        for cls in classes_to_find:
            if cls in html:
                # عرض السياق
                idx = html.find(cls)
                context = html[max(0,idx-50):idx+100]
                print(f"\n[FOUND] {cls}")
                print(f"  Context: ...{context[:150]}...")
            else:
                print(f"[NOT FOUND] {cls}")

        # البحث عن هيكل الماب
        print("\n" + "="*60)
        print("Looking for map section structure...")
        print("="*60)

        # البحث عن divs مع map
        import re
        map_divs = re.findall(r'<div[^>]*class="[^"]*map[^"]*"[^>]*>', html, re.IGNORECASE)
        print(f"\nFound {len(map_divs)} map-related divs:")
        for div in map_divs[:10]:
            print(f"  {div[:150]}")

    except Exception as e:
        print(f"[ERROR] Fetching page: {e}")

if __name__ == "__main__":
    main()
