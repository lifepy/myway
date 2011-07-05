from os.path import dirname, join
rel = lambda * x: join(dirname(__file__) , *x)

# Localization Settings

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mywaydb', # Or path to database file if using sqlite3.
        'USER': 'myuser', # Not used with sqlite3.
        'PASSWORD': 'mypass', # Not used with sqlite3.
        'HOST': 'localhost', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306', # Set to empty string for default. Not used with sqlite3.
    }
}

WWW_ROOT = '/opt/www'
SHARE_DIR = WWW_ROOT+'/share'
UPLOAD_DIR = WWW_ROOT+'/upload'

AUTH_PROFILE_MODULE = 'account.UserProfile'
LOGIN_REDIRECT_URL='/home'
LOGIN_URL='/login'

STATIC_URL = '/static/'
STATIC_DOC_ROOT = rel('static')

MEDIA_ROOT = '/opt/www/media'

# Configurations for django-compressor
COMPRESS = True
COMPRESS_ROOT = STATIC_DOC_ROOT

