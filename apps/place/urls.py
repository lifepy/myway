from django.conf.urls.defaults import *

urlpatterns = patterns('place',
    (r'^details/$', 'views.place_details'),
    (r'^photos/([^/]+)/json/$', 'ajax.get_photolist_by_area'),
    (r'^upload/$', 'upload.upload_photo'),
    (r'^restraunts/in/([^/]+)/json/$', 'ajax.get_restraunt_list'),
)
