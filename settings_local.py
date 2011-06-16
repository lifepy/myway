
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

SHARE_DIR='/opt/www/media/share'
UPLOAD_DIR='/opt/www/media/upload'

LOGIN_REDIRECT_URL='/home'
LOGIN_URL='/login'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/opt/www/media'
