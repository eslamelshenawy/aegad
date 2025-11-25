import paramiko
import re

HOST = '50.6.43.189'
USERNAME = 'pkqczdte'
KEY_FILE = 'E:/osama/id_rsa'
KEY_PASSWORD = '$wt%I&n!rwme'

# كود الماب المظبوط - النسخة النهائية
MAP_CODE = '''
// ----------- تصميم الماب - Google Maps Style -----------
add_action('wp_head', 'aegad_map_fullwidth_design', 999);
function aegad_map_fullwidth_design() {
    ?>
    <style type="text/css">
    /* ========== Aegad Map Section Fix ========== */

    /* قسم الماب الرئيسي */
    .directorist-archive-contents.directorist-w-100 {
        position: relative !important;
        width: 100% !important;
        height: 500px !important;
        overflow: hidden !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* الماب نفسها */
    .directorist-archive-map {
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 100% !important;
        z-index: 1 !important;
    }

    .directorist-archive-map__container,
    .directorist-archive-map__container > div,
    .gm-style {
        width: 100% !important;
        height: 100% !important;
    }

    /* ========== الفلاتر - شريط صغير أعلى اليسار ========== */
    .directorist-archive-contents.directorist-w-100 .directorist-search-form,
    .directorist-archive-contents .directorist-advanced-search,
    .directorist-archive-contents .directorist-filter-container {
        position: absolute !important;
        top: 15px !important;
        left: 15px !important;
        right: auto !important;
        bottom: auto !important;
        width: 320px !important;
        max-width: calc(100% - 30px) !important;
        max-height: 400px !important;
        overflow-y: auto !important;
        background: #fff !important;
        border-radius: 12px !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2) !important;
        padding: 15px !important;
        z-index: 100 !important;
        margin: 0 !important;
    }

    /* تصغير عنوان الفلاتر */
    .directorist-search-form .directorist-search-form__title,
    .directorist-search-form h3 {
        font-size: 16px !important;
        font-weight: 600 !important;
        margin-bottom: 10px !important;
        padding-bottom: 10px !important;
        border-bottom: 1px solid #eee !important;
    }

    /* الحقول */
    .directorist-search-form input,
    .directorist-search-form select {
        background: #f5f5f5 !important;
        border: 1px solid #ddd !important;
        border-radius: 8px !important;
        padding: 10px 12px !important;
        font-size: 13px !important;
        width: 100% !important;
        margin-bottom: 10px !important;
        box-sizing: border-box !important;
    }

    .directorist-search-form input:focus,
    .directorist-search-form select:focus {
        border-color: #1a73e8 !important;
        outline: none !important;
    }

    /* زر البحث */
    .directorist-search-form button[type="submit"],
    .directorist-search-form .btn-primary {
        background: #1a73e8 !important;
        color: #fff !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        font-size: 14px !important;
        width: 100% !important;
        cursor: pointer !important;
        margin-top: 5px !important;
    }

    .directorist-search-form button:hover {
        background: #1557b0 !important;
    }

    /* ========== إصلاح السكشن التالية ========== */

    /* إخفاء الفلاتر المكررة في السكشن التالية */
    .directorist-archive-contents.directorist-w-100 ~ * .directorist-search-form,
    .directorist-archive-contents.directorist-w-100 ~ * .directorist-advanced-search,
    section:not(:has(.directorist-archive-map)) .directorist-search-form:not(:first-of-type) {
        /* Keep visible but don't interfere */
    }

    /* التأكد من أن السكشن التالية تبدأ بعد الماب مباشرة */
    .directorist-archive-contents.directorist-w-100 {
        margin-bottom: 0 !important;
    }

    /* ========== Responsive ========== */
    @media (max-width: 768px) {
        .directorist-archive-contents.directorist-w-100 {
            height: 400px !important;
        }

        .directorist-archive-contents.directorist-w-100 .directorist-search-form {
            width: calc(100% - 20px) !important;
            left: 10px !important;
            top: 10px !important;
            max-height: 300px !important;
        }
    }
    </style>

    <script>
    // إصلاح الفلاتر بـ JavaScript
    document.addEventListener('DOMContentLoaded', function() {
        setTimeout(function() {
            // البحث عن قسم الماب
            var mapSection = document.querySelector('.directorist-archive-contents.directorist-w-100');
            if (mapSection) {
                // تحديد ارتفاع ثابت
                mapSection.style.height = '500px';
                mapSection.style.overflow = 'hidden';
                mapSection.style.position = 'relative';

                // التأكد من أن الفلاتر داخل قسم الماب
                var filters = mapSection.querySelector('.directorist-search-form');
                if (filters) {
                    filters.style.position = 'absolute';
                    filters.style.top = '15px';
                    filters.style.left = '15px';
                    filters.style.zIndex = '100';
                    filters.style.width = '320px';
                    filters.style.maxWidth = 'calc(100% - 30px)';
                }
            }
        }, 500);
    });
    </script>
    <?php
}
'''

def main():
    print("="*60)
    print("Fixing Map - Version 2")
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

        print("[SUCCESS] Updated!")

        sftp.close()
        client.close()

        print("\n[DONE] Map fixed!")

    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
