import paramiko
import re

HOST = '50.6.43.189'
USERNAME = 'pkqczdte'
KEY_FILE = 'E:/osama/id_rsa'
KEY_PASSWORD = '$wt%I&n!rwme'

# الكود النهائي المصحح
MAP_CODE = '''
// ----------- تصميم الماب - النسخة النهائية -----------
add_action('wp_head', 'aegad_map_fullwidth_design', 999);
function aegad_map_fullwidth_design() {
    ?>
    <style type="text/css">
    /* ========== إصلاح قسم الماب بالكامل ========== */

    /* الكونتينر الرئيسي - الماب والفلاتر معاً */
    .directorist-archive-contents.directorist-w-100 {
        display: block !important;
        position: relative !important;
        width: 100% !important;
        height: 550px !important;
        overflow: hidden !important;
        margin: 0 0 30px 0 !important;
        padding: 0 !important;
    }

    /* إخفاء الـ layout الافتراضي (grid/flex) */
    .directorist-archive-contents.directorist-w-100 > .directorist-row,
    .directorist-archive-contents.directorist-w-100 > .row {
        display: block !important;
        position: relative !important;
        width: 100% !important;
        height: 100% !important;
    }

    /* ========== الماب - Full Width ========== */
    .directorist-archive-contents.directorist-w-100 .directorist-archive-map,
    .directorist-archive-contents.directorist-w-100 .directorist-col-lg-8,
    .directorist-archive-contents.directorist-w-100 [class*="col-"][class*="-8"] {
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        bottom: 0 !important;
        width: 100% !important;
        height: 100% !important;
        max-width: 100% !important;
        flex: none !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    .directorist-archive-map__container,
    .directorist-archive-map__container > div {
        width: 100% !important;
        height: 100% !important;
    }

    /* ========== الفلاتر - عائمة فوق الماب ========== */
    .directorist-archive-contents.directorist-w-100 .directorist-col-lg-4,
    .directorist-archive-contents.directorist-w-100 [class*="col-"][class*="-4"],
    .directorist-archive-contents.directorist-w-100 .directorist-archive-sidebar,
    .directorist-archive-contents.directorist-w-100 .directorist-search-form {
        position: absolute !important;
        top: 15px !important;
        left: 15px !important;
        right: auto !important;
        bottom: auto !important;
        width: 300px !important;
        max-width: calc(100% - 30px) !important;
        max-height: calc(100% - 30px) !important;
        overflow-y: auto !important;
        background: #fff !important;
        border-radius: 12px !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.15) !important;
        padding: 15px !important;
        z-index: 100 !important;
        flex: none !important;
        margin: 0 !important;
    }

    /* تصغير الفلاتر */
    .directorist-archive-contents.directorist-w-100 .directorist-search-form__title {
        font-size: 16px !important;
        margin-bottom: 10px !important;
    }

    .directorist-archive-contents.directorist-w-100 .directorist-search-form input,
    .directorist-archive-contents.directorist-w-100 .directorist-search-form select {
        padding: 8px 12px !important;
        font-size: 13px !important;
        border-radius: 8px !important;
        margin-bottom: 8px !important;
    }

    .directorist-archive-contents.directorist-w-100 .directorist-search-form button {
        padding: 10px 15px !important;
        font-size: 13px !important;
        border-radius: 8px !important;
        background: #1a73e8 !important;
        color: #fff !important;
        border: none !important;
        width: 100% !important;
    }

    /* ========== إخفاء الفلاتر المكررة في السكشن التالية ========== */

    /* إخفاء أي فلاتر خارج قسم الماب */
    body:not(.single-at_biz_dir) .directorist-search-form:not(.directorist-archive-contents .directorist-search-form),
    .elementor-section .directorist-search-form,
    .directorist-archive-items ~ .directorist-search-form,
    section:has(.directorist-archive-items) .directorist-search-form {
        display: none !important;
    }

    /* إبقاء فلاتر الماب فقط */
    .directorist-archive-contents.directorist-w-100 .directorist-search-form {
        display: block !important;
    }

    /* ========== Responsive ========== */
    @media (max-width: 991px) {
        .directorist-archive-contents.directorist-w-100 {
            height: 450px !important;
        }

        .directorist-archive-contents.directorist-w-100 .directorist-col-lg-4,
        .directorist-archive-contents.directorist-w-100 .directorist-search-form {
            width: 280px !important;
        }
    }

    @media (max-width: 768px) {
        .directorist-archive-contents.directorist-w-100 {
            height: 400px !important;
        }

        .directorist-archive-contents.directorist-w-100 .directorist-col-lg-4,
        .directorist-archive-contents.directorist-w-100 .directorist-search-form {
            width: calc(100% - 20px) !important;
            left: 10px !important;
            top: 10px !important;
            max-height: 250px !important;
        }
    }
    </style>

    <script>
    document.addEventListener('DOMContentLoaded', function() {
        // إخفاء الفلاتر المكررة
        setTimeout(function() {
            var mapSection = document.querySelector('.directorist-archive-contents.directorist-w-100');
            if (!mapSection) return;

            // البحث عن كل الفلاتر في الصفحة
            var allFilters = document.querySelectorAll('.directorist-search-form');
            allFilters.forEach(function(filter, index) {
                // إبقاء الفلتر الأول فقط (اللي في الماب)
                if (!mapSection.contains(filter)) {
                    filter.style.display = 'none';
                }
            });

            console.log('AEGAD: Hidden duplicate filters');
        }, 1000);
    });
    </script>
    <?php
}
'''

def main():
    print("="*60)
    print("Final Map Fix - v3")
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

        print("\n" + "="*60)
        print("[DONE] Map fixed!")
        print("="*60)
        print("\nChanges:")
        print("1. Map fills full width")
        print("2. Filters float on top-left of map")
        print("3. Duplicate filters hidden")

    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
