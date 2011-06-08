from django.conf.urls.defaults import *
from django.contrib.auth import views as auth_views
from django.views.generic.simple import direct_to_template
from settings import rel
from django.contrib import admin
admin.autodiscover()

import views 

urlpatterns = patterns('',
    # Auth
    (r'^login/$', auth_views.login, {"template_name":"account/login.html", "redirect_field_name":"/"}),
    
    # Modules
    (r'account/', include('myway.account.urls')),
    (r'console/', include('myway.console.urls')),

    # For DEBUG Only
    (r'success/', direct_to_template, {'template':'debug/success.html'}),
    (r'fail/', direct_to_template, {'template':'debug/fail.html'}),
    
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
