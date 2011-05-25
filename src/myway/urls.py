from django.conf.urls.defaults import *
from django.contrib.auth import views as auth_views
from settings import rel
from django.contrib import admin
admin.autodiscover()

import views 
import account

urlpatterns = patterns('',
    # Auth
    (r'^login/$', auth_views.login, {"template_name":"account/login.html", "redirect_field_name":"/"}),
    
    # Modules
    (r'my/', include('myway.my.urls')),
    (r'account/', include('myway.account.urls')),
    
    # Static
    (r'static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': rel('static')}),
    
    # Public
    url(r'/$', views.index, name='root_url'),
    url(r'index/$', views.index, name="index_url"),
    url(r'about/$', views.about, name="about_url"),

    # Admin
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

)
