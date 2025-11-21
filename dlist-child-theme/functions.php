<?php
/**
 * Dlist Child Theme Functions
 */

// ----------- تحذير تحديد الموقع الجغرافي -----------
add_action('wp_footer', 'aegad_geo_warning', 999);
function aegad_geo_warning() {
    if (is_admin()) return;
    ?>
    <script>
    (function() {
        
        if (window.aegadGeo) { console.log('AEGAD DEBUG: Already running, exiting'); return; }
        window.aegadGeo = true;
        

        function showWarn(isGranted) {
            
            var old = document.querySelector('.aegad-geo-beautiful');
            if (old) {
                
                old.remove();
            }
            var w = document.createElement('div');
            w.className = 'aegad-geo-beautiful';

            var msg = isGranted
                ? '<div class="aegad-geo-msg">نستخدم موقعك الدقيق لعرض الإعلانات القريبة منك</div><div class="aegad-geo-sub">We use your precise location to show nearby ads</div>'
                : '<div class="aegad-geo-msg">نستخدم موقعك التقريبي لعرض الإعلانات القريبة منك</div><div class="aegad-geo-sub">We use your approximate location to show nearby ads</div>';
            w.innerHTML = '<div class="aegad-geo-icon">📍</div>' +
                '<div class="aegad-geo-text">' +
                '<div class="aegad-geo-title">تنبيه الموقع</div>' +
                msg +
                '</div>';
            var s = document.createElement('style');
            s.textContent = '.aegad-geo-beautiful{position:fixed;top:20px;right:20px;background:linear-gradient(135deg,#ff6b6b,#ee5a6f);padding:20px 24px;border-radius:16px;box-shadow:0 12px 40px rgba(238,90,111,0.4);display:flex;align-items:center;gap:16px;max-width:400px;z-index:999999;animation:aegadGeoBounce 0.6s cubic-bezier(0.68,-0.55,0.265,1.55);border:2px solid rgba(255,255,255,0.3)}@keyframes aegadGeoBounce{0%{opacity:0;transform:translateY(-30px) scale(0.8)}100%{opacity:1;transform:translateY(0) scale(1)}}.aegad-geo-icon{font-size:32px;line-height:1;animation:aegadGeoPulse 2s ease-in-out infinite}@keyframes aegadGeoPulse{0%,100%{transform:scale(1)}50%{transform:scale(1.2)}}.aegad-geo-text{color:#fff;flex:1}.aegad-geo-title{font-size:16px;font-weight:700;margin-bottom:6px}.aegad-geo-msg{font-size:13px;margin-bottom:4px;opacity:0.95}.aegad-geo-sub{font-size:11px;opacity:0.8}@media(max-width:768px){.aegad-geo-beautiful{top:10px;right:10px;left:10px;max-width:none;padding:16px 18px}.aegad-geo-icon{font-size:28px}.aegad-geo-title{font-size:14px}.aegad-geo-msg{font-size:12px}.aegad-geo-sub{font-size:10px}}';
            document.head.appendChild(s);
            document.body.appendChild(w);
            // Removed: sessionStorage.setItem('aegad_geo_shown', 'yes');
            setTimeout(function() {
            
        
                w.style.transition = 'all 0.4s';
                w.style.opacity = '0';
                w.style.transform = 'translateY(-20px)';
                setTimeout(function() {
            
         w.remove(); }, 400);
            }, 12000);
        }

        setTimeout(function() {
            if (!navigator.geolocation) {  showWarn(false); return; }
            
            var responded = false;
            
            // Timeout: if user ignores for 8 seconds, show warning
            var t = setTimeout(function() {
                if (!responded) {
                    console.log('AEGAD: User ignored location request - showing warning');
                    showWarn(false);
                }
            }, 8000);
            
            navigator.geolocation.getCurrentPosition(
                function(p) {
                    // SUCCESS: User allowed location - NO warning needed!
                    responded = true;
                    clearTimeout(t);
                    sessionStorage.setItem('aegad_geo', 'granted');
                    // IMPORTANT: Save coordinates for map centering!
                    sessionStorage.setItem('aegad_lat', p.coords.latitude);
                    sessionStorage.setItem('aegad_lng', p.coords.longitude);
                    console.log('AEGAD: User allowed location - no warning shown');
                    console.log('AEGAD: Saved coordinates:', p.coords.latitude, p.coords.longitude);
                },
                function(e) {  
                    // ERROR: User denied location - show warning
                    responded = true;
                    clearTimeout(t);
                    console.log('AEGAD: User denied location - showing warning');
                    showWarn(false); 
                },
                {
                    timeout: 7000,  // Browser timeout: 7 seconds
                    enableHighAccuracy: false,
                    maximumAge: 0
                }
            );
        }, 2000);
    })();
    </script>
    <?php
}

