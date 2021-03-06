# Django settings for cualbondi project.
import os

CUALBONDI_ENV = os.environ.get('CUALBONDI_ENV', 'development')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*',]

LOGIN_REDIRECT_URL = '/'

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: "/usuarios/%s/" % u.username, 
}

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
DEFAULT_FROM_EMAIL = "info@cualbondi.com.ar"

MANAGERS = ADMINS

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

DATABASES = {}

USE_CACHE = True
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
CACHE_TIMEOUT = 60*60

# Variables personalizadas
RADIO_ORIGEN_DEFAULT = 200
RADIO_DESTINO_DEFAULT = 200
LONGITUD_PAGINA = 5

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Argentina/Buenos_Aires'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-ar'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_PATH, os.path.pardir, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASE_PATH, os.path.pardir, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '=tr&%05vw6&s4eoq)wdj(d&(56#cq@5k0b-c$^v6vr)#%e(c+&'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'apps.core.middleware.WhodidMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "apps.core.context_processors.lista_ciudades",
    "apps.core.context_processors.get_ciudad_actual",
    "apps.core.context_processors.show_android_alert",
    "apps.core.context_processors.home_url",
    "apps.core.context_processors.facebook_app_id",
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.dirname(__file__),'templates'),
)

GOOGLE_API = "//maps.google.com/maps/api/js?v=3.6&sensor=false"

INSTALLED_APPS = (
    'social.apps.django_app.default',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.gis',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',

    # Externas
    'bootstrap_toolkit',
    'floppyforms',
    'imagekit',
    'leaflet',
    'piston',
#    'moderacion',
#    'editor',
#    'django_extensions',
    'rest_framework',
    'rest_framework_tracking',
    'django_nose',

    # Propias
    'apps.api2',
    'apps.catastro',
    'apps.core',
    'apps.usuarios',
    'apps.anuncios',
    'apps.mobile_updates',
    'apps.editor',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('apps.api2.permissions.ReadOnly',),
    'PAGE_SIZE': 10,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework_jsonp.renderers.JSONPRenderer',
    ),
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
here = lambda *x: os.path.join(os.path.dirname(os.path.realpath(__file__)), *x)
LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'simple': {
            'format': '%(levelname)s | %(message)s'
        },
        'json': {
            '()': 'django_log_formatter_json.JSONFormatter',
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'json'
        },
#        'file': {
#            'level': 'DEBUG',
#            'class': 'logging.FileHandler',
#            'filename': '/tmp/django.log',
#        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'logstash': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True
        }
    },
}

if CUALBONDI_ENV == 'production':

    LOGGING.update({
        'handlers': {
            'logstash': {
                'level': 'DEBUG',
                'class': 'logstash.LogstashHandler',
                'host': '78.47.196.202',  # stats.cualbondi.com.ar
                'port': 5000,
                'version': 1,
                'message_type': 'logstash',
                'fqdn': False,
                'tags': [],
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['logstash'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'logstash': {
                'handlers': ['logstash'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    })

    FACEBOOK_APP_ID = "516530425068934"
    FACEBOOK_API_SECRET = 'f90d27d49f50939996db0f299dec129d'
    FACEBOOK_EXTENDED_PERMISSIONS = ['email']
    SOCIAL_AUTH_FACEBOOK_KEY="516530425068934"
    SOCIAL_AUTH_FACEBOOK_SECRET='f90d27d49f50939996db0f299dec129d'
    SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

    HOME_URL = "http://cualbondi.com.ar"

    EMAIL_HOST = 'mail.cualbondi.com.ar'
    EMAIL_PORT = 25

    from settings_local import *
    INSTALLED_APPS += LOCAL_INSTALLED_APPS

else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'geocualbondidb',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }

    #MIDDLEWARE_CLASSES = ('debug_panel.middleware.DebugPanelMiddleware', ) + MIDDLEWARE_CLASSES
    
    FACEBOOK_APP_ID = "370174876416548"
    FACEBOOK_APP_ID = "516530425068934"
    FACEBOOK_API_SECRET = 'f90d27d49f50939996db0f299dec129d'
    FACEBOOK_EXTENDED_PERMISSIONS = ['email']
    SOCIAL_AUTH_FACEBOOK_KEY="516530425068934"
    SOCIAL_AUTH_FACEBOOK_SECRET='f90d27d49f50939996db0f299dec129d'
    SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
    HOME_URL = "http://local.cualbondi.com.ar"
    #INSTALLED_APPS += ('debug_toolbar', 'debug_panel','django_extensions')
    DEBUG_TOOLBAR_PATCH_SETTINGS = False 
    INSTALLED_APPS += ('debug_toolbar', 'django_extensions')
    
    import logging
    l = logging.getLogger('django.db.backends')
    l.setLevel(logging.DEBUG)
    l.addHandler(logging.StreamHandler())
    LOGGING.update({
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
            }
        },
        'loggers': {
            'django.db.backends': {
                'level': 'DEBUG',
                'handlers': ['console'],
            }
        }
    })

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        },

        # this cache backend will be used by django-debug-panel
        'debug-panel': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': '/var/tmp/debug-panel-cache',
            'TIMEOUT': 300,
            'OPTIONS': {
                'MAX_ENTRIES': 200
            }
        }
    }
    
    REQUEST_LOGGING_BACKEND = {
        'host': 'localhost',
        'port': 9200,
        'index': 'cualbondi',
        'type': 'requests'
    }


WERCKER_DB_IPADDR = os.environ.get('POSTGIS_PORT_5432_TCP_ADDR', False)
if WERCKER_DB_IPADDR:
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'cb',
            'HOST': WERCKER_DB_IPADDR,
            'PORT': os.environ.get('POSTGIS_PORT_5432_TCP_PORT', False)
        }
    }
    print DATABASES

# fix logging https://www.caktusgroup.com/blog/2015/01/27/Django-Logging-Configuration-logging_config-default-settings-logger/
LOGGING_CONFIG = None
import logging.config
logging.config.dictConfig(LOGGING)
