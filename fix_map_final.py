import paramiko
import re

HOST = '50.6.43.189'
USERNAME = 'pkqczdte'
KEY_FILE = 'E:/osama/id_rsa'
KEY_PASSWORD = '$wt%I&n!rwme'

# كود الماب المظبوط
MAP_CODE = '''
// ----------- تصميم الماب - Google Maps Style -----------
add_action('wp_head', 'aegad_map_fullwidth_design', 999);
function aegad_map_fullwidth_design() {
    ?>
    <style type="text/css">
    /* ========== Aegad Map - Google Maps Style - FIXED ========== */

    /* الكونتينر الرئيسي للماب */
    .directorist-archive-contents.directorist-w-100,
    .directorist-content-area-with-map,
    .directorist-archive-map-wrapper {
        position: relative !important;
        width: 100% !important;
        height: 600px !important;
        min-height: 500px !important;
        max-height: 700px !important;
        overflow: hidden !important;
        margin-bottom: 0 !important;
    }

    /* الماب نفسها */
    .directorist-archive-map,
    .directorist-map-wrapper,
    .directorist-archive-map__container,
    .atbdp-map,
    #gmap,
    .gm-style {
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 100% !important;
        z-index: 1 !important;
    }

    /* ========== شريط البحث/الفلاتر - عائم فوق الماب ========== */
    .directorist-archive-contents .directorist-search-form,
    .directorist-content-area-with-map .directorist-search-form,
    .directorist-archive-map-wrapper .directorist-search-form,
    .directorist-map-wrapper .directorist-search-form {
        position: absolute !important;
        top: 15px !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        right: auto !important;
        bottom: auto !important;
        width: 700px !important;
        max-width: calc(100% - 30px) !important;
        background: #ffffff !important;
        border-radius: 8px !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.3) !important;
        padding: 12px 20px !important;
        z-index: 999 !important;
        display: flex !important;
        flex-wrap: wrap !important;
        align-items: center !important;
        gap: 10px !important;
        margin: 0 !important;
    }

    /* إخفاء العناوين */
    .directorist-search-form label,
    .directorist-search-form__title,
    .directorist-search-form h3,
    .directorist-search-form .search-title {
        display: none !important;
    }

    /* الحقول */
    .directorist-search-form .directorist-search-field,
    .directorist-search-form .form-group,
    .directorist-search-form > div {
        flex: 1 1 150px !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    .directorist-search-form input,
    .directorist-search-form select,
    .directorist-search-form .form-control {
        background: #f1f3f4 !important;
        border: none !important;
        border-radius: 24px !important;
        padding: 12px 20px !important;
        font-size: 14px !important;
        width: 100% !important;
        height: 44px !important;
        margin: 0 !important;
        box-sizing: border-box !important;
    }

    .directorist-search-form input:focus,
    .directorist-search-form select:focus {
        background: #fff !important;
        box-shadow: 0 1px 6px rgba(32,33,36,0.28) !important;
        outline: none !important;
    }

    /* زر البحث */
    .directorist-search-form button[type="submit"],
    .directorist-search-form .btn-primary,
    .directorist-search-form .directorist-btn {
        background: #1a73e8 !important;
        color: #fff !important;
        border: none !important;
        border-radius: 24px !important;
        padding: 12px 30px !important;
        font-weight: 500 !important;
        font-size: 14px !important;
        height: 44px !important;
        cursor: pointer !important;
        flex-shrink: 0 !important;
        margin: 0 !important;
    }

    .directorist-search-form button[type="submit"]:hover {
        background: #1557b0 !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.3) !important;
    }

    /* ========== منع التأثير على السكشن التالية ========== */
    .directorist-archive-contents.directorist-w-100,
    .directorist-content-area-with-map {
        contain: layout !important;
    }

    /* ========== Responsive ========== */
    @media (max-width: 768px) {
        .directorist-archive-contents.directorist-w-100,
        .directorist-content-area-with-map,
        .directorist-archive-map-wrapper {
            height: 450px !important;
            min-height: 400px !important;
        }

        .directorist-archive-contents .directorist-search-form,
        .directorist-content-area-with-map .directorist-search-form {
            width: calc(100% - 20px) !important;
            top: 10px !important;
            padding: 10px 15px !important;
            flex-direction: column !important;
            gap: 8px !important;
        }

        .directorist-search-form .directorist-search-field,
        .directorist-search-form .form-group,
        .directorist-search-form > div {
            flex: 1 1 100% !important;
            width: 100% !important;
        }

        .directorist-search-form button[type="submit"] {
            width: 100% !important;
        }
    }

    @media (max-width: 480px) {
        .directorist-archive-contents.directorist-w-100,
        .directorist-content-area-with-map {
            height: 400px !important;
        }
    }
    </style>
    <?php
}
'''

def main():
    print("="*60)
    print("Fixing Map - Final Version")
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

        # حذف كود الماب القديم
        pattern = r"\n// [-]+ تصميم الماب[^\n]*\nadd_action\('wp_head', 'aegad_map_fullwidth_design'[^\n]*\nfunction aegad_map_fullwidth_design\(\) \{.*?\n\}\n?"
        content = re.sub(pattern, '\n', content, flags=re.DOTALL)

        print(f"[INFO] After cleanup: {len(content)} chars")

        # إضافة الكود الجديد
        if content.strip().endswith('?>'):
            content = content.rstrip()[:-2].rstrip() + '\n' + MAP_CODE + '\n?>'
        else:
            content = content.rstrip() + '\n' + MAP_CODE

        print(f"[INFO] Final size: {len(content)} chars")

        # رفع الملف
        with sftp.file(functions_path, 'w') as f:
            f.write(content.encode('utf-8'))

        print("[SUCCESS] Updated!")

        sftp.close()
        client.close()

        print("\n" + "="*60)
        print("[DONE] Map fixed!")
        print("="*60)
        print("\nChanges:")
        print("- Map height: 600px (fixed)")
        print("- Filters: floating on top of map")
        print("- No effect on sections below")

    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
