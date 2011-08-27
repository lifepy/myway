import sys
from os.path import dirname, join, realpath

'''
import mongoengine
mongoengine.connect('mywaydb', 'myway', 'sharemyway2u')
AUTHENTICATION_BACKENDS = ('mongoengine.django.auth.MongoEngineBackend',)
SESSION_ENGINE = 'mongoengine.django.sessions'
'''

PROJECT_ROOT = dirname(realpath(__file__))
sys.path.append(join(PROJECT_ROOT, 'apps'))

DEBUG=True
SCRIPT_NAME="/"
TEMPLATE_DEBUG = DEBUG

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
MEDIA_URL = '/media/'
MEDIA_ROOT = join(PROJECT_ROOT,'media')#'/opt/www/media'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# ADMIN_MEDIA_PREFIX = '/media/'

# Static Files
STATIC_URL = '/static/'
STATIC_DOC_ROOT = join(PROJECT_ROOT, 'media','static')

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3izojq@p1x5m+l*75!z3ih&+4eys8)ng2eogomdk+djipo=enz'

# Template
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

TEMPLATE_DIRS = (
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    join(PROJECT_ROOT, 'templates'),
)

# Middleware 
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django_extensions',
    'compressor',
    'uploadify',
    # my apps
    'account',
    'tags',
    'todo',
)

# Configurations for django-compressor
COMPRESS = True
COMPRESS_ROOT = STATIC_DOC_ROOT

try:
    from local_settings import *
except ImportError:
    pass
