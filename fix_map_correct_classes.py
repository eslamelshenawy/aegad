import paramiko
import re

HOST = '50.6.43.189'
USERNAME = 'pkqczdte'
KEY_FILE = 'E:/osama/id_rsa'
KEY_PASSWORD = '$wt%I&n!rwme'

# الكود الصحيح بالـ classes الفعلية
MAP_CODE = '''
// ----------- تصميم الماب - النسخة الصحيحة -----------
add_action('wp_head', 'aegad_map_fullwidth_design', 999);
function aegad_map_fullwidth_design() {
    ?>
    <style type="text/css">
    /* ========== Aegad Map - Correct Classes ========== */

    /* الكونتينر الرئيسي للماب */
    .directorist-archive-contents.directorist-w-100 {
        position: relative !important;
        width: 100% !important;
        height: 550px !important;
        overflow: hidden !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* قسم الماب */
    .directorist-archive-items.directorist-archive-map-view {
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        bottom: 0 !important;
        width: 100% !important;
        height: 100% !important;
        z-index: 1 !important;
    }

    /* الماب نفسها */
    .atbdp-body.atbdp-map {
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    /* ========== الفلاتر - عائمة فوق الماب ========== */
    .directorist-archive-contents.directorist-w-100 .directorist-advanced-filter__top {
        position: absolute !important;
        top: 15px !important;
        left: 15px !important;
        right: auto !important;
        bottom: auto !important;
        width: 320px !important;
        max-width: calc(100% - 30px) !important;
        max-height: calc(100% - 30px) !important;
        overflow-y: auto !important;
        background: #fff !important;
        border-radius: 12px !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2) !important;
        padding: 15px !important;
        z-index: 100 !important;
    }

    /* تحسين شكل الفلاتر */
    .directorist-advanced-filter__top .directorist-advanced-filter__advanced {
        display: flex !important;
        flex-direction: column !important;
        gap: 10px !important;
    }

    .directorist-advanced-filter__top .directorist-advanced-filter__advanced__element {
        margin: 0 !important;
    }

    .directorist-advanced-filter__top input,
    .directorist-advanced-filter__top select {
        padding: 10px 12px !important;
        font-size: 13px !important;
        border-radius: 8px !important;
        border: 1px solid #ddd !important;
        background: #f8f8f8 !important;
    }

    .directorist-advanced-filter__top input:focus,
    .directorist-advanced-filter__top select:focus {
        border-color: #1a73e8 !important;
        outline: none !important;
    }

    /* زر البحث */
    .directorist-advanced-filter__action button,
    .directorist-advanced-filter__action .directorist-btn {
        background: #1a73e8 !important;
        color: #fff !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 12px 20px !important;
        font-size: 14px !important;
        cursor: pointer !important;
        width: 100% !important;
    }

    .directorist-advanced-filter__action button:hover {
        background: #1557b0 !important;
    }

    /* ========== إخفاء الفلاتر المكررة ========== */

    /* إخفاء أي فلاتر خارج قسم الماب الرئيسي */
    .elementor-section .directorist-advanced-filter__top,
    .elementor-widget .directorist-advanced-filter__top:not(.directorist-archive-contents .directorist-advanced-filter__top) {
        display: none !important;
    }

    /* ========== Responsive ========== */
    @media (max-width: 768px) {
        .directorist-archive-contents.directorist-w-100 {
            height: 450px !important;
        }

        .directorist-archive-contents.directorist-w-100 .directorist-advanced-filter__top {
            width: calc(100% - 20px) !important;
            left: 10px !important;
            top: 10px !important;
            max-height: 300px !important;
        }
    }
    </style>
    <?php
}
'''

def main():
    print("="*60)
    print("Fixing Map with Correct Classes")
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

        with sftp.file(functions_path, 'r') as f:
            content = f.read().decode('utf-8')

        print(f"[INFO] Original: {len(content)} chars")

        # حذف الكود القديم
        pattern = r"\n// [-]+ تصميم الماب[^\n]*\nadd_action\('wp_head', 'aegad_map_fullwidth_design'[^\n]*\nfunction aegad_map_fullwidth_design\(\) \{.*?\n\}\n?"
        content = re.sub(pattern, '\n', content, flags=re.DOTALL)

        print(f"[INFO] After cleanup: {len(content)} chars")

        # إضافة الكود الجديد
        if content.strip().endswith('?>'):
            content = content.rstrip()[:-2].rstrip() + '\n' + MAP_CODE + '\n?>'
        else:
            content = content.rstrip() + '\n' + MAP_CODE

        print(f"[INFO] Final: {len(content)} chars")

        with sftp.file(functions_path, 'w') as f:
            f.write(content.encode('utf-8'))

        print("[SUCCESS] Updated with correct classes!")

        sftp.close()
        client.close()

        print("\n" + "="*60)
        print("[DONE]")
        print("="*60)
        print("\nClasses targeted:")
        print("- .directorist-archive-contents.directorist-w-100")
        print("- .directorist-archive-items.directorist-archive-map-view")
        print("- .atbdp-body.atbdp-map")
        print("- .directorist-advanced-filter__top")

    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
