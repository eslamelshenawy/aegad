<?php
/**
 * @author  WpWax
 * @since   1.7.05
 * @version 1.0
 */

use Elementor\Plugin;

function dlist_setup() {

	require_once get_template_directory() . '/inc/customizer.php';
	require_once get_template_directory() . '/inc/comment_form.php';
	require_once get_template_directory() . '/inc/dlist-helper.php';

	if ( did_action('directorist_loaded') ) {
		require_once get_template_directory() . '/inc/migration.php';
		require_once get_template_directory() . '/migration/class-migration-v8.php';
		require_once get_template_directory() . '/inc/directorist-support.php';
		require_once get_template_directory() . '/inc/directorist-notice.php';
		require_once get_template_directory() . '/updater/theme-updater-admin.php';
		require_once get_template_directory() . '/inc/updater-config.php';
	}

	require_once get_template_directory() . '/lib/tgm/plugin_ac.php';

	load_theme_textdomain( 'dlist', get_theme_file_path( '/languages' ) );

	add_image_size( 'dlist_blog', 730, 413, true );
	add_image_size( 'dlist_blog_grid', 350, 300, true );
	add_image_size( 'dlist_related_blog', 223, 136, true );

	add_theme_support( 'automatic-feed-links' );
	add_theme_support( 'title-tag' );
	add_theme_support( 'post-thumbnails' );
	add_theme_support( 'woocommerce' );
	add_theme_support( 'wc-product-gallery-lightbox' );
	add_theme_support( 'wc-product-gallery-zoom' );
	add_theme_support( 'wc-product-gallery-slider' );
	add_theme_support( 'editor-styles' );
	add_editor_style( 'style-editor.css' );
	remove_theme_support( 'widgets-block-editor' );

	register_nav_menus(
		array(
			'primary' => esc_html__( 'Primary Menu', 'dlist' ),
		)
	);

	add_theme_support(
		'html5',
		array(
			'search-form',
			'comment-form',
			'comment-list',
			'gallery',
			'caption',
		)
	);

	add_theme_support(
		'custom-background',
		apply_filters(
			'dlist_custom_background_args',
			array(
				'default-color' => 'fff',
				'default-image' => '',
			)
		)
	);

	add_theme_support( 'customize-selective-refresh-widgets' );

	add_theme_support(
		'custom-logo',
		array(
			'height'      => 40,
			'width'       => 120,
			'flex-width'  => true,
			'flex-height' => true,
		)
	);
}

add_action( 'after_setup_theme', 'dlist_setup' );

if ( ! function_exists( 'dlist_content_width' ) ) {
	function dlist_content_width() {
		$GLOBALS['content_width'] = apply_filters( 'dlist_content_width', 640 );
	}

	add_action( 'after_setup_theme', 'dlist_content_width', 0 );
}

/**
 * Register widget area.
 */

