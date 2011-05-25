from django.conf.urls.defaults import *

urlpatterns = patterns('myway.account.views',
    (r'^register/$', 'register'),
    (r'^confirm/(?P<activation_key>.+$)', 'confirm'),
)
