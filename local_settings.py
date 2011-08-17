SITE_ID = 1

# Time/Language
#TIME_ZONE = 'China/Beijing'
LANGUAGE_CODE = 'en-us'

ADMINS = (
    ('Han Zhang', 'zhanghan.simon@gmail.com'),
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

# Upload Folders
WWW_ROOT = '/opt/www'
SHARE_DIR = WWW_ROOT+'/share'
UPLOAD_DIR = WWW_ROOT+'/upload'

# Authentication
LOGIN_REDIRECT_URL='/home'
LOGIN_URL='/login'

# Profile
AUTH_PROFILE_MODULE = 'account.UserProfile'