// ----------- مبدل اللغة -----------
add_action('wp_footer', 'aegad_lang_switcher', 998);
function aegad_lang_switcher() {
    if (is_admin() || !function_exists('icl_get_languages')) return;
    $langs = icl_get_languages('skip_missing=0');
    if (empty($langs)) return;
    $current = ICL_LANGUAGE_CODE;
    $codes = array('ar'=>'AR','en'=>'EN','es'=>'ES','fr'=>'FR','ru'=>'RU','tr'=>'TR');
    $names = array('ar'=>'العربية','en'=>'English','es'=>'Español','fr'=>'Français','ru'=>'Русский','tr'=>'Türkçe');
    $current_code = isset($codes[$current]) ? $codes[$current] : strtoupper(substr($current,0,2));
    $current_name = isset($names[$current]) ? $names[$current] : $current;
    ?>
    <style>
        #aegad-lang{position:fixed;bottom:30px;left:30px;z-index:99999}
        #aegad-lang button{width:56px;height:56px;border:none;border-radius:14px;cursor:pointer;font-size:14px;font-weight:700;color:#fff;letter-spacing:0.5px;transition:all 0.3s cubic-bezier(0.4,0,0.2,1);background:linear-gradient(135deg,#667eea,#764ba2);box-shadow:0 8px 24px rgba(102,126,234,0.4);border:2px solid rgba(255,255,255,0.2);position:relative}
        #aegad-lang button:hover{transform:translateY(-4px) scale(1.05);box-shadow:0 10px 30px rgba(102,126,234,0.5)}
        #aegad-lang button:active{transform:translateY(-2px) scale(1)}
        #aegad-lang button::after{content:'▼';position:absolute;bottom:8px;right:8px;font-size:8px;opacity:0.7}
        #aegad-lang .menu{position:absolute;bottom:calc(100% + 12px);left:0;background:#fff;border-radius:14px;box-shadow:0 12px 48px rgba(0,0,0,0.15);padding:10px;min-width:180px;display:none;border:2px solid #f0f0f0}
        #aegad-lang.open .menu{display:block;animation:menuPop 0.3s cubic-bezier(0.68,-0.55,0.265,1.55)}
        @keyframes menuPop{from{opacity:0;transform:translateY(10px) scale(0.9)}to{opacity:1;transform:translateY(0) scale(1)}}
        #aegad-lang a{display:flex;align-items:center;justify-content:space-between;padding:12px 14px;text-decoration:none;color:#2d3748;font-size:14px;font-weight:500;border-radius:10px;transition:all 0.2s;margin-bottom:4px}
        #aegad-lang a:last-child{margin-bottom:0}
        #aegad-lang a:hover{color:#fff;transform:translateX(4px);background:linear-gradient(135deg,#667eea,#764ba2)}
        #aegad-lang .code{font-size:11px;font-weight:700;background:#f0f0f0;padding:5px 10px;border-radius:8px;letter-spacing:0.5px;transition:all 0.2s}
        #aegad-lang a:hover .code{background:rgba(255,255,255,0.25);color:#fff}
        @media(max-width:768px){#aegad-lang{bottom:20px;left:20px}#aegad-lang button{width:50px;height:50px;font-size:13px}}
    </style>
    <div id="aegad-lang">
        <button onclick="this.parentElement.classList.toggle('open')" title="<?php echo $current_name; ?>">
            <?php echo $current_code; ?>
        </button>
        <div class="menu">
            <?php foreach ($langs as $code => $lang): ?>
                <?php if ($code === $current) continue; ?>
                <a href="<?php echo esc_url($lang['url']); ?>">
                    <span><?php echo isset($names[$code]) ? $names[$code] : $lang['native_name']; ?></span>
                    <span class="code"><?php echo isset($codes[$code]) ? $codes[$code] : strtoupper(substr($code,0,2)); ?></span>
                </a>
            <?php endforeach; ?>
        </div>
    </div>
    <script>
        document.addEventListener('click', function(e) {
            var b = document.getElementById('aegad-lang');
            if (b && !b.contains(e.target)) b.classList.remove('open');
            var link = e.target.closest('#aegad-lang a[href]');
            if (link) {
                var h = link.getAttribute('href');
                var l = '';
                if (h.indexOf('/ar/') > -1 || h.indexOf('/ar') > -1) l = 'ar';
                else if (h.indexOf('/en/') > -1 || h.indexOf('/en') > -1) l = 'en';
                else if (h.indexOf('/es/') > -1 || h.indexOf('/es') > -1) l = 'es';
                else if (h.indexOf('/fr/') > -1 || h.indexOf('/fr') > -1) l = 'fr';
                else if (h.indexOf('/ru/') > -1 || h.indexOf('/ru') > -1) l = 'ru';
                else if (h.indexOf('/tr/') > -1 || h.indexOf('/tr') > -1) l = 'tr';
                if (l) document.cookie = 'aegad_manual_lang=' + l + '; path=/; max-age=2592000; secure; samesite=lax';
            }
        });
    </script>
    <?php
}

// ----------- تفعيل إعادة التوجيه عبر WPML -----------
add_action('init', 'aegad_enable_wpml_redirect', 1);
function aegad_enable_wpml_redirect() {
    if (!function_exists('icl_get_languages')) return;
    $s = get_option('icl_sitepress_settings');
    if ($s && is_array($s)) {
        if (!isset($s['language_negotiation_type']) || $s['language_negotiation_type'] != 1) {
            $s['language_negotiation_type'] = 1;
            update_option('icl_sitepress_settings', $s);
        }
    }
}

// ----------- كشف اللغة الذكي واحترام التحديد اليدوي -----------
add_action('init', 'aegad_smart_detection', 5);
function aegad_smart_detection() {
    if (is_admin()
        || (defined('DOING_AJAX') && DOING_AJAX)
        || (defined('REST_REQUEST') && REST_REQUEST)
        || !function_exists('icl_get_languages')
    ) return;

    $curr = defined('ICL_LANGUAGE_CODE') ? ICL_LANGUAGE_CODE : '';
    $manual = isset($_COOKIE['aegad_manual_lang']) ? $_COOKIE['aegad_manual_lang'] : '';

    // تحديث قاعدة البيانات للغة الحالية
    if ($curr) {
        $s = get_option('icl_sitepress_settings');
        if ($s && is_array($s) && isset($s['default_language']) && $s['default_language'] !== $curr) {
            $s['default_language'] = $curr;
            update_option('icl_sitepress_settings', $s);
        }
    }

    if ($manual) return; // إذا حدد المستخدم اللغة يدوياً لا تعيد التوجيه

    if (isset($_COOKIE['wpml_browser_redirect_test'])) return;

    // جلب لغة المتصفح
    $bl = '';
    if (isset($_SERVER['HTTP_ACCEPT_LANGUAGE'])) {
        if (preg_match('/^([a-z]{2})/i', $_SERVER['HTTP_ACCEPT_LANGUAGE'], $m)) {
            $bl = strtolower($m[1]);
        }
    }
    if (!$bl) return;

    $sup = array('ar','en','es','fr','ru','tr');
    if (!in_array($bl, $sup)) $bl = 'en';

    $s = get_option('icl_sitepress_settings');
    if ($s && is_array($s) && isset($s['default_language']) && $s['default_language'] !== $bl) {
        $s['default_language'] = $bl;
        update_option('icl_sitepress_settings', $s);
    }

    // إعادة التوجيه إذا اختلفت اللغة الحالية عن المتصفح
    if ($curr !== $bl) {
        $ls = icl_get_languages('skip_missing=0');
        if (isset($ls[$bl]['url'])) {
            setcookie('wpml_browser_redirect_test', 1, time() + 86400, '/', '', true, false);
            wp_redirect($ls[$bl]['url'], 302);
            exit;
        }
    }
}

// ----------- إعداد سياسات المتصفح الآمنة (مع السماح للـ geolocation) -----------
add_action('send_headers', 'aegad_set_permissions_policy');
function aegad_set_permissions_policy() {
    if (!headers_sent()) {
        header("Permissions-Policy: accelerometer=(), autoplay=(), camera=(), encrypted-media=(), fullscreen=(), geolocation=*, gyroscope=(), magnetometer=(), microphone=(), midi=(), payment=(), sync-xhr=(), usb=()");
    }
}

// AffiliateWP Auto-Activation (runs once)
add_action('init', 'aegad_activate_affiliatewp', 999);
function aegad_activate_affiliatewp() {
    // Check if already activated
    if (get_option('aegad_affiliatewp_activated')) {
        return; // Already done
    }

    // Activate the plugin
    if (!is_plugin_active('affiliate-wp/affiliate-wp.php')) {
        $result = activate_plugin('affiliate-wp/affiliate-wp.php');
        if (!is_wp_error($result)) {
            // Plugin activated successfully

            // Set basic settings
            $settings = array(
                'referral_rate' => '10',
                'referral_rate_type' => 'percentage',
                'currency' => 'USD',
                'cookie_exp' => '30',
                'allow_affiliate_registration' => '1',
                'require_approval' => '0',
                'referral_var' => 'ref',
                'currency_position' => 'before'
            );

            update_option('affwp_settings', $settings);

            // Mark as activated
            update_option('aegad_affiliatewp_activated', '1');
        }
    } else {
        // Already active, just mark as done
        update_option('aegad_affiliatewp_activated', '1');
    }
}

// AffiliateWP Page Creator (runs once after activation)
add_action('init', 'aegad_create_affiliate_pages', 1000);
function aegad_create_affiliate_pages() {
    // Only run if plugin is active
    if (!function_exists('affiliate_wp') || get_option('aegad_aff_pages_created')) {
        return;
    }

    // Create Registration Page
    if (!get_page_by_title('Affiliate Registration', OBJECT, 'page')) {
        wp_insert_post(array(
            'post_title' => 'Affiliate Registration',
            'post_content' => '[affiliate_registration]',
            'post_status' => 'publish',
            'post_type' => 'page',
            'post_author' => 1,
            'comment_status' => 'closed'
        ));
    }

    // Create Dashboard Page
    if (!get_page_by_title('Affiliate Area', OBJECT, 'page')) {
        $area_id = wp_insert_post(array(
            'post_title' => 'Affiliate Area',
            'post_content' => '[affiliate_area]',
            'post_status' => 'publish',
            'post_type' => 'page',
            'post_author' => 1,
            'comment_status' => 'closed'
        ));

        // Update settings with affiliate area page
        $settings = get_option('affwp_settings', array());
        $settings['affiliates_page'] = $area_id;
        update_option('affwp_settings', $settings);
    }

    // Mark as done
    update_option('aegad_aff_pages_created', '1');
}


// Aegad - Map User Location (Waits for Google Maps)
add_action('wp_head', 'aegad_map_location_early', 1);
function aegad_map_location_early() {
    if (is_admin()) return;
    ?>
    <script>
// Aegad - Wait for Google Maps then Override
(function() {
        
    console.log('AEGAD: Waiting for Google Maps...');

    var userLat = null;
    var userLng = null;
    var mapsCentered = [];

    // Get location
    var savedLat = sessionStorage.getItem('aegad_lat');
    var savedLng = sessionStorage.getItem('aegad_lng');

    if (savedLat && savedLng) {
        userLat = parseFloat(savedLat);
        userLng = parseFloat(savedLng);
        console.log('AEGAD: Saved location:', userLat, userLng);
    }

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            userLat = position.coords.latitude;
            userLng = position.coords.longitude;
            sessionStorage.setItem('aegad_lat', userLat);
            sessionStorage.setItem('aegad_lng', userLng);
            console.log('AEGAD: Fresh location:', userLat, userLng);
        });
    }

    // Function to center map
    function centerMap(map, id) {
        if (!map || !userLat || !userLng) return false;
        if (mapsCentered.indexOf(id) >= 0) return false;

        try {
            var userLoc = new google.maps.LatLng(userLat, userLng);
            map.setCenter(userLoc);
            map.setZoom(14);

            new google.maps.Marker({
                position: userLoc,
                map: map,
                title: 'موقعك | Your Location',
                icon: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
                zIndex: 999999,
                animation: google.maps.Animation.DROP
            });

            mapsCentered.push(id);
            console.log('AEGAD: ✓✓✓ Map centered! ID:', id);
            return true;
        } catch(e) {
            console.log('AEGAD: Error:', e);
            return false;
        }
    }

    // Wait for Google Maps to load
    function waitForGoogleMaps() {
        if (typeof google !== 'undefined' && google.maps && google.maps.Map) {
            console.log('AEGAD: ✓ Google Maps loaded!');
            setupMapOverride();
        } else {
            setTimeout(waitForGoogleMaps, 100);
        }
    }

    // Setup the override
    function setupMapOverride() {
        var OrigMap = google.maps.Map;
        var mapCount = 0;

        google.maps.Map = function(elem, opts) {
            mapCount++;
            var mapId = 'gmap_' + mapCount;

            console.log('AEGAD: ⚡ New map created!', mapId);

            // Create map with original
            var map = new OrigMap(elem, opts);

            // Store reference
            elem.__aegadMap = map;
            window['__aegadMap' + mapCount] = map;

            // SMART DETECTION: Check if this is a search results map
            var isSearchPage = false;
            var url = window.location.href;
            var pathname = window.location.pathname;

            // Check URL for search parameters (query string)
            if (url.indexOf('?') > -1) {
                var searchParams = ['q=', 'in_loc=', 'search=', 'location=', 'place=', 's='];
                for (var i = 0; i < searchParams.length; i++) {
                    if (url.indexOf(searchParams[i]) > -1) {
                        isSearchPage = true;
                        console.log('AEGAD: Search page detected (param: ' + searchParams[i] + ')');
                        break;
                    }
                }
            }

            // Also check for path-based search URLs
            if (!isSearchPage) {
                var searchPaths = ['/search/', '/location/', '/in-location/', '/all-locations/'];
                for (var i = 0; i < searchPaths.length; i++) {
                    if (pathname.indexOf(searchPaths[i]) > -1) {
                        isSearchPage = true;
                        console.log('AEGAD: Search page detected (path: ' + searchPaths[i] + ')');
                        break;
                    }
                }
            }

            // Check if map already has a center defined (from search results)
            var hasCustomCenter = false;
            if (opts && opts.center) {
                hasCustomCenter = true;
                console.log('AEGAD: Map has custom center:', opts.center);
            }

            // ONLY center the map if:
            // 1. NOT a search page
            // 2. Map doesn't have custom center
            // 3. User is on homepage or general page
            var shouldCenter = !isSearchPage && !hasCustomCenter;

            if (shouldCenter) {
                // Center it after creation
                setTimeout(function() {
                    if (userLat && userLng) {
                        console.log('AEGAD: Centering map', mapId);
                        centerMap(map, mapId);
                    } else {
                        console.log('AEGAD: No user location yet, will retry...');
                        // Retry after user grants permission
                        setTimeout(function() {
                            if (userLat && userLng) {
                                centerMap(map, mapId);
                            }
                        }, 2000);
                    }
                }, 800);
            } else {
                console.log('AEGAD: Skip auto-center (search results map)', mapId);
            }

            return map;
        };

        google.maps.Map.prototype = OrigMap.prototype;
        console.log('AEGAD: ✓ Map constructor overridden!');
    }

    // Start waiting
    waitForGoogleMaps();

    // Also scan for existing maps periodically (but skip on search pages)
    var scanAttempts = 0;
    var scanInterval = setInterval(function() {
        
        scanAttempts++;

        if (scanAttempts > 15 || mapsCentered.length > 0) {
            clearInterval(scanInterval);
            return;
        }

        // Skip scanning on search pages
        var url = window.location.href;
        var pathname = window.location.pathname;
        
        // Check query parameters
        if (url.indexOf('?') > -1) {
            var searchParams = ['q=', 'in_loc=', 'search=', 'location=', 'place=', 's='];
            for (var i = 0; i < searchParams.length; i++) {
                if (url.indexOf(searchParams[i]) > -1) {
                    console.log('AEGAD: Skipping scan (search page - param)');
                    clearInterval(scanInterval);
                    return;
                }
            }
        }
        
        // Check path-based search URLs
        var searchPaths = ['/search/', '/location/', '/in-location/', '/all-locations/'];
        for (var i = 0; i < searchPaths.length; i++) {
            if (pathname.indexOf(searchPaths[i]) > -1) {
                console.log('AEGAD: Skipping scan (search page - path)');
                clearInterval(scanInterval);
                return;
            }
        }

        if (!userLat || !userLng || typeof google === 'undefined' || !google.maps) {
            return;
        }

        console.log('AEGAD: Scan #' + scanAttempts);

        // Scan window for map objects
        for (var key in window) {
            try {
                var obj = window[key];
                if (obj && typeof obj === 'object' &&
                    typeof obj.setCenter === 'function' &&
                    typeof obj.setZoom === 'function' &&
                    typeof obj.panTo === 'function') {

                    centerMap(obj, 'scan_' + key);
                }
            } catch(e) {}
        }
    }, 1500);

})();

    </script>
    <?php
}


