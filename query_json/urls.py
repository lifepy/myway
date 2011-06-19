from django.conf.urls.defaults import *

urlpatterns = patterns('query_json.views',
    (r'^cities/in/([^/]+)/$', 'get_city_list'),
    (r'^subareas/in/([^/]+)/$', 'get_area_list'),
)
