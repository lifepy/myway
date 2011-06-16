# coding=utf-8
from os.path import join

from django.core.context_processors import csrf
from django.shortcuts import render_to_response
import logging
logger = logging.getLogger('console.views')

from forms import UploadFileForm
from forms import UploadShareForm
from query_json.views import city_dict

encodings = ['utf-8', 'gb2312', 'gbk']
def handle_uploaded_file(f):
    name = ''
    for encoding in encodings:
        try:
            name = f.name.encode(encoding)
        except:
            logger.error("Encoding with %s failed." % encoding)
        else:
            break
    if name == '':
        raise NotImplemented
    destination = open(join('/opt/www/upload',name), 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

def upload_file(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = UploadFileForm(request.POST)
        if form.is_valid():
            for fname in request.FILES:
                handle_uploaded_file(request.FILES[fname])
            return render_to_response('debug/success.html')
    else:
        form = UploadFileForm()
    c.update({'form':form})
    return render_to_response('upload.html', {"province_list" : city_dict.keys()})

def upload_share(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = UploadShareForm(request.POST,request.FILES)
        if form.is_valid():
            # consider to use this:
            for fname in request.FILES:
                handle_uploaded_file(request.FILES[fname])
            # handle_uploaded_file(request.FILES["file"])
            # if len(request.FILES) > 1:
                # for i in range(1,len(request.FILES)):
                    # file = request.FILES["file%d" %i]
                    # handle_uploaded_file(file)
            return render_to_response('debug/success.html')
    else:
        form = UploadShareForm()
    c.update({'form':form})
    return render_to_response('uploadshare.html', c)
