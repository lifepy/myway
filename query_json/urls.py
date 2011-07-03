from django.conf.urls.defaults import *

urlpatterns = patterns('',
    #(r'^cities/in/([^/]+)/$', 'get_city_list'),
    (r'^subareas/in/([^/]+)/$', 'query_json.geo_queries.get_area_list'),
    (r'^restraunts/in/([^/]+)/$', 'query_json.geo_queries.get_restraunt_list'),
    (r'^photolist/in/([^/]+)/$', 'spot_views.get_photolist_by_area'),
    (r'^files/in/([^/]+)/?(.+)?/$','query_json.file_queries.get_file_list'),
    (r'^aaData/files/in/([^/]+)/?(.+)?/$','query_json.file_queries.get_file_list_for_data_table')
)
