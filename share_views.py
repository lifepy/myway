# coding=utf-8
import os
import urllib2
from os.path import join, isdir, basename

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from settings import SHARE_DIR

@csrf_exempt
def share(request, relative_path):
    page_url = 'share.html'
    relative_path = relative_path.encode('utf-8')
    file_list = [ ]

    cur_dir = join(SHARE_DIR , relative_path)
    # print cur_dir
    # if isdir(cur_dir):
        # # if target is dir, go deep
        # for filename in os.listdir(cur_dir):
            # if isdir(join(SHARE_DIR, filename)):
                # file_list.append( (filename, True) )
            # else:
                # file_list.append( (filename, False) )
    # else:
        # # if target is a file, force a download
        # response = HttpResponse(mimetype='application/force-download')
        # filename = basename(relative_path)
        #response['Content-Disposition'] = 'attachment; filename='+filename
        # response['X-Sendfile-Encoding'] = 'url'
        # response['X-Sendfile'] = urllib2.quote(cur_dir)
        # return response

    if request.method == 'POST':
        for fname in request.FILES:
            f = request.FILES[fname]
            name = f.name.encode('utf-8')
            
            destination = open(join(cur_dir, name), 'wb+')
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
        return HttpResponseRedirect('/share/'+relative_path)

    print file_list
    return render_to_response(page_url, {'file_list':file_list})


