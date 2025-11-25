import paramiko
import re

HOST = '50.6.43.189'
USERNAME = 'pkqczdte'
KEY_FILE = 'E:/osama/id_rsa'
KEY_PASSWORD = '$wt%I&n!rwme'

MAP_CODE = '''
// ----------- تصميم الماب - v4 -----------
add_action('wp_head', 'aegad_map_fullwidth_design', 999);
function aegad_map_fullwidth_design() {
    ?>
    <style type="text/css">
    /* ========== Aegad Map - v4 ========== */

    /* الكونتينر الرئيسي */
    .directorist-archive-contents.directorist-w-100 {
        position: relative !important;
        width: 100% !important;
        height: 550px !important;
        overflow: hidden !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* قسم الماب - Full Width */
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

    .atbdp-body.atbdp-map {
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    /* ========== الفلاتر فوق الماب ========== */
    .directorist-archive-contents.directorist-w-100 .directorist-advanced-filter__top {
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
        box-shadow: 0 2px 10px rgba(0,0,0,0.2) !important;
        padding: 15px !important;
        z-index: 100 !important;
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
    }

    /* تحسين الفلاتر */
    .directorist-archive-contents.directorist-w-100 .directorist-advanced-filter__advanced {
        display: flex !important;
        flex-direction: column !important;
        gap: 10px !important;
    }

    .directorist-archive-contents.directorist-w-100 .directorist-advanced-filter__advanced__element {
        margin: 0 !important;
    }

    .directorist-archive-contents.directorist-w-100 .directorist-advanced-filter__top input,
    .directorist-archive-contents.directorist-w-100 .directorist-advanced-filter__top select {
        padding: 10px 12px !important;
        font-size: 13px !important;
        border-radius: 8px !important;
        border: 1px solid #ddd !important;
        background: #f8f8f8 !important;
        width: 100% !important;
    }

    .directorist-archive-contents.directorist-w-100 .directorist-advanced-filter__action button {
        background: #1a73e8 !important;
        color: #fff !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 12px 20px !important;
        width: 100% !important;
        cursor: pointer !important;
    }

    /* ========== إخفاء الفلاتر في Best Things to Do ========== */

    /* إخفاء كل الفلاتر خارج قسم الماب */
    .directorist-advanced-filter__top:not(.directorist-archive-contents.directorist-w-100 .directorist-advanced-filter__top) {
        display: none !important;
    }

    /* إخفاء الفلاتر في elementor sections */
    .elementor-section .directorist-advanced-filter__top,
    .elementor-widget .directorist-advanced-filter__top {
        display: none !important;
    }

    /* إخفاء الفلاتر بجانب الكروت */
    .directorist-archive-items:not(.directorist-archive-map-view) .directorist-advanced-filter__top,
    .directorist-archive-items:not(.directorist-archive-map-view) ~ .directorist-advanced-filter__top,
    .listing-with-sidebar .directorist-advanced-filter__top,
    .listing-with-sidebar__sidebar {
        display: none !important;
    }

    /* إعادة إظهار فلاتر الماب فقط */
    .directorist-archive-contents.directorist-w-100 .directorist-advanced-filter__top {
        display: block !important;
    }

    /* ========== Responsive ========== */
    @media (max-width: 768px) {
        .directorist-archive-contents.directorist-w-100 {
            height: 400px !important;
        }

        .directorist-archive-contents.directorist-w-100 .directorist-advanced-filter__top {
            width: calc(100% - 20px) !important;
            left: 10px !important;
            top: 10px !important;
            max-height: 250px !important;
        }
    }
    </style>

    <script>
    document.addEventListener('DOMContentLoaded', function() {
        setTimeout(function() {
            // إخفاء الفلاتر المكررة
            var mapContainer = document.querySelector('.directorist-archive-contents.directorist-w-100');
            var allFilters = document.querySelectorAll('.directorist-advanced-filter__top');

            allFilters.forEach(function(filter) {
                if (mapContainer && mapContainer.contains(filter)) {
                    // إبقاء فلاتر الماب
                    filter.style.display = 'block';
                } else {
                    // إخفاء الباقي
                    filter.style.display = 'none';
                }
            });

            // إخفاء sidebar filters
            var sidebars = document.querySelectorAll('.listing-with-sidebar__sidebar, .directorist-archive-sidebar');
            sidebars.forEach(function(sidebar) {
                sidebar.style.display = 'none';
            });

            console.log('AEGAD: Filters fixed');
        }, 500);
    });
    </script>
    <?php
}
'''

def main():
    print("="*60)
    print("Map Fix v4 - Show filters on map, hide elsewhere")
    print("="*60)

    try:
        key = paramiko.RSAKey.from_private_key_file(KEY_FILE, password=KEY_PASSWORD)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=HOST, username=USERNAME, pkey=key, timeout=15, allow_agent=False, look_for_keys=False)
        sftp = client.open_sftp()
        print("[SUCCESS] Connected!")

        functions_path = 'public_html/wp-content/themes/dlist/functions.php'

        with sftp.file(functions_path, 'r') as f:
            content = f.read().decode('utf-8')

        print(f"[INFO] Original: {len(content)} chars")

        pattern = r"\n// [-]+ تصميم الماب[^\n]*\nadd_action\('wp_head', 'aegad_map_fullwidth_design'[^\n]*\nfunction aegad_map_fullwidth_design\(\) \{.*?\n\}\n?"
        content = re.sub(pattern, '\n', content, flags=re.DOTALL)

        if content.strip().endswith('?>'):
            content = content.rstrip()[:-2].rstrip() + '\n' + MAP_CODE + '\n?>'
        else:
            content = content.rstrip() + '\n' + MAP_CODE

        print(f"[INFO] Final: {len(content)} chars")

        with sftp.file(functions_path, 'w') as f:
            f.write(content.encode('utf-8'))

        print("[SUCCESS] Updated!")
        print("\nChanges:")
        print("1. Filters visible on map (top-left)")
        print("2. Filters hidden in 'Best Things' section")

        sftp.close()
        client.close()

    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()
