import paramiko

HOST = '50.6.43.189'
USERNAME = 'pkqczdte'
KEY_FILE = 'E:/osama/id_rsa'
KEY_PASSWORD = '$wt%I&n!rwme'

def main():
    print("="*60)
    print("Fixing functions.php to enqueue map CSS")
    print("="*60)

    try:
        key = paramiko.RSAKey.from_private_key_file(KEY_FILE, password=KEY_PASSWORD)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=HOST, username=USERNAME, pkey=key, timeout=15, allow_agent=False, look_for_keys=False)
        sftp = client.open_sftp()
        print("[SUCCESS] Connected!")

        # Read functions.php
        functions_path = 'public_html/wp-content/themes/dlist/functions.php'
        with sftp.file(functions_path, 'r') as f:
            content = f.read().decode('utf-8')

        print(f"[INFO] functions.php size: {len(content)} chars")

        # Check if already enqueued
        if 'aegad-map-style' in content:
            print("[INFO] aegad-map-style already present!")
        else:
            # Try to add enqueue - look for wp_enqueue_style patterns
            # Add at the end of the file before ?>

            enqueue_code = '''
// ----------- تحميل CSS الماب الجديد - Full Width Map -----------
add_action('wp_enqueue_scripts', 'aegad_map_fullwidth_css', 999);
function aegad_map_fullwidth_css() {
    wp_enqueue_style('aegad-map-style', get_stylesheet_directory_uri() . '/aegad-map-style.css', array(), time());
}
'''
            # Find the closing ?> and add before it
            if '?>' in content:
                content = content.replace('?>', enqueue_code + '\n?>')
            else:
                content = content + '\n' + enqueue_code

            # Upload
            with sftp.file(functions_path, 'w') as f:
                f.write(content.encode('utf-8'))

            print("[SUCCESS] functions.php updated!")

        sftp.close()
        client.close()
        print("[DONE] CSS will now be loaded on the site!")

    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
