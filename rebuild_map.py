import paramiko
import re

HOST = '50.6.43.189'
USERNAME = 'pkqczdte'
KEY_FILE = 'E:/osama/id_rsa'
KEY_PASSWORD = '$wt%I&n!rwme'

# الكود الجديد للماب فقط
MAP_CODE = '''
// ----------- تصميم الماب الجديد - Full Width مع فلاتر عائمة -----------
add_action('wp_head', 'aegad_map_fullwidth_design', 999);
function aegad_map_fullwidth_design() {
    ?>
    <style type="text/css">
    /* ========== Aegad Map - Full Width + Floating Filters ========== */

    /* الماب تملأ السكشن بالكامل */
    .directorist-map-wrapper,
    .directorist-archive-map,
    .directorist-search-map,
    .atbdp-map-wrapper,
    #directorist-map,
    .directorist-content-area-with-map,
    .directorist-archive-contents.directorist-w-100 {
        position: relative !important;
        width: 100vw !important;
        max-width: 100vw !important;
        margin-left: calc(-50vw + 50%) !important;
        margin-right: calc(-50vw + 50%) !important;
        padding: 0 !important;
        overflow: visible !important;
    }

    /* حجم الماب */
    .directorist-map-wrapper .gm-style,
    .directorist-map-wrapper > div,
    .atbdp-map,
    #gmap,
    .directorist-map,
    .directorist-archive-map__container,
    [id*="google-map"] {
        width: 100% !important;
        min-height: 600px !important;
        height: 70vh !important;
        max-height: 800px !important;
    }

    /* ========== الفلاتر العائمة ========== */
    .directorist-map-wrapper .directorist-search-form,
    .directorist-content-area-with-map .directorist-search-form,
    .directorist-archive-contents .directorist-search-form {
        position: absolute !important;
        top: 20px !important;
        right: 20px !important;
        left: auto !important;
        width: 360px !important;
        max-width: calc(100% - 40px) !important;
        background: rgba(255, 255, 255, 0.98) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border-radius: 20px !important;
        box-shadow: 0 10px 40px rgba(0,0,0,0.15), 0 2px 10px rgba(0,0,0,0.08) !important;
        padding: 24px !important;
        z-index: 1000 !important;
        border: 1px solid rgba(255,255,255,0.8) !important;
        max-height: calc(100vh - 150px) !important;
        overflow-y: auto !important;
        animation: aegadSlideIn 0.5s ease forwards !important;
    }

    /* Hover */
    .directorist-map-wrapper .directorist-search-form:hover {
        box-shadow: 0 15px 50px rgba(0,0,0,0.2), 0 5px 15px rgba(0,0,0,0.1) !important;
        transform: translateY(-2px) !important;
    }

    /* حقول الفلاتر */
    .directorist-search-form input,
    .directorist-search-form select,
    .directorist-search-form .form-control {
        background: #f9fafb !important;
        border: 2px solid #e5e7eb !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        font-size: 14px !important;
        width: 100% !important;
        margin-bottom: 12px !important;
    }

    .directorist-search-form input:focus,
    .directorist-search-form select:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 4px rgba(59,130,246,0.1) !important;
        outline: none !important;
    }

    /* زر البحث */
    .directorist-search-form button[type="submit"],
    .directorist-search-form .btn-primary {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%) !important;
        color: #fff !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 24px !important;
        font-weight: 600 !important;
        width: 100% !important;
        cursor: pointer !important;
        box-shadow: 0 4px 15px rgba(59,130,246,0.3) !important;
    }

    .directorist-search-form button[type="submit"]:hover {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%) !important;
        transform: translateY(-2px) !important;
    }

    /* Animation */
    @keyframes aegadSlideIn {
        from { opacity: 0; transform: translateX(30px); }
        to { opacity: 1; transform: translateX(0); }
    }

    /* Responsive */
    @media (max-width: 768px) {
        .directorist-map-wrapper .gm-style,
        .atbdp-map, #gmap, .directorist-map {
            min-height: 400px !important;
            height: 50vh !important;
        }

        .directorist-map-wrapper .directorist-search-form,
        .directorist-content-area-with-map .directorist-search-form {
            position: relative !important;
            top: auto !important;
            right: auto !important;
            width: 100% !important;
            max-width: 100% !important;
            margin: 0 !important;
            border-radius: 0 0 20px 20px !important;
        }
    }
    </style>
    <?php
}
'''

