from django.conf.urls.defaults import *

urlpatterns = patterns('account.views',
    (r'^register/$', 'register'),
    (r'^confirm/(?P<activation_key>.+$)', 'confirm'),
)
