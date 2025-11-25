import paramiko
import re

HOST = '50.6.43.189'
USERNAME = 'pkqczdte'
KEY_FILE = 'E:/osama/id_rsa'
KEY_PASSWORD = '$wt%I&n!rwme'

MAP_CODE = '''
// ----------- تصميم الماب - v6 -----------
add_action('wp_head', 'aegad_map_fullwidth_design', 99999);
function aegad_map_fullwidth_design() {
    ?>
    <style type="text/css">
    /* ========== Aegad Map v6 ========== */

    /* 1. قسم الماب */
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

    /* 2. إخفاء كل الفلاتر في قسم الماب */
    .directorist-archive-contents.directorist-w-100[data-atts*="map"] .directorist-advanced-filter__top {
        display: none !important;
    }

    /* ========== 3. إخفاء كل الفلاتر في Best Things to Do ========== */

    /* إخفاء searchform */
    .listing-with-sidebar__searchform {
        display: none !important;
        visibility: hidden !important;
        width: 0 !important;
        height: 0 !important;
        overflow: hidden !important;
        position: absolute !important;
        left: -9999px !important;
    }

    /* إخفاء الفلاتر */
    .listing-with-sidebar .directorist-advanced-filter__top,
    .listing-with-sidebar .directorist-advanced-filter,
    .listing-with-sidebar .directorist-search-form {
        display: none !important;
        visibility: hidden !important;
        width: 0 !important;
        height: 0 !important;
        overflow: hidden !important;
        position: absolute !important;
        left: -9999px !important;
    }

    /* إخفاء sidebar */
    .listing-with-sidebar__sidebar,
    .directorist-archive-sidebar {
        display: none !important;
        visibility: hidden !important;
        width: 0 !important;
        height: 0 !important;
    }

    /* جعل المحتوى full width */
    .listing-with-sidebar__contents,
    .listing-with-sidebar__listing {
        width: 100% !important;
        max-width: 100% !important;
        flex: 1 !important;
    }

    .listing-with-sidebar__wrapper {
        display: block !important;
    }

    .listing-with-sidebar {
        display: block !important;
    }

    /* ========== Responsive ========== */
    @media (max-width: 768px) {
        .directorist-archive-contents.directorist-w-100[data-atts*="map"] {
            height: 400px !important;
        }
    }
    </style>

    <script>
    (function() {
        function hideAllFilters() {
            // إخفاء كل الفلاتر في الصفحة
            var selectors = [
                '.listing-with-sidebar__searchform',
                '.listing-with-sidebar .directorist-advanced-filter__top',
                '.listing-with-sidebar .directorist-advanced-filter',
                '.listing-with-sidebar__sidebar',
                '.directorist-archive-sidebar',
                '.directorist-archive-contents.directorist-w-100 .directorist-advanced-filter__top'
            ];

            selectors.forEach(function(sel) {
                var elements = document.querySelectorAll(sel);
                elements.forEach(function(el) {
                    el.style.cssText = 'display: none !important; visibility: hidden !important; width: 0 !important; height: 0 !important; position: absolute !important; left: -9999px !important;';
                });
            });

            console.log('AEGAD v6: All filters hidden');
        }

        // تشغيل عدة مرات
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', hideAllFilters);
        } else {
            hideAllFilters();
        }
        setTimeout(hideAllFilters, 300);
        setTimeout(hideAllFilters, 1000);
        setTimeout(hideAllFilters, 2000);
        setTimeout(hideAllFilters, 4000);
    })();
    </script>
    <?php
}
'''

def main():
    print("="*60)
    print("Map Fix v6 - Hide ALL filters")
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
        print("\nAll filters will be hidden:")
        print("- Map section filters")
        print("- Best Things sidebar/filters")

        sftp.close()
        client.close()

    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()
