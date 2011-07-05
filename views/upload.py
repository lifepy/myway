# coding=utf-8
from os.path import join

from django import forms
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
import logging
logger = logging.getLogger('console.views')

from query_json.db import province_list

class UploadShareForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

def store_to_fs(file, target_dir):
    ''' Store uploaded file to file system under given target_dir '''
    name = file.name.encode('utf-8')
    if name == '':
        raise ValueError
    destination = open(join(target_dir,name), 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()


def upload_file(request):
    if request.method == 'GET':
        c = {}
        c.update(csrf(request))
        plist = [ (p['name'], p['id']) for p in province_list]
        c.update({"province_list" : plist})
        return render_to_response('upload.html', c)
    if request.method == 'POST':
        for fname in request.FILES:
            store_to_fs(request.FILES[fname], '/opt/www/upload')
        return render_to_response('debug/success.html')

# deprecated!
def upload_share(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = UploadShareForm(request.POST,request.FILES)
        if form.is_valid():
            for fname in request.FILES:
                store_to_fs(request.FILES[fname], '/opt/www/share')
            return render_to_response('debug/success.html')
    else:
        form = UploadShareForm()
    c.update({'form':form})
    return render_to_response('uploadshare.html', c)
