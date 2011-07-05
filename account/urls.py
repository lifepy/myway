from django.conf.urls.defaults import *

urlpatterns = patterns('account',
    (r'^register/$', 'views.register'),
    (r'^confirm/(?P<activation_key>.+$)', 'views.confirm'),
    (r'^login/json/$', 'ajax.ajax_login'),
)
