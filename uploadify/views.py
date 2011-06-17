from os.path import join

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import django.dispatch
import logging
logger = logging.getLogger('uploadify')

from uploadify import settings


upload_received = django.dispatch.Signal(providing_args=['data'])

@csrf_exempt
def upload(request, *args, **kwargs):
    if request.method == 'POST':
        if request.FILES:
            upload_received.send(sender='uploadify', data=request.FILES['Filedata'])
    return HttpResponse('True')

def upload_received_handler(sender, data, **kwargs):
    if data.file:
        handle_uploaded_file(data)

def handle_uploaded_file(f):
    name = ''
    for encoding in ['utf-8','gb2312','gbk']:
        try:
            name = f.name.encode(encoding)
        except:
            logger.error("Encoding with %s failed." % encoding)
        else:
            break
    if name == '':
        raise NotImplemented
    destination = open(join(settings.UPLOAD_ROOT,name), 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

upload_received.connect(upload_received_handler)
