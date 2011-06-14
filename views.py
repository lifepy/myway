import os
from os.path import join, isdir, basename, dirname

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.forms import AuthenticationForm
from settings import SHARE_DIR

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home')
    
    return render_to_response('index.html', context_instance=RequestContext(request, {'form': AuthenticationForm()}))

def about(request):
    return render_to_response('about.html', context_instance=RequestContext(request))

def plan(request, city):
    print "city=%s"%city
    print bool(city)
    return render_to_response('plan.html', context_instance=RequestContext(request))

def blog(request):
    return render_to_response('teamblog.html', context_instance=RequestContext(request))

def test(request):
    return render_to_response('test.html')

def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))

@csrf_exempt
def share(request, relative_path):
    page_url = 'share.html'
    file_list = [dirname(relative_path), ]

    cur_dir = join(SHARE_DIR , relative_path)
    print cur_dir
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
        response['Content-Disposition'] = 'attachment; filename=%s' %basename(relative_path)
        response['X-Sendfile'] = cur_dir
        return response

    if request.method == 'POST':
        for fname in request.FILES:
            f = request.FILES[fname]
            name = f.name.encode('utf-8')
            
            destination = open(join(cur_dir, name), 'wb+')
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
        return HttpResponseRedirect('/share/'+relative_path)

    return render_to_response(page_url, {'file_list':file_list})