def main():
    print("="*60)
    print("Rebuilding Map Code ONLY - Safe Mode")
    print("="*60)

    try:
        key = paramiko.RSAKey.from_private_key_file(KEY_FILE, password=KEY_PASSWORD)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=HOST, username=USERNAME, pkey=key, timeout=15, allow_agent=False, look_for_keys=False)
        sftp = client.open_sftp()
        print("[SUCCESS] Connected!")

        theme_path = 'public_html/wp-content/themes/dlist/'

        # 1. حذف ملف CSS القديم فقط
        try:
            sftp.remove(theme_path + 'aegad-map-style.css')
            print("[DELETED] aegad-map-style.css")
        except:
            print("[INFO] aegad-map-style.css not found (OK)")

        # 2. قراءة functions.php
        functions_path = theme_path + 'functions.php'
        with sftp.file(functions_path, 'r') as f:
            content = f.read().decode('utf-8')

        original_size = len(content)
        print(f"[INFO] Original size: {original_size} chars")

        # 3. حذف فقط الأكواد المتعلقة بالماب

        # حذف دالة aegad_map_fullwidth_css إذا وجدت
        pattern1 = r"\n// [-]+ تحميل CSS الماب الجديد[^\n]*\nadd_action\('wp_enqueue_scripts', 'aegad_map_fullwidth_css'[^\n]*\nfunction aegad_map_fullwidth_css\(\) \{[^}]+\}\n?"
        content = re.sub(pattern1, '\n', content)

        # حذف دالة aegad_map_fullwidth_design إذا وجدت (النسخة القديمة)
        pattern2 = r"\n// [-]+ تصميم الماب الجديد[^\n]*\nadd_action\('wp_head', 'aegad_map_fullwidth_design'[^\n]*\nfunction aegad_map_fullwidth_design\(\) \{.*?\n\}\n?"
        content = re.sub(pattern2, '\n', content, flags=re.DOTALL)

        # حذف أي سطر enqueue للـ aegad-map-style
        content = re.sub(r"[^\n]*aegad-map-style[^\n]*\n?", '', content)

        # تنظيف الأسطر الفارغة الزائدة فقط (3 أو أكثر تصبح 2)
        content = re.sub(r'\n{4,}', '\n\n\n', content)

        new_size = len(content)
        print(f"[INFO] After cleanup: {new_size} chars")
        print(f"[INFO] Removed: {original_size - new_size} chars (map code only)")

        # 4. إضافة الكود الجديد قبل ?>
        if content.strip().endswith('?>'):
            content = content.rstrip()[:-2] + MAP_CODE + '\n?>'
        else:
            content = content.rstrip() + '\n' + MAP_CODE

        final_size = len(content)
        print(f"[INFO] Final size: {final_size} chars")

        # 5. رفع الملف المحدث
        with sftp.file(functions_path, 'w') as f:
            f.write(content.encode('utf-8'))

        print("[SUCCESS] functions.php updated!")

        # 6. التحقق من رفع الملف
        with sftp.file(functions_path, 'r') as f:
            verify = f.read().decode('utf-8')

        if 'aegad_map_fullwidth_design' in verify:
            print("[VERIFIED] New map code is in place!")
        else:
            print("[WARNING] Verification failed")

        sftp.close()
        client.close()

        print("\n" + "="*60)
        print("[DONE] Map code rebuilt - other code untouched!")
        print("="*60)

    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
