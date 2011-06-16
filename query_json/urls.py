from django.conf.urls.defaults import *

urlpatterns = patterns('json.views',
    (r'^cities/in/([^/]+/$', 'get_city_list'),
    (r'^areas/in/([^/]+/$', 'get_area_list'),
)
