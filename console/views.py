# coding=utf-8
from os.path import join

from django.core.context_processors import csrf
from django.shortcuts import render_to_response
import logging
logger = logging.getLogger('console.views')

from forms import UploadShareForm
from query_json.db import province_list

from mongo_models import Photo

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

def handle_uploaded_photo(f):
    if f.name == '':
        raise NotImplemented
    photo = Photo(author="simon", description="what so ever")
    photo.file.new_file()
    
    for chunk in f.chunks():
        photo.file.write(chunk)
        #destination.write(chunk)
    #destination.close()
    photo.file.close()
    photo.file.content_type="image/jpeg"
    photo.save()

def upload_file(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        for fname in request.FILES:
            handle_uploaded_photo(request.FILES[fname])
        return render_to_response('debug/success.html')
    plist = [ (p['name'], p['id']) for p in province_list]
    c.update({"province_list" : plist})
    return render_to_response('upload.html', c)

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
