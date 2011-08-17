# coding=utf-8
import urllib2
from os.path import splitext

from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext

from query_json.db import province_list
from mongo_models import Photo, Restraunt

def store_photo_to_db(file, author, description, content_type):
    ''' Store uploaded photo into GridFS (mongoDB) '''
    if file.name == '':
        raise ValueError
    r = Restraunt.objects().first()
    photo = Photo(author=author, description=description)
    photo.file.new_file()
    
    for chunk in file.chunks():
        photo.file.write(chunk)
    photo.file.content_type=content_type
    photo.file.close()
    photo.save()
    r.photos.append(photo)
    r.save()
    return photo

def upload_photo(request):
    if request.method == 'GET':
        c = {}
        c.update(csrf(request))
        plist = [ (p['name'], p['region-code']) for p in province_list]
        c.update({"province_list" : plist})
        return render_to_response('place/upload.html', c, context_instance=RequestContext(request))
    if request.method == 'POST':
        # remove file extension name
        filenames = [ splitext(fname)[0] for fname in dict(request.POST)['Filename'] ]
        # quote to match 
        file_root_names = [ urllib2.quote(fname.encode('utf-8')) for fname in filenames ]
        place = request.POST['spot']
        r = Restraunt.objects(name=place).first()
        for i,fid in enumerate(request.FILES):
            file = request.FILES[fid]
            root_name = file_root_names[i]
            # TODO: read username
            photo = store_photo_to_db(file, 'simon', request.POST['desc-' + root_name], file.content_type)
            if r:
                r.photos.append(photo)
        r.save()        
        return render_to_response('debug/success.html')