// ----------- إخفاء العناصر المكررة في الصفحة الرئيسية -----------
add_action('wp_head', 'aegad_hide_duplicates', 99999);
function aegad_hide_duplicates() {
    if (!is_front_page()) return;
    ?>
    <style>
    /* تحسين عرض الصفحة الرئيسية بعد حذف العناصر */
    
    /* التأكد من أن الـ sections تاخد العرض الكامل بشكل جميل */
    body.home .elementor-section {
        width: 100% !important;
        max-width: 100% !important;
    }
    
    /* تحسين المسافات بين الـ sections */
    body.home .elementor-section:not(:last-child) {
        margin-bottom: 60px !important;
    }
    
    /* تحسين عرض الفلتر المتبقي */
    body.home .elementor-widget-directorist_search_listing {
        width: 100% !important;
        max-width: 1200px !important;
        margin: 0 auto !important;
    }
    
    /* تنظيف أي فراغات فاضية بعد حذف العناصر */
    body.home .elementor-column:empty,
    body.home .elementor-widget:empty {
        display: none !important;
    }
    
    /* تحسين responsive للموبايل */
    @media (max-width: 768px) {
        body.home .elementor-section:not(:last-child) {
            margin-bottom: 40px !important;
        }
        
        body.home .elementor-widget-directorist_search_listing {
            padding: 15px !important;
        }
    }
    
    /* تحسين العرض بعد حذف Most Popular Categories */
    body.home .elementor-top-section {
        transition: all 0.3s ease !important;
    }
    
    /* تحسين عرض "Best Things to Do" بعد حذف الفلاتر */
    body.home .aegad-filters-removed {
        padding-top: 40px !important;
        padding-bottom: 40px !important;
    }
    
    body.home .aegad-filters-removed .elementor-container {
        max-width: 100% !important;
        margin: 0 auto !important;
    }
    
    /* إخفاء كل الفلاتر في قسم Best Things to Do - حل نهائي */
    /* Target widget 7fd6f4bb which contains the listings */
    body.home .elementor-element-7fd6f4bb .directorist-search-form,
    body.home .elementor-element-7fd6f4bb .directorist-basic-search,
    body.home .elementor-element-7fd6f4bb .directorist-advanced-search,
    body.home .elementor-element-7fd6f4bb .listing-with-sidebar__searchform,
    body.home .elementor-element-7fd6f4bb .listing-with-sidebar__sidebar,
    body.home .elementor-element-7fd6f4bb aside,
    body.home .elementor-element-7fd6f4bb form.directorist-search-form {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        height: 0 !important;
        width: 0 !important;
        overflow: hidden !important;
        position: absolute !important;
        left: -99999px !important;
        z-index: -9999 !important;
    }
    
    /* Also target by section */
    body.home section.elementor-element-36380079 .directorist-search-form,
    body.home section.elementor-element-36380079 .listing-with-sidebar__sidebar,
    body.home section.elementor-element-36380079 aside {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        height: 0 !important;
        max-height: 0 !important;
    }
/* إخفاء القسم المكرر بالكامل - section 5a4edcde */    body.home .elementor-element-5a4edcde,    body.home section.elementor-element-5a4edcde {        display: none !important;        visibility: hidden !important;        opacity: 0 !important;        height: 0 !important;        max-height: 0 !important;        overflow: hidden !important;        position: absolute !important;        left: -99999px !important;        z-index: -9999 !important;    }    /* إخفاء widget 7592cdb0 داخل هذا القسم */    body.home .elementor-element-7592cdb0,    body.home .elementor-element-83abe9c {        display: none !important;        visibility: hidden !important;        opacity: 0 !important;        height: 0 !important;        max-height: 0 !important;        overflow: hidden !important;    }
    
    /* جعل قسم الـ listings كامل العرض */
    body.home .elementor-element-7fd6f4bb .listing-with-sidebar__listing,
    body.home .elementor-element-7fd6f4bb .listing-with-sidebar__contents {
        width: 100% !important;
        max-width: 100% !important;
        flex: 1 !important;
        margin: 0 !important;
    }
    
    body.home .elementor-element-7fd6f4bb .listing-with-sidebar {
        display: block !important;
    }
    
    body.home .elementor-element-7fd6f4bb .listing-with-sidebar__wrapper {
        display: block !important;
    }
    
    /* Force listings to be full width */
    body.home .elementor-element-7fd6f4bb .directorist-archive-items {
        width: 100% !important;
    }
    
    /* تحسين عرض العناوين في القسم */
    body.home .aegad-filters-removed .elementor-heading-title {
        text-align: center !important;
        margin-bottom: 30px !important;
    }
    
    /* تحسين عرض المحتوى بعد حذف الفلاتر */
    body.home .aegad-filters-removed .elementor-widget-wrap {
        justify-content: center !important;
        gap: 20px !important;
    }
    
    @media (max-width: 768px) {
        body.home .aegad-filters-removed {
            padding-top: 30px !important;
            padding-bottom: 30px !important;
        }
    }
    </style>
    <script>
    (function() {
        function removeUnwantedElements() {
            var count = 0;
            
            // 1. REMOVE duplicate search filters (keep first only) - NOT just hide
            var filters = document.querySelectorAll('.elementor-widget-directorist_search_listing');
            if (filters.length > 1) {
                for (var i = 1; i < filters.length; i++) {
                    // Remove the widget completely from DOM
                    if (filters[i] && filters[i].parentNode) {
                        filters[i].parentNode.removeChild(filters[i]);
                        count++;
                    }
                }
                console.log('AEGAD: DELETED ' + count + ' duplicate filters from DOM');
            }
            
            // 2. REMOVE "Most Popular Categories" section completely
            var allHeadings = document.querySelectorAll('h1, h2, h3, h4, h5, h6, .elementor-heading-title');
            for (var i = 0; i < allHeadings.length; i++) {
                var heading = allHeadings[i];
                var text = heading.textContent || heading.innerText || '';
                
                // Check if heading contains "Most Popular Categories"
                if (text.trim() === 'Most Popular Categories' || text.indexOf('Most Popular Categories') > -1) {
                    // Find the closest section container and remove it
                    var container = heading.closest('.elementor-section');
                    
                    if (container && container.parentNode) {
                        container.parentNode.removeChild(container);
                        console.log('AEGAD: DELETED "Most Popular Categories" section from DOM');
                        break;
                    }
                }
            }
            
            // 3. REMOVE ALL filters inside "Best Things to Do in the City" section
            var bestThingsHeadings = document.querySelectorAll('h1, h2, h3, h4, h5, h6, .elementor-heading-title');
            for (var i = 0; i < bestThingsHeadings.length; i++) {
                var heading = bestThingsHeadings[i];
                var text = heading.textContent || heading.innerText || '';
                
                // Check if heading contains "Best Things to Do"
                if (text.indexOf('Best Things to Do') > -1) {
                    // Find the section containing this heading
                    var section = heading.closest('.elementor-section');
                    
                    if (section) {
                        var removedCount = 0;
                        
                        // Remove ALL types of search forms and filters
                        // 1. Remove directorist search forms (basic + advanced)
                        var searchForms = section.querySelectorAll('.directorist-search-form, .directorist-basic-search, .directorist-advanced-search, .listing-with-sidebar__searchform');
                        for (var j = 0; j < searchForms.length; j++) {
                            if (searchForms[j] && searchForms[j].parentNode) {
                                searchForms[j].parentNode.removeChild(searchForms[j]);
                                removedCount++;
                            }
                        }
                        
                        // 2. Remove sidebars with filters
                        var sidebars = section.querySelectorAll('.listing-with-sidebar__sidebar, aside');
                        for (var j = 0; j < sidebars.length; j++) {
                            if (sidebars[j] && sidebars[j].parentNode) {
                                sidebars[j].parentNode.removeChild(sidebars[j]);
                                removedCount++;
                            }
                        }
                        
                        // 3. Remove any remaining filter widgets
                        var widgets = section.querySelectorAll('.elementor-widget-directorist_search_listing');
                        for (var j = 0; j < widgets.length; j++) {
                            if (widgets[j] && widgets[j].parentNode) {
                                widgets[j].parentNode.removeChild(widgets[j]);
                                removedCount++;
                            }
                        }
                        
                        if (removedCount > 0) {
                            console.log('AEGAD: DELETED ' + removedCount + ' filter elements from "Best Things to Do" section');
                            
                            // Fix layout: add class and fix width
                            section.classList.add('aegad-filters-removed');
                            
                            // Make listing section full width after removing sidebar
                            var listingSection = section.querySelector('.listing-with-sidebar__listing');
                            if (listingSection) {
                                listingSection.style.width = '100%';
                                listingSection.style.maxWidth = '100%';
                            }
                        }
                        break;
                    }
                }
            }
// 4. REMOVE duplicate section 5a4edcde completely            var duplicateSection = document.querySelector('.elementor-element-5a4edcde');            if (duplicateSection && duplicateSection.parentNode) {                duplicateSection.parentNode.removeChild(duplicateSection);                console.log('AEGAD: DELETED duplicate section 5a4edcde from DOM');            }
        }

        // Run multiple times to catch dynamic content
        removeUnwantedElements();
        
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', removeUnwantedElements);
        }
        
        window.addEventListener('load', function() {
            setTimeout(removeUnwantedElements, 100);
            setTimeout(removeUnwantedElements, 500);
            setTimeout(removeUnwantedElements, 1000);
        });
        
        if (window.elementorFrontend) {
            elementorFrontend.hooks.addAction('frontend/element_ready/widget', removeUnwantedElements);
        }
    })();
    </script>
    <?php
}

