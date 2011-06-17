from django.conf import settings
STATIC_DOC_ROOT = getattr(settings, 'STATIC_DOC_ROOT', '')
MEDIA_ROOT = getattr(settings, 'MEDIA_ROOT', '')

# Uploadify root folder path, relative to MEDIA_ROOT
UPLOADIFY_PATH = '%s' % '/static/jquery/uploadify/'

# Upload path that files are sent to
UPLOADIFY_UPLOAD_PATH = '%s%s' % (MEDIA_ROOT, 'upload/')

UPLOAD_ROOT = '/opt/www/upload'
