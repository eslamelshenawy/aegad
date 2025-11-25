import paramiko

# Server credentials
HOST = '50.6.43.189'
USERNAME = 'pkqczdte'
KEY_FILE = 'E:/osama/id_rsa'
KEY_PASSWORD = '$wt%I&n!rwme'

# CSS content for map
MAP_CSS = '''/* ========== Aegad Map Section - Full Width Design ========== */
/* الماب تملأ السكشن بالكامل + فلاتر عائمة أعلى اليمين */

/* السكشن الذي يحتوي على الماب - Full Width */
.directorist-map-wrapper,
.directorist-archive-map,
.directorist-search-map,
.atbdp-map-wrapper,
#directorist-map,
.atbdp-body .map-wrapper,
[class*="map-section"],
.elementor-widget-directorist_search_listing_map,
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

/* الماب نفسها تملأ السكشن بالكامل */
.directorist-map-wrapper .gm-style,
.directorist-map-wrapper > div,
.atbdp-map,
#gmap,
.directorist-map,
.directorist-archive-map .gm-style,
[id*="google-map"],
.google-map-container,
.directorist-archive-map__container {
    width: 100% !important;
    min-height: 600px !important;
    height: 70vh !important;
    max-height: 800px !important;
}

/* ========== الفلاتر العائمة - Floating Filters Card ========== */

/* تحويل الفلاتر لـ card عائم أبيض أعلى اليمين */
.directorist-map-wrapper .directorist-search-form,
.directorist-map-wrapper .directorist-basic-search,
.directorist-map-wrapper .directorist-advanced-search,
.directorist-content-area-with-map .directorist-search-form,
.directorist-archive-contents .directorist-search-form,
.atbdp-body .directorist-search-form,
.aegad-floating-filters {
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
    box-shadow:
        0 10px 40px rgba(0, 0, 0, 0.15),
        0 2px 10px rgba(0, 0, 0, 0.08),
        inset 0 1px 0 rgba(255, 255, 255, 0.9) !important;
    padding: 24px !important;
    z-index: 1000 !important;
    border: 1px solid rgba(255, 255, 255, 0.8) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    max-height: calc(100vh - 150px) !important;
    overflow-y: auto !important;
}

/* Hover effect للـ card */
.directorist-map-wrapper .directorist-search-form:hover,
.directorist-content-area-with-map .directorist-search-form:hover {
    box-shadow:
        0 15px 50px rgba(0, 0, 0, 0.2),
        0 5px 15px rgba(0, 0, 0, 0.1),
        inset 0 1px 0 rgba(255, 255, 255, 1) !important;
    transform: translateY(-2px) !important;
}

/* عنوان الفلاتر */
.directorist-search-form__title,
.directorist-search-form h3,
.directorist-search-form .search-title {
    font-size: 18px !important;
    font-weight: 700 !important;
    color: #1f2937 !important;
    margin-bottom: 20px !important;
    padding-bottom: 15px !important;
    border-bottom: 2px solid #f3f4f6 !important;
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
    transition: all 0.2s ease !important;
    width: 100% !important;
    margin-bottom: 12px !important;
}

.directorist-search-form input:focus,
.directorist-search-form select:focus {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1) !important;
    background: #ffffff !important;
    outline: none !important;
}

/* زر البحث في الفلاتر */
.directorist-search-form button[type="submit"],
.directorist-search-form .btn-primary,
.directorist-search-form .search-submit {
    background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 14px 24px !important;
    font-weight: 600 !important;
    font-size: 15px !important;
    width: 100% !important;
    cursor: pointer !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3) !important;
    margin-top: 8px !important;
}

.directorist-search-form button[type="submit"]:hover {
    background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4) !important;
}

/* Labels في الفلاتر */
.directorist-search-form label {
    font-size: 13px !important;
    font-weight: 600 !important;
    color: #4b5563 !important;
    margin-bottom: 6px !important;
    display: block !important;
}

/* Scrollbar للفلاتر */
.directorist-search-form::-webkit-scrollbar {
    width: 6px !important;
}

.directorist-search-form::-webkit-scrollbar-track {
    background: #f3f4f6 !important;
    border-radius: 10px !important;
}

.directorist-search-form::-webkit-scrollbar-thumb {
    background: #d1d5db !important;
    border-radius: 10px !important;
}

/* ========== Responsive Design للماب ========== */

@media (max-width: 768px) {
    .directorist-map-wrapper .gm-style,
    .atbdp-map,
    #gmap,
    .directorist-map {
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

@media (max-width: 480px) {
    .directorist-map-wrapper .directorist-search-form {
        padding: 16px !important;
    }

    .directorist-search-form input,
    .directorist-search-form select {
        padding: 10px 14px !important;
    }
}

/* Animation للـ card عند التحميل */
@keyframes aegadSlideIn {
    from {
        opacity: 0;
        transform: translateX(30px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

.directorist-map-wrapper .directorist-search-form {
    animation: aegadSlideIn 0.5s cubic-bezier(0.4, 0, 0.2, 1) forwards !important;
}

/* ========== نهاية تحسينات الماب ========== */
'''

