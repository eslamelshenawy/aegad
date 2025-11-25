import paramiko
import re

HOST = '50.6.43.189'
USERNAME = 'pkqczdte'
KEY_FILE = 'E:/osama/id_rsa'
KEY_PASSWORD = '$wt%I&n!rwme'

# كود الماب الجديد - مثل Google Maps
MAP_CODE = '''
// ----------- تصميم الماب - Google Maps Style -----------
add_action('wp_head', 'aegad_map_fullwidth_design', 999);
function aegad_map_fullwidth_design() {
    ?>
    <style type="text/css">
    /* ========== Aegad Map - Google Maps Style ========== */

    /* السكشن اللي فيها الماب فقط */
    .directorist-archive-contents.directorist-w-100,
    .directorist-content-area-with-map {
        position: relative !important;
        width: 100% !important;
        height: 100vh !important;
        max-height: 100vh !important;
        overflow: hidden !important;
    }

    /* الماب نفسها - Full Screen */
    .directorist-archive-map,
    .directorist-map-wrapper,
    .atbdp-map,
    #gmap,
    .directorist-map,
    .directorist-archive-map__container {
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        bottom: 0 !important;
        width: 100% !important;
        height: 100% !important;
        z-index: 1 !important;
    }

    /* شريط البحث - أعلى الماب مثل Google */
    .directorist-archive-contents .directorist-search-form,
    .directorist-content-area-with-map .directorist-search-form,
    .directorist-map-wrapper .directorist-search-form {
        position: absolute !important;
        top: 15px !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        right: auto !important;
        width: 600px !important;
        max-width: calc(100% - 30px) !important;
        background: #fff !important;
        border-radius: 8px !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.3) !important;
        padding: 8px 15px !important;
        z-index: 1000 !important;
        display: flex !important;
        flex-wrap: wrap !important;
        align-items: center !important;
        gap: 10px !important;
    }

    /* إخفاء العناصر الغير ضرورية في الفلاتر */
    .directorist-search-form label,
    .directorist-search-form__title,
    .directorist-search-form h3 {
        display: none !important;
    }

    /* حقول البحث - inline مثل Google */
    .directorist-search-form .directorist-search-field,
    .directorist-search-form .form-group {
        flex: 1 !important;
        min-width: 150px !important;
        margin: 0 !important;
    }

    .directorist-search-form input,
    .directorist-search-form select {
        background: #f8f9fa !important;
        border: 1px solid #dfe1e5 !important;
        border-radius: 24px !important;
        padding: 10px 20px !important;
        font-size: 14px !important;
        width: 100% !important;
        margin: 0 !important;
        height: 44px !important;
    }

    .directorist-search-form input:focus,
    .directorist-search-form select:focus {
        border-color: #4285f4 !important;
        box-shadow: 0 1px 6px rgba(66,133,244,0.3) !important;
        outline: none !important;
    }

    /* زر البحث - دائري مثل Google */
    .directorist-search-form button[type="submit"],
    .directorist-search-form .btn-primary {
        background: #4285f4 !important;
        color: #fff !important;
        border: none !important;
        border-radius: 24px !important;
        padding: 10px 24px !important;
        font-weight: 500 !important;
        height: 44px !important;
        min-width: 100px !important;
        cursor: pointer !important;
        flex-shrink: 0 !important;
    }

    .directorist-search-form button[type="submit"]:hover {
        background: #3367d6 !important;
    }

    /* منع الماب من التأثير على السكشن التالية */
    .directorist-archive-contents.directorist-w-100 + *,
    .directorist-content-area-with-map + * {
        position: relative !important;
        z-index: 10 !important;
        margin-top: 0 !important;
    }

    /* ========== Responsive ========== */
    @media (max-width: 768px) {
        .directorist-archive-contents.directorist-w-100,
        .directorist-content-area-with-map {
            height: 70vh !important;
        }

        .directorist-archive-contents .directorist-search-form,
        .directorist-content-area-with-map .directorist-search-form {
            width: calc(100% - 20px) !important;
            top: 10px !important;
            flex-direction: column !important;
            padding: 10px !important;
        }

        .directorist-search-form input,
        .directorist-search-form select,
        .directorist-search-form button[type="submit"] {
            width: 100% !important;
        }
    }
    </style>
    <?php
}
'''

def main():
    print("="*60)
    print("Updating Map to Google Maps Style")
    print("="*60)

    try:
        key = paramiko.RSAKey.from_private_key_file(KEY_FILE, password=KEY_PASSWORD)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=HOST, username=USERNAME, pkey=key, timeout=15, allow_agent=False, look_for_keys=False)
        sftp = client.open_sftp()
        print("[SUCCESS] Connected!")

        theme_path = 'public_html/wp-content/themes/dlist/'
        functions_path = theme_path + 'functions.php'

        # قراءة الملف
        with sftp.file(functions_path, 'r') as f:
            content = f.read().decode('utf-8')

        print(f"[INFO] Original size: {len(content)} chars")

        # حذف كود الماب القديم فقط
        pattern = r"\n// [-]+ تصميم الماب[^\n]*\nadd_action\('wp_head', 'aegad_map_fullwidth_design'[^\n]*\nfunction aegad_map_fullwidth_design\(\) \{.*?\n\}\n?"
        content = re.sub(pattern, '\n', content, flags=re.DOTALL)

        print(f"[INFO] After removing old code: {len(content)} chars")

        # إضافة الكود الجديد
        if content.strip().endswith('?>'):
            content = content.rstrip()[:-2].rstrip() + '\n' + MAP_CODE + '\n?>'
        else:
            content = content.rstrip() + '\n' + MAP_CODE

        print(f"[INFO] Final size: {len(content)} chars")

        # رفع الملف
        with sftp.file(functions_path, 'w') as f:
            f.write(content.encode('utf-8'))

        print("[SUCCESS] functions.php updated!")

        # التحقق
        with sftp.file(functions_path, 'r') as f:
            verify = f.read().decode('utf-8')

        if 'Google Maps Style' in verify:
            print("[VERIFIED] New Google-style map code is in place!")

        sftp.close()
        client.close()

        print("\n" + "="*60)
        print("[DONE] Map updated to Google Maps style!")
        print("="*60)
        print("\nChanges:")
        print("- Map fills the section 100%")
        print("- Search bar at top center (like Google)")
        print("- Does NOT affect sections below")

    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
