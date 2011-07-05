from django.conf.urls.defaults import *
from django.contrib.auth import views as auth_views
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()

from settings import rel
import views 
urlpatterns = patterns('',
    # For DEBUG Only
    (r'success/', direct_to_template, {'template':'debug/success.html'}),
    (r'fail/', direct_to_template, {'template':'debug/fail.html'}),
    (r'^test/$', direct_to_template, {'template':'test.html'}),
    (r'^login/modal/$', direct_to_template, {'template':'login_modal.html'}),

    # Modules
    (r'^place/', include('place.urls')),     # place-related pages/queries
    (r'^account/', include('account.urls')), # account management
    (r'^json/', include('query_json.urls')), # general json queries
    (r'^todo/', include('todo.urls')),       # Todo list (to be tuned)

    # Upload
    (r'^upload/photo/fs/$', views.upload.upload_file), # store photo to file system
    (r'^uploadify/', include('uploadify.urls')),
    
    # Basic Views
    url(r'^$', views.basic.index, name='index-url'),
    url(r'about/$', views.basic.about,name='about-url'),
    url(r'plan/$', views.basic.plan, {'city':''},name='plan-url'),
    url(r'plan/(.+)/$', views.basic.plan),
    url(r'blog/$', views.basic.blog, name='blog-url'),
    (r'^home/$', views.basic.home),

    # Share
    (r'^share/$', views.share.upload_and_download, {'relative_path':''}),
    (r'^share/(.+)/$', views.share.upload_and_download),
    (r'^share/check/$', views.share.check),

    # GridFS access
    (r'^gridfs/([a-zA-Z0-9]+)/$', views.grid_fs.serve_file_by_id),
    (r'^gridfs/photo/([a-zA-Z0-9]+)/$', views.grid_fs.serve_photo_by_id),

    # Log in/out
    (r'^login/$', auth_views.login, {"template_name":"account/login.html", "redirect_field_name":"/home"}),
    (r'^logout/$', auth_views.logout, {"template_name":'account/logged_out.html'}),
    # Admin
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Static
    (r'static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': rel('static')}),
)
