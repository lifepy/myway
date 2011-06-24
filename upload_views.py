# coding=utf-8
from os.path import join

from django import forms
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
import logging
logger = logging.getLogger('console.views')

from query_json.db import province_list
from mongo_models import Photo

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

def store_photo_to_db(file, author, description, content_type):
    ''' Store uploaded photo into GridFS (mongoDB) '''
    if file.name == '':
        raise ValueError
    photo = Photo(author=author, description=description)
    photo.file.new_file()
    
    for chunk in file.chunks():
        photo.file.write(chunk)
    photo.file.close()
    photo.file.content_type=content_type
    photo.save()
    return photo


# ------------------------------------------------------------------
# Views
def upload_photo(request):
    if request.method == 'GET':
        c = {}
        c.update(csrf(request))
        plist = [ (p['name'], p['id']) for p in province_list]
        c.update({"province_list" : plist})
        return render_to_response('upload.html', c)
    if request.method == 'POST':
        for fname in request.FILES:
            file = request.FILES[fname]
            # TODO: add field so that user could add description for picture
            store_photo_to_db(file, 'simon', 'change me!', file.content_type)
        return render_to_response('debug/success.html')

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
