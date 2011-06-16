from django.conf.urls.defaults import *
from django.contrib.auth import views as auth_views
from django.views.generic.simple import direct_to_template
from settings import rel
from django.contrib import admin
admin.autodiscover()

import views 

urlpatterns = patterns('',
    # Logged in Home
    (r'^home/$', views.home),
    # Log in/out
    (r'^login/$', auth_views.login, {"template_name":"account/login.html", "redirect_field_name":"/home"}),
    (r'^logout/$', auth_views.logout, {"template_name":'account/logged_out.html'}),
    
    # Modules
    (r'account/', include('account.urls')),
    (r'console/', include('console.urls')),

    # Query returns JSON
    (r'json/', include('query_json.urls')),

    # For DEBUG Only
    (r'success/', direct_to_template, {'template':'debug/success.html'}),
    (r'fail/', direct_to_template, {'template':'debug/fail.html'}),
    
    # Static
    (r'static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': rel('static')}),
    
    # Public
    url(r'^$', views.index, name='index-url'),
    url(r'about/$', views.about,name='about-url'),
    url(r'plan/$', views.plan, {'city':''},name='plan-url'),
    url(r'plan/(.+)/$', views.plan),
    url(r'blog/$', views.blog, name='blog-url'),

    # Admin
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Share
    (r'^share/$', views.share, {'relative_path':''}),
    (r'^share/(.+)/$', views.share),

)
