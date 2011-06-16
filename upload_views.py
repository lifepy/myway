# coding=utf-8
from os.path import join

from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponse

import logging
logger = logging.getLogger('console.views')

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

def upload_single_file(request):
    print 'asdf'
    if request.method == 'POST':
        print request.FILES
        for fname in request.FILES['Filedata']:
            handle_uploaded_file(request.FILES[fname])
            print fname
    return HttpResponse('/ok')

def upload_multiple_files(request):
    return HttpResponse('whatsoever')

'''
def upload_share(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = UploadShareForm(request.POST,request.FILES)
        if form.is_valid():
            for fname in request.FILES:
                handle_uploaded_file(request.FILES[fname])
            return render_to_response('debug/success.html')
    else:
        form = UploadShareForm()
    c.update({'form':form})
    return render_to_response('uploadshare.html', c)
'''
