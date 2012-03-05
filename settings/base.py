# Django settings file for bedrock.

import os

from django.utils.functional import lazy

from funfactory.settings_base import *

# Make file paths relative to settings.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = lambda *a: os.path.join(ROOT, *a)

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-US'

SESSION_COOKIE_SECURE = True

# Accepted locales
PROD_LANGUAGES = ('de', 'en-US', 'es', 'fr',)
DEV_LANGUAGES = DEV_LANGUAGES + ['en-US']

DOTLANG_FILES = ('main.lang',)
DOTLANG_CACHE = 60

# Make this unique, and don't share it with anybody.
SECRET_KEY = '1iz#v0m55@h26^m6hxk3a7at*h$qj_2a$juu1#nv50548j(x1v'

TEMPLATE_DIRS = (
    path('templates'),
    path('locale')
)

def JINJA_CONFIG():
    import jinja2
    from django.conf import settings
    config = {'extensions': ['tower.template.i18n', 'jinja2.ext.do',
                             'jinja2.ext.with_', 'jinja2.ext.loopcontrols',
                             'l10n_utils.template.l10n_blocks'],
              'finalize': lambda x: x if x is not None else ''}
    return config

# Bundles is a dictionary of two dictionaries, css and js, which list css files
# and js files that can be bundled together by the minify app.
MINIFY_BUNDLES = {
    'css': {
        'b2g': (
            'css/b2g.less',
        ),
        'collusion': (
            'css/collusion.less',
        ),
        'common': (
            'css/sandstone/sandstone.less',
        ),
        'contribute': (
            'css/contribute.less',
        ),
        'channel': (
            'css/covehead/template.css',
            'css/covehead/content.css',
            'css/covehead/channel.css',
        ),
        'firefox': (
            'css/firefox/template.less',
        ),
        'firefox-customize': (
            'css/sandstone/video.less',
            'css/firefox/customize.less',
        ),
        'firefox-security': (
            'css/firefox/security.less',
        ),
        'home': (
            'css/covehead/template.css',
            'css/covehead/content.css',
            'css/covehead/home.css',
        ),
        'geolocation': (
            'css/covehead/template.css',
            'css/covehead/content.css',
            'css/covehead/mozilla-expanders.css',
            'css/covehead/geolocation.css',
            'css/jquery/nyroModal.css'
        ),
        'marketplace': (
            'css/marketplace.less',
        ),
        'persona': (
            'css/persona.less',
        ),
        'sandstone-guide': (
            'css/sandstone-guide.less',
        ),
        'video': (
            'css/sandstone/video.less',
        ),
    },
    'js': {
        'collusion': (
            'js/collusion/d3.layout.js',
            'js/collusion/d3.geom.js',
            'js/collusion/collusion-addon.js',
            'js/collusion/demo.js',
            'js/collusion/graphrunner.js',
        ),
        'common': (
            'js/libs/jquery-1.7.1.min.js',
        ),
        'firefox': (
            'js/libs/jquery-1.7.1.min.js',
            'js/nav-main.js',
        ),
        'firefox-customize': (
            'js/mozilla-video-tools.js',
            'js/firefox/customize.js',
        ),
        'geolocation': (
            'js/libs/jquery-1.4.4.min.js',
            'js/libs/jquery.nyroModal.pack.js',
            'js/mozilla-expanders.js',
            'js/geolocation-demo.js'
        ),
        'pager': (
            'js/mozilla-pager.js',
        ),
        'video': (
            'js/mozilla-video-tools.js',
        ),
    }
}

# Dynamically process LESS server-side? (usually true to local
# development)
LESS_PREPROCESS = False
LESS_BIN = 'lessc'

# Override this because we've moved settings into a directory
PROD_DETAILS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                'lib/product_details_json')

MIDDLEWARE_CLASSES = (
    'funfactory.middleware.LocaleURLMiddleware',
    'multidb.middleware.PinningRouterMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'session_csrf.CsrfMiddleware',  # Must be after auth middleware.
    'django.contrib.messages.middleware.MessageMiddleware',
    'commonware.middleware.FrameOptionsHeader',
    #'mobility.middleware.DetectMobileMiddleware',
    #'mobility.middleware.XMobileMiddleware',
    'mozorg.middleware.CacheMiddleware'
)

INSTALLED_APPS = list(INSTALLED_APPS) + [
    # Local apps
    'l10n_example',  # DELETEME
    'b2g',
    'collusion',
    'marketplace',
    'mozorg',
    'persona',
    'landing',
    'research',

    # libs
    'l10n_utils',
    'dotlang',
]

## Auth
PWD_ALGORITHM = 'bcrypt'
HMAC_KEYS = {
    #'2011-01-01': 'cheesecake',
}

GMAP_API_KEY = ''

BASKET_URL = 'http://basket.mozilla.com'

# This prefixes /b/ on all URLs generated by `reverse` so that links
# work on the dev site while we have a mix of Python/PHP
FORCE_SLASH_B = False
