import paramiko
import re

HOST = '50.6.43.189'
USERNAME = 'pkqczdte'
KEY_FILE = 'E:/osama/id_rsa'
KEY_PASSWORD = '$wt%I&n!rwme'

MAP_CODE = '''
// ----------- تصميم الماب - v5 Final -----------
add_action('wp_head', 'aegad_map_fullwidth_design', 99999);
function aegad_map_fullwidth_design() {
    ?>
    <style type="text/css">
    /* ========== Aegad Map v5 - Final Fix ========== */

    /* 1. الماب Full Width */
    .directorist-archive-contents.directorist-w-100[data-atts*="map"] {
        position: relative !important;
        width: 100% !important;
        height: 550px !important;
        overflow: hidden !important;
        margin: 0 0 20px 0 !important;
        padding: 0 !important;
    }

    .directorist-archive-contents.directorist-w-100[data-atts*="map"] .directorist-archive-items {
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 100% !important;
    }

    .directorist-archive-contents.directorist-w-100[data-atts*="map"] .atbdp-body.atbdp-map {
        width: 100% !important;
        height: 100% !important;
    }

    /* 2. الفلاتر فوق الماب */
    .directorist-archive-contents.directorist-w-100[data-atts*="map"] .directorist-advanced-filter__top {
        position: absolute !important;
        top: 15px !important;
        left: 15px !important;
        width: 300px !important;
        max-height: 500px !important;
        overflow-y: auto !important;
        background: #fff !important;
        border-radius: 12px !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2) !important;
        padding: 15px !important;
        z-index: 999 !important;
    }

    .directorist-archive-contents.directorist-w-100[data-atts*="map"] .directorist-advanced-filter__top input,
    .directorist-archive-contents.directorist-w-100[data-atts*="map"] .directorist-advanced-filter__top select {
        padding: 8px 12px !important;
        border-radius: 6px !important;
        border: 1px solid #ddd !important;
        font-size: 13px !important;
    }

    .directorist-archive-contents.directorist-w-100[data-atts*="map"] .directorist-advanced-filter__action button {
        background: #1a73e8 !important;
        color: #fff !important;
        border: none !important;
        border-radius: 6px !important;
        padding: 10px 16px !important;
        width: 100% !important;
    }

    /* ========== 3. إخفاء الفلاتر في Best Things to Do ========== */

    /* إخفاء listing-with-sidebar__searchform */
    .listing-with-sidebar__searchform {
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
        width: 0 !important;
        overflow: hidden !important;
    }

    /* إخفاء الفلاتر داخل listing-with-sidebar */
    .listing-with-sidebar .directorist-advanced-filter__top {
        display: none !important;
        visibility: hidden !important;
    }

    /* جعل المحتوى يأخذ العرض الكامل */
    .listing-with-sidebar__contents {
        width: 100% !important;
        max-width: 100% !important;
    }

    .listing-with-sidebar__wrapper {
        display: block !important;
    }

    /* ========== Responsive ========== */
    @media (max-width: 768px) {
        .directorist-archive-contents.directorist-w-100[data-atts*="map"] {
            height: 400px !important;
        }

        .directorist-archive-contents.directorist-w-100[data-atts*="map"] .directorist-advanced-filter__top {
            width: calc(100% - 20px) !important;
            left: 10px !important;
            max-height: 250px !important;
        }
    }
    </style>

    <script>
    (function() {
        function fixFilters() {
            // إخفاء الفلاتر في listing-with-sidebar
            var sidebarFilters = document.querySelectorAll('.listing-with-sidebar .directorist-advanced-filter__top, .listing-with-sidebar__searchform');
            sidebarFilters.forEach(function(el) {
                el.style.cssText = 'display: none !important; visibility: hidden !important;';
            });

            // التأكد من ظهور فلاتر الماب
            var mapFilters = document.querySelectorAll('.directorist-archive-contents.directorist-w-100 .directorist-advanced-filter__top');
            mapFilters.forEach(function(el) {
                if (!el.closest('.listing-with-sidebar')) {
                    el.style.cssText = 'display: block !important; visibility: visible !important;';
                }
            });

            console.log('AEGAD: Filters fixed via JS');
        }

        // تشغيل عدة مرات للتأكد
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', fixFilters);
        } else {
            fixFilters();
        }
        setTimeout(fixFilters, 500);
        setTimeout(fixFilters, 1500);
        setTimeout(fixFilters, 3000);
    })();
    </script>
    <?php
}
'''

def main():
    print("="*60)
    print("Map Fix v5 - Final")
    print("="*60)

    try:
        key = paramiko.RSAKey.from_private_key_file(KEY_FILE, password=KEY_PASSWORD)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=HOST, username=USERNAME, pkey=key, timeout=15, allow_agent=False, look_for_keys=False)
        sftp = client.open_sftp()
        print("[OK] Connected!")

        functions_path = 'public_html/wp-content/themes/dlist/functions.php'

        with sftp.file(functions_path, 'r') as f:
            content = f.read().decode('utf-8')

        print(f"Original: {len(content)}")

        pattern = r"\n// [-]+ تصميم الماب[^\n]*\nadd_action\('wp_head', 'aegad_map_fullwidth_design'[^\n]*\nfunction aegad_map_fullwidth_design\(\) \{.*?\n\}\n?"
        content = re.sub(pattern, '\n', content, flags=re.DOTALL)

        if content.strip().endswith('?>'):
            content = content.rstrip()[:-2].rstrip() + '\n' + MAP_CODE + '\n?>'
        else:
            content = content.rstrip() + '\n' + MAP_CODE

        print(f"Final: {len(content)}")

        with sftp.file(functions_path, 'w') as f:
            f.write(content.encode('utf-8'))

        print("[OK] Updated!")
        print("\nTargets:")
        print("- .listing-with-sidebar__searchform (HIDE)")
        print("- .listing-with-sidebar .directorist-advanced-filter__top (HIDE)")

        sftp.close()
        client.close()

    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()
