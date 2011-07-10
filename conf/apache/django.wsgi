import os, sys
from os.path import join, pardir, abspath, dirname

#Calculate the path based on the location of the WSGI script.
apache_configuration= dirname(__file__)
project_dir = join(apache_configuration, pardir)

#tags_dir = os.path.join(src_dir, 'myway')

# append source dir
if project_dir not in sys.path:
    sys.path.append(project_dir)

# append tag dir
#if tags_dir not in sys.path:
#    sys.path.append(tags_dir)

sys.stdout = sys.stderr
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
os.environ['SCRIPT_NAME'] = '/myway/'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