function dlist_sidebar_register() {

	register_sidebar(
		array(
			'name'          => esc_html__( 'All Listing Widgets ', 'dlist' ),
			'id'            => 'all_listing',
			'description'   => esc_html__( 'It will display on the left side of the All Listing element.', 'dlist' ),
			'before_widget' => '<div class="widget atbd_widget %2$s">',
			'after_widget'  => '</div>',
			'before_title'  => '<div class="widget-header atbd_widget_title"><h6 class="widget-title">',
			'after_title'   => '</h6></div>',
		)
	);

	if( class_exists( 'WooCommerce' ) ){
		register_sidebar(
			array(
				'name'          => esc_html__( 'Shop Page Widgets', 'dlist' ),
				'id'            => 'shop_sidebar',
				'description'   => esc_html__( 'Appears in the shop page sidebar.', 'dlist' ),
				'before_widget' => '<div class="widget widget-wrapper %2$s"><div class="widget-default">',
				'after_widget'  => '</div></div>',
				'before_title'  => '<div class="widget-header"><h6 class="widget-title">',
				'after_title'   => '</h6> </div>',
			)
		);
	}

	register_sidebar(
		array(
			'name'          => esc_html__( 'Blog Widgets', 'dlist' ),
			'id'            => 'blog_sidebar',
			'description'   => esc_html__( 'Appears in the blog page sidebar.', 'dlist' ),
			'before_widget' => '<div class="widget widget-wrapper %2$s"><div class="widget-default">',
			'after_widget'  => '</div></div>',
			'before_title'  => '<div class="widget-header"><h6 class="widget-title">',
			'after_title'   => '</h6> </div>',
		)
	);

	register_sidebar(
		array(
			'name'          => esc_html__( 'Page Widgets', 'dlist' ),
			'id'            => 'page_sidebar',
			'description'   => esc_html__( 'Appears in the page sidebar.', 'dlist' ),
			'before_widget' => '<div class="widget widget-wrapper %2$s"><div class="widget-default">',
			'after_widget'  => '</div></div>',
			'before_title'  => '<div class="widget-header"><h6 class="widget-title">',
			'after_title'   => '</h6></div>',
		)
	);

	$footer_widget_titles = array(
		'1' => esc_html__( 'Footer 1', 'dlist' ),
		'2' => esc_html__( 'Footer 2', 'dlist' ),
		'3' => esc_html__( 'Footer 3', 'dlist' ),
		'4' => esc_html__( 'Footer 4', 'dlist' ),
	);

	foreach ( $footer_widget_titles as $id => $name ) {
		register_sidebar(
			array(
				'name'          => $name,
				'id'            => 'footer_sidebar_' . $id,
				'before_widget' => '<div class="widget %2$s">',
				'after_widget'  => '</div>',
				'before_title'  => '<h2 class="widget-title">',
				'after_title'   => '</h2>',
			)
		);
	}
}

add_action( 'widgets_init', 'dlist_sidebar_register' );

/*
=====================================================
Register custom fonts.
====================================================== = */
function dlist_fonts_url() {
	$fonts_url = '';
	$fonts     = array();
	$subsets   = 'arabic';

	if ( 'off' !== _x( 'on', 'DM Sans font: on or off', 'dlist' ) ) {
		$fonts[] = 'DM+Sans:400,500,700';
	}

	if ( $fonts ) {
		$fonts_url = add_query_arg(
			array(
				'family' => implode( '|', $fonts ),
				'subset' => $subsets,
			),
			'https://fonts.googleapis.com/css'
		);
	}
	
	return esc_url_raw( $fonts_url );
}

/**
 * Enqueue scripts and styles.
 */
