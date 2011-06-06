import os, sys

#Calculate the path based on the location of the WSGI script.
apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)

path = os.path.join(workspace, 'myway', 'src')
if path not in sys.path:
    sys.path.append(path)

path = os.path.join(path, 'myway')
if path not in sys.path:
    sys.path.append(path)
# sys.path.append(workspace) 

os.environ['DJANGO_SETTINGS_MODULE'] = 'myway.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