def main():
    print("="*60)
    print("Uploading Map CSS to Server")
    print("="*60)

    try:
        # Load SSH key
        print("Loading SSH key...")
        key = paramiko.RSAKey.from_private_key_file(KEY_FILE, password=KEY_PASSWORD)
        print("[SUCCESS] RSA key loaded")

        # Connect
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        print(f"Connecting to {HOST}...")
        client.connect(
            hostname=HOST,
            username=USERNAME,
            pkey=key,
            timeout=15,
            allow_agent=False,
            look_for_keys=False
        )
        print("[SUCCESS] Connected!")

        # Open SFTP
        sftp = client.open_sftp()
        print("[SUCCESS] SFTP session opened")

        # Path to child theme on server
        theme_path = 'public_html/wp-content/themes/dlist-developer-developer-developer-developer/dlist-developer/'

        # Check if dlist child theme exists
        try:
            sftp.listdir(theme_path)
            print(f"[INFO] Theme found at: {theme_path}")
        except:
            # Try alternative paths
            alt_paths = [
                'public_html/wp-content/themes/dlist-developer/',
                'public_html/wp-content/themes/dlist/',
                'public_html/wp-content/themes/dlist-child/',
            ]
            for alt in alt_paths:
                try:
                    sftp.listdir(alt)
                    theme_path = alt
                    print(f"[INFO] Theme found at: {theme_path}")
                    break
                except:
                    continue

        # Upload CSS file
        css_path = theme_path + 'aegad-map-style.css'
        print(f"Uploading to: {css_path}")

        with sftp.file(css_path, 'w') as f:
            f.write(MAP_CSS)

        print("[SUCCESS] aegad-map-style.css uploaded!")

        # Now we need to add enqueue in functions.php
        # First, download functions.php
        functions_path = theme_path + 'functions.php'
        print(f"Reading: {functions_path}")

        with sftp.file(functions_path, 'r') as f:
            functions_content = f.read().decode('utf-8')

        # Check if already enqueued
        if 'aegad-map-style' in functions_content:
            print("[INFO] aegad-map-style already enqueued in functions.php")
        else:
            # Find the enqueue function and add our CSS
            old_enqueue = "wp_enqueue_style('dlist-child-style', get_stylesheet_uri(), array(), filemtime(get_stylesheet_directory() . '/style.css'));"
            new_enqueue = """wp_enqueue_style('dlist-child-style', get_stylesheet_uri(), array(), filemtime(get_stylesheet_directory() . '/style.css'));
    // تحميل CSS الماب الجديد - Full Width Map
    wp_enqueue_style('aegad-map-style', get_stylesheet_directory_uri() . '/aegad-map-style.css', array(), filemtime(get_stylesheet_directory() . '/aegad-map-style.css'));"""

            if old_enqueue in functions_content:
                functions_content = functions_content.replace(old_enqueue, new_enqueue)

                # Upload modified functions.php
                with sftp.file(functions_path, 'w') as f:
                    f.write(functions_content.encode('utf-8'))

                print("[SUCCESS] functions.php updated with new CSS enqueue!")
            else:
                print("[WARNING] Could not find enqueue function to modify")
                print("[INFO] You may need to manually add the CSS enqueue")

        # Close connections
        sftp.close()
        client.close()

        print("\n" + "="*60)
        print("[SUCCESS] All done!")
        print("="*60)
        print("\nMap CSS uploaded successfully!")
        print("- Full width map section")
        print("- Floating white filter card on top-right")
        print("- Clean design with shadow")

    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
