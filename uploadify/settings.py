import settings_local

STATIC_DOC_ROOT = getattr(settings_local, 'STATIC_DOC_ROOT', '')

# Uploadify root folder path, relative to MEDIA_ROOT
UPLOADIFY_PATH = '%s' % '/static/jquery/uploadify/'

# Upload path that files are sent to
UPLOADIFY_UPLOAD_PATH = settings_local.SHARE_DIR
