import paramiko
import re

HOST = '50.6.43.189'
USERNAME = 'pkqczdte'
KEY_FILE = 'E:/osama/id_rsa'
KEY_PASSWORD = '$wt%I&n!rwme'

MAP_CODE = '''
// ----------- تصميم الماب - Google Style Filters -----------
add_action('wp_head', 'aegad_map_fullwidth_design', 99999);
function aegad_map_fullwidth_design() {
    ?>
    <style type="text/css">
    /* ========== Aegad Map - Google Style ========== */

    /* 1. قسم الماب - Full Width */
    .directorist-archive-contents.directorist-w-100[data-atts*="map"] {
        position: relative !important;
        width: 100% !important;
        height: 100vh !important;
        max-height: 800px !important;
        min-height: 600px !important;
        overflow: hidden !important;
        margin: 0 !important;
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

    /* 2. إخفاء الفلاتر القديمة */
    .directorist-archive-contents.directorist-w-100[data-atts*="map"] .directorist-advanced-filter__top {
        display: none !important;
    }

    /* 3. إخفاء كل الفلاتر في Best Things والسكشنات الأخرى */
    .listing-with-sidebar__searchform,
    .listing-with-sidebar .directorist-advanced-filter__top,
    .listing-with-sidebar .directorist-advanced-filter,
    .listing-with-sidebar .directorist-advanced-filter__advanced,
    .listing-with-sidebar .directorist-search-form,
    .listing-with-sidebar__sidebar,
    .directorist-archive-sidebar,
    .directorist-search-form-wrap,
    .directorist-search-field-review,
    .directorist-search-field-tag,
    .directorist-advanced-filter__advanced,
    .directorist-archive-contents.directorist-w-100[data-atts*="grid"] .directorist-advanced-filter__top,
    .directorist-archive-contents.directorist-w-100[data-atts*="grid"] .directorist-advanced-filter__advanced,
    .directorist-archive-contents.directorist-w-100:not([data-atts*="map"]) .directorist-advanced-filter__top,
    .directorist-archive-contents.directorist-w-100:not([data-atts*="map"]) .directorist-advanced-filter__advanced {
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
        width: 0 !important;
        overflow: hidden !important;
        position: absolute !important;
        left: -9999px !important;
        opacity: 0 !important;
        pointer-events: none !important;
    }

    /* Best Things section فقط - مش الماب */
    .directorist-archive-contents[data-atts*="grid"] .listing-with-sidebar__contents,
    .directorist-archive-contents[data-atts*="grid"] .listing-with-sidebar__listing {
        width: 100% !important;
        max-width: 100% !important;
    }

    .directorist-archive-contents[data-atts*="grid"] .listing-with-sidebar__wrapper,
    .directorist-archive-contents[data-atts*="grid"] .listing-with-sidebar {
        display: block !important;
    }

    /* 5. إصلاح عرض الكروت في Best Things فقط */
    .directorist-archive-contents[data-atts*="grid"]:not([data-atts*="map"]) {
        height: auto !important;
        overflow: visible !important;
        position: relative !important;
    }

    .directorist-archive-contents[data-atts*="grid"]:not([data-atts*="map"]) .directorist-archive-items {
        position: relative !important;
        height: auto !important;
        overflow: visible !important;
    }

    /* 4. إخفاء Explore Hot Locations وكل اللي تحته */
    .elementor-element-1fcb1c0,
    .elementor-element-1fcb1c0 ~ section,
    .elementor-element-1fcb1c0 ~ .elementor-section {
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
        overflow: hidden !important;
    }

    /* ========== 4. شريط البحث Google Style ========== */
    #aegad-google-filters {
        position: absolute !important;
        top: 15px !important;
        left: 15px !important;
        right: 15px !important;
        z-index: 1000 !important;
        display: flex !important;
        align-items: center !important;
        gap: 10px !important;
        flex-wrap: nowrap !important;
    }

    /* Search Box */
    #aegad-google-filters .aegad-search-box {
        background: #fff !important;
        border-radius: 8px !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.3) !important;
        padding: 0 15px !important;
        height: 48px !important;
        display: flex !important;
        align-items: center !important;
        gap: 10px !important;
        min-width: 300px !important;
        max-width: 400px !important;
    }

    #aegad-google-filters .aegad-search-box input {
        border: none !important;
        outline: none !important;
        font-size: 15px !important;
        flex: 1 !important;
        background: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
        height: 100% !important;
    }

    #aegad-google-filters .aegad-search-box input::placeholder {
        color: #5f6368 !important;
    }

    #aegad-google-filters .aegad-search-icon {
        color: #4285f4 !important;
        font-size: 20px !important;
    }

    /* Filter Buttons Container */
    #aegad-google-filters .aegad-filter-buttons {
        display: flex !important;
        gap: 8px !important;
        overflow-x: auto !important;
        flex: 1 !important;
        scrollbar-width: none !important;
    }

    #aegad-google-filters .aegad-filter-buttons::-webkit-scrollbar {
        display: none !important;
    }

    /* Filter Buttons */
    #aegad-google-filters .aegad-filter-btn {
        background: #fff !important;
        border: none !important;
        border-radius: 20px !important;
        padding: 10px 16px !important;
        font-size: 14px !important;
        font-weight: 500 !important;
        color: #3c4043 !important;
        cursor: pointer !important;
        white-space: nowrap !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.2) !important;
        display: flex !important;
        align-items: center !important;
        gap: 6px !important;
        transition: all 0.2s !important;
    }

    #aegad-google-filters .aegad-filter-btn:hover {
        background: #f1f3f4 !important;
    }

    #aegad-google-filters .aegad-filter-btn.active {
        background: #e8f0fe !important;
        color: #1a73e8 !important;
    }

    #aegad-google-filters .aegad-filter-btn svg,
    #aegad-google-filters .aegad-filter-btn img {
        width: 18px !important;
        height: 18px !important;
    }

    /* ========== Responsive ========== */
    @media (max-width: 768px) {
        .directorist-archive-contents.directorist-w-100[data-atts*="map"] {
            height: 100vh !important;
            max-height: 600px !important;
            min-height: 400px !important;
        }

        #aegad-google-filters {
            flex-direction: column !important;
            align-items: stretch !important;
            gap: 8px !important;
        }

        #aegad-google-filters .aegad-search-box {
            min-width: 100% !important;
            max-width: 100% !important;
        }

        #aegad-google-filters .aegad-filter-buttons {
            padding-bottom: 5px !important;
        }
    }
    </style>

    <script>
    (function() {
        function createGoogleFilters() {
            // جرب عدة selectors للماب
            var mapContainer = document.querySelector('.directorist-archive-contents.directorist-w-100[data-atts*="map"]');

            // لو مش لاقي، جرب بطريقة تانية
            if (!mapContainer) {
                var allContainers = document.querySelectorAll('.directorist-archive-contents');
                allContainers.forEach(function(c) {
                    var atts = c.getAttribute('data-atts') || '';
                    if (atts.includes('map') || atts.includes('"view":"map"')) {
                        mapContainer = c;
                    }
                });
            }

            // لو لسه مش لاقي، جرب الماب مباشرة
            if (!mapContainer) {
                var mapElement = document.querySelector('.atbdp-body.atbdp-map');
                if (mapElement) {
                    mapContainer = mapElement.closest('.directorist-archive-contents') || mapElement.parentElement;
                }
            }

            if (!mapContainer || document.getElementById('aegad-google-filters')) return;

            // تأكد إن الكونتينر فيه position relative
            mapContainer.style.position = 'relative';

            // إنشاء شريط الفلاتر
            var filtersBar = document.createElement('div');
            filtersBar.id = 'aegad-google-filters';

            filtersBar.innerHTML = `
                <div class="aegad-search-box">
                    <span class="aegad-search-icon">🔍</span>
                    <input type="text" placeholder="Search location..." id="aegad-map-search">
                    <span style="cursor:pointer;color:#4285f4;">⬆️</span>
                </div>
                <div class="aegad-filter-buttons">
                    <button class="aegad-filter-btn" data-category="restaurants">🍽️ Restaurants</button>
                    <button class="aegad-filter-btn" data-category="hotels">🏨 Hotels</button>
                    <button class="aegad-filter-btn" data-category="outdoor-activities">📸 Activities</button>
                    <button class="aegad-filter-btn" data-category="shopping">🛍️ Shopping</button>
                    <button class="aegad-filter-btn" data-category="place">📍 Places</button>
                    <button class="aegad-filter-btn" data-category="store">🏪 Stores</button>
                </div>
            `;

            mapContainer.appendChild(filtersBar);

            // ========== تشغيل البحث ==========
            var searchInput = document.getElementById('aegad-map-search');
            var searchBtn = filtersBar.querySelector('.aegad-search-box span:last-child');

            function doSearch() {
                var query = searchInput.value.trim();
                if (query) {
                    // البحث في الموقع
                    window.location.href = '/search-result/?q=' + encodeURIComponent(query) + '&directory_type=general';
                }
            }

            searchInput.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    doSearch();
                }
            });

            searchBtn.addEventListener('click', doSearch);

            // ========== تشغيل فلاتر الكاتيجوري ==========
            var buttons = filtersBar.querySelectorAll('.aegad-filter-btn');
            buttons.forEach(function(btn) {
                btn.addEventListener('click', function() {
                    var category = this.dataset.category;

                    // إزالة active من كل الأزرار
                    buttons.forEach(function(b) { b.classList.remove('active'); });

                    // إضافة active للزر المضغوط
                    this.classList.add('active');

                    // الانتقال لصفحة الكاتيجوري
                    window.location.href = '/single-category/?atbdp_category=' + encodeURIComponent(category) + '&directory_type=general';
                });
            });

            // ========== البحث في الماب مباشرة (إذا كان OpenStreetMap) ==========
            function searchOnMap(query) {
                // محاولة البحث باستخدام Nominatim API
                if (window.L && window.aegadMap) {
                    fetch('https://nominatim.openstreetmap.org/search?format=json&q=' + encodeURIComponent(query + ' Saudi Arabia'))
                        .then(function(r) { return r.json(); })
                        .then(function(data) {
                            if (data && data[0]) {
                                var lat = parseFloat(data[0].lat);
                                var lon = parseFloat(data[0].lon);
                                window.aegadMap.setView([lat, lon], 14);
                            }
                        });
                }
            }

            console.log('AEGAD: Google-style filters with functionality created');
        }

        // ========== إضافة زر Explore All لسكشن Best Things ==========
        function addExploreAllButton() {
            // البحث عن سكشن Best Things to Do
            var headings = document.querySelectorAll('h2');
            var bestThingsSection = null;

            headings.forEach(function(h) {
                if (h.textContent.includes('Best Things to Do')) {
                    bestThingsSection = h.closest('.elementor-section') || h.closest('.elementor-top-section');
                }
            });

            if (!bestThingsSection || document.getElementById('aegad-explore-all-btn')) return;

            // إنشاء زر Explore All
            var btnContainer = document.createElement('div');
            btnContainer.id = 'aegad-explore-all-btn';
            btnContainer.style.cssText = 'text-align: center; padding: 30px 0 50px 0;';

            btnContainer.innerHTML = '<a href="/all-listings/" style="display: inline-block; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: #fff; padding: 16px 50px; border-radius: 50px; font-size: 17px; font-weight: 600; text-decoration: none; box-shadow: 0 4px 15px rgba(102,126,234,0.4); transition: all 0.3s; text-transform: uppercase; letter-spacing: 1px;">Explore All →</a>';

            // إضافة hover effect
            var link = btnContainer.querySelector('a');
            link.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-2px)';
                this.style.boxShadow = '0 6px 20px rgba(102,126,234,0.5)';
            });
            link.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0)';
                this.style.boxShadow = '0 4px 15px rgba(102,126,234,0.4)';
            });

            // إضافة الزر بعد السكشن
            bestThingsSection.parentNode.insertBefore(btnContainer, bestThingsSection.nextSibling);

            console.log('AEGAD: Explore All button added');
        }

        // إخفاء الفلاتر القديمة بشكل قوي
        function hideOldFilters() {
            var selectors = [
                '.listing-with-sidebar__searchform',
                '.listing-with-sidebar .directorist-advanced-filter__top',
                '.listing-with-sidebar .directorist-advanced-filter',
                '.listing-with-sidebar .directorist-advanced-filter__advanced',
                '.listing-with-sidebar .directorist-search-form',
                '.listing-with-sidebar__sidebar',
                '.directorist-archive-sidebar',
                '.directorist-search-form-wrap',
                '.directorist-search-field-review',
                '.directorist-search-field-tag',
                '.directorist-advanced-filter__advanced'
            ];

            selectors.forEach(function(sel) {
                var elements = document.querySelectorAll(sel);
                elements.forEach(function(el) {
                    el.style.cssText = 'display: none !important; visibility: hidden !important; height: 0 !important; width: 0 !important; overflow: hidden !important; position: absolute !important; left: -9999px !important;';
                });
            });

            // إخفاء الفلاتر في أي سكشن غير الماب
            var allFilters = document.querySelectorAll('.directorist-advanced-filter__top, .directorist-advanced-filter__advanced');
            allFilters.forEach(function(filter) {
                var parent = filter.closest('.directorist-archive-contents');
                if (parent) {
                    var atts = parent.getAttribute('data-atts') || '';
                    if (!atts.includes('"view":"map"')) {
                        filter.style.cssText = 'display: none !important; visibility: hidden !important; height: 0 !important; width: 0 !important;';
                    }
                } else {
                    // إخفاء أي فلتر خارج الماب
                    filter.style.cssText = 'display: none !important; visibility: hidden !important;';
                }
            });
        }

        function init() {
            hideOldFilters();
            createGoogleFilters();
            addExploreAllButton();
        }

        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', init);
        } else {
            init();
        }
        setTimeout(init, 500);
        setTimeout(init, 1500);
    })();
    </script>
    <?php
}
'''

def main():
    print("="*60)
    print("Map - Google Style Filters")
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
        print("\nGoogle-style filters:")
        print("- Search box on left")
        print("- Filter buttons: Restaurants, Hotels, Things to do, etc.")

        sftp.close()
        client.close()

    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()
