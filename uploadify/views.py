from os.path import join

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import django.dispatch
import logging
logger = logging.getLogger('uploadify')

from uploadify import settings

upload_received = django.dispatch.Signal(providing_args=['data','to_dir'])

@csrf_exempt
def upload(request, *args, **kwargs):
    '''
    Upload file to target dir specified as uploadify.settings.UPLOAD_ROOT
    '''
    if request.method == 'POST':
        if request.FILES:
            upload_received.send(sender='uploadify', data=request.FILES['Filedata'], to_dir=settings.UPLOADIFY_UPLOAD_PATH)
    return HttpResponse('True')

def upload_received_handler(sender, data, to_dir, **kwargs):
    if data.file and to_dir:
        handle_uploaded_file(data, to_dir)

def handle_uploaded_file(file, to_dir):
    '''
    Move uploaded file to ``to_dir``
    '''
    name = ''
    for encoding in ['utf-8','gb2312','gbk']:
        try:
            name = file.name.encode(encoding)
        except:
            logger.error("Encoding with %s failed." % encoding)
        else:
            break
    if name == '':
        raise NotImplemented
    destination = open(join(to_dir,name), 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()

upload_received.connect(upload_received_handler)
