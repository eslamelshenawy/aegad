<?php
define('WP_CACHE', true); // Added by FlyingPress

/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the website, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'pkqczdte_WPHAA');

/** Database username */
define('DB_USER', 'pkqczdte_WPHAA');

/** Database password */
define('DB_PASSWORD', 'HsDy#v(ba[.kM&c97');

/** Database hostname */
define('DB_HOST', 'localhost');

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY', 'b4eccda66215efa71df6bd08f5298989d21309687d85ada00da5cba28e6abd74');
define('SECURE_AUTH_KEY', '7491b845eb6209f34c19a613c303eeb76726c78d91a049e0270746d6629ac317');
define('LOGGED_IN_KEY', 'eecdf1dccfae4f6687d22eff7c5a6f8b45f46917bbbe990586164b796c30acd8');
define('NONCE_KEY', '5ceca6e0bccab6bfe1428a0e3a4068b2b23d6514b4e33528da47c33edaf1fe09');
define('AUTH_SALT', 'ec8d4994ccfde0f1b59de7df45ae2bb4104bbbc3287af9187aa0a4bdc633db76');
define('SECURE_AUTH_SALT', '9d7d59a645dcd73afdfc3b16b42f2c2f6040ca5eb01c46217b99613f9b7046cd');
define('LOGGED_IN_SALT', '582ecf647e8ae6f1325c74e530dcdce56fb5e7f33ef2bc89c109ed0982c6aa2e');
define('NONCE_SALT', 'c9c31df17fda16708e0c5c15616e77d36305d6f512780b282ca6aacdaee4fceb');

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 *
 * At the installation time, database tables are created with the specified prefix.
 * Changing this value after WordPress is installed will make your site think
 * it has not been installed.
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/#table-prefix
 */
$table_prefix = '8uA_';
define('WP_CRON_LOCK_TIMEOUT', 120);
define('AUTOSAVE_INTERVAL', 300);
define('WP_POST_REVISIONS', 20);
define('EMPTY_TRASH_DAYS', 7);
define('WP_AUTO_UPDATE_CORE', true);

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://developer.wordpress.org/advanced-administration/debug/debug-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */





// Accept all subdomains
if (!defined('WP_HOME')) {
    $protocol = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off') ? 'https' : 'http';
    $domain = $_SERVER['HTTP_HOST'];
    define('WP_HOME', $protocol . '://' . $domain);
    define('WP_SITEURL', $protocol . '://' . $domain);
}
/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
// Settings modified by hosting provider
define('DISALLOW_FILE_EDIT', true);
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