// إضافة CSS إضافي في الـ footer لضمان التطبيق
add_action('wp_footer', 'aegad_force_hide_filters_footer', 99999);
function aegad_force_hide_filters_footer() {
    if (!is_front_page()) return;
    ?>
    <style>
    /* CSS نهائي في الـ footer - أقوى من أي شيء */
    .elementor-element-7fd6f4bb .directorist-search-form,
    .elementor-element-7fd6f4bb .listing-with-sidebar__sidebar,
    .elementor-element-36380079 .directorist-search-form,
    .elementor-element-36380079 .listing-with-sidebar__sidebar {
        display: none !important;
    }
    
    .elementor-element-7fd6f4bb .listing-with-sidebar__listing {
        width: 100% !important;
    }
    </style>
    <script>
    // JavaScript backup لحذف الفلاتر
    (function() {
        setTimeout(function() {
            var widget = document.querySelector('.elementor-element-7fd6f4bb');
            if (widget) {
                var forms = widget.querySelectorAll('.directorist-search-form, .listing-with-sidebar__sidebar, aside');
                forms.forEach(function(el) {
                    if (el) el.remove();
                });
                console.log('AEGAD FOOTER: Removed filters from Best Things section');
            }
// أيضا حذف القسم المكرر 5a4edcde            var dupSection = document.querySelector('.elementor-element-5a4edcde');            if (dupSection && dupSection.parentNode) {                dupSection.parentNode.removeChild(dupSection);                console.log('AEGAD FOOTER: Removed duplicate section 5a4edcde');            }
        }, 2000);
    })();
    </script>
    <?php
}

?>