function dlist_scripts() {
	
	wp_enqueue_style( 'dlist-fonts', dlist_fonts_url(), array(), null );
	wp_enqueue_style( 'dlist-gutenberg', get_theme_file_uri( 'assets/css/gutenberg.css' ) );
	wp_enqueue_style( 'magnific-popup', get_theme_file_uri( 'vendor_assets/css/magnific-popup.css' ), array(), null );
	wp_enqueue_style( 'owl-carousel', get_theme_file_uri( 'vendor_assets/css/owl.carousel.min.css' ), array(), null );
	
	if ( is_rtl() ) {
		wp_enqueue_style( 'elementor-rtl', get_theme_file_uri( 'assets/css/elementor-rtl.css' ) );
		wp_enqueue_style( 'directorist-rtl', get_theme_file_uri( 'assets/css/directorist-rtl.css' ) );
		wp_enqueue_style( 'bootstrap-rtl', get_theme_file_uri( 'vendor_assets/css/bootstrap/bootstrap-rtl.css' ), array(), null );
		wp_enqueue_style( 'dlist-rtl-style', get_theme_file_uri( 'assets/css/theme-style-rtl.css' ), array(), null );
		wp_enqueue_style( 'dlist-responsive-rtl', get_theme_file_uri( 'assets/css/theme-responsive-rtl.css' ), array(), null );
	} else {
		//Helpgent
		if( class_exists( 'HelpGent' ) ){
			wp_enqueue_style( 'dlist-helpgent', get_theme_file_uri( 'assets/css/helpgent.css' ) );
		}
		wp_enqueue_style( 'dlist-elementor', get_theme_file_uri( 'assets/css/elementor.css' ) );
		wp_enqueue_style( 'dlist-directorist', get_theme_file_uri( 'assets/css/directorist.css' ) );
		wp_enqueue_style( 'bootstrap', get_theme_file_uri( 'vendor_assets/css/bootstrap/bootstrap.css' ), array(), null );
		wp_enqueue_style( 'dlist-style', get_theme_file_uri( 'assets/css/style.css' ), array(), null );
		wp_enqueue_style( 'dlist-responsive', get_theme_file_uri( 'assets/css/responsive.css' ), array(), null );
	}

	//Custom color selection.
	dlist_dynamic_style();

	wp_enqueue_script( 'bootstrap_popper', get_theme_file_uri( 'vendor_assets/js/bootstrap/popper.js' ), array( 'jquery' ), null, false );
	wp_enqueue_script( 'bootstrap', get_theme_file_uri( 'vendor_assets/js/bootstrap/bootstrap.min.js' ), array( 'jquery', 'bootstrap_popper' ), null, false );
	wp_enqueue_script( 'jquery-ui-core', array( 'jquery' ) );
	wp_enqueue_script( 'waypoints', get_theme_file_uri( 'vendor_assets/js/jquery.waypoints.min.js' ), array( 'jquery' ), null, true );
	wp_enqueue_script( 'counterup', get_theme_file_uri( 'vendor_assets/js/jquery.counterup.min.js' ), array( 'jquery' ), null, true );
	wp_enqueue_script( 'magnific-popup', get_theme_file_uri( 'vendor_assets/js/jquery.magnific-popup.min.js' ), array( 'jquery' ), null, true );
	wp_enqueue_script( 'carousel', get_theme_file_uri( 'vendor_assets/js/owl.carousel.min.js' ), array( 'jquery' ), null, true );
	wp_enqueue_script( 'headroom', get_theme_file_uri( 'vendor_assets/js/headroom.min.js' ), array( 'jquery' ), null, true );
	wp_enqueue_script( 'dlist-main', get_theme_file_uri( 'theme_assets/js/main.js' ), array( 'jquery' ), null, true );

	

	$data = array(
		'rtl'     => is_rtl() ? 'true' : 'false',
		'ajaxurl' => admin_url( 'admin-ajax.php' ),
	);

	wp_localize_script( 'dlist-main', 'dlist_rtl', $data );

	if ( did_action( 'elementor/loaded' ) && Plugin::$instance->preview->is_preview_mode() ) {
		// JS scripts
		wp_enqueue_script( 'waypoints' );
		wp_enqueue_script( 'magnific-popup' );
		wp_enqueue_script( 'counterup' );
		wp_enqueue_script( 'carousel' );
	}
	if ( is_singular() && comments_open() && get_option( 'thread_comments' ) ) {
		wp_enqueue_script( 'comment-reply' );
	}
}

add_action( 'wp_enqueue_scripts', 'dlist_scripts', 15 );

/*
=================================================
 Admin Enqueue scripts and styles.
=================================================*/
function dlist_admin_css() {
	wp_enqueue_style( 'dlist-admin-css', get_theme_file_uri( 'theme_assets/admin.css' ), array(), null );
	wp_enqueue_script( 'dlist-listing-image', get_theme_file_uri( 'theme_assets/listing-image.js' ), array( 'jquery' ), null, false );
}

add_action( 'admin_enqueue_scripts', 'dlist_admin_css' );

// Removing the 'directorist-inline-style' to prevent CSS conflict
// add_filter( 'directorist_load_inline_style', '__return_false' );

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
