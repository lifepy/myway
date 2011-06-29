# coding=utf-8
import os
import urllib2
from os.path import join, isdir, basename

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from settings import SHARE_DIR
from mongo_models import *

@csrf_exempt
def download(request, object_id):
    page_url = 'share.html'

    



    cur_dir = join(SHARE_DIR , relative_path)
    if request.method == 'GET':
        if isdir(cur_dir):
            # if target is dir, go deep
            for filename in os.listdir(cur_dir):
                if isdir(join(SHARE_DIR, filename)):
                    file_list.append( (filename, True) )
                else:
                    file_list.append( (filename, False) )
        else:
            # if target is a file, force a download
            response = HttpResponse(mimetype='application/force-download')
            filename = basename(relative_path)
            response['Content-Disposition'] = 'attachment; filename='+filename
            response['X-Sendfile-Encoding'] = 'url'
            response['X-Sendfile'] = urllib2.quote(cur_dir)
            return response

    if request.method == 'POST':
        for fname in request.FILES:
            try:
                f = request.FILES[fname]
                name = f.name.encode('utf-8')
                print "Upload '%s' to '%s'" % (name, cur_dir)
                destination = open(join(cur_dir, name), 'wb+')
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()
            except Exception as e:
                print e
        print "SUCCESS"
        return HttpResponse('True')
        #return HttpResponseRedirect('/share/'+relative_path)

    return render_to_response(page_url, {'file_list':file_list, 'upload_path':'/share/'+relative_path+'/'})


