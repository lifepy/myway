from django.conf.urls.defaults import *

urlpatterns = patterns('myway.console.views',
    (r'^upload/$', 'upload_file'),
    (r'uploadshare/$', 'upload_share'),
)
