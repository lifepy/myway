import os, sys
from os.path import join, pardir, abspath, dirname

#Calculate the path based on the location of the WSGI script.
apache_configuration= dirname(__file__)
project_dir = join(apache_configuration, pardir)

src_dir = os.path.join(project_dir, 'src')
tags_dir = os.path.join(src_dir, 'myway')

# append source dir
if src_dir not in sys.path:
    sys.path.append(src_dir)

# append tag dir
if tags_dir not in sys.path:
    sys.path.append(tags_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'myway.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
