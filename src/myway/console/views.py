from os.path import join
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from forms import UploadFileForm
from django.core.context_processors import csrf

def handle_uploaded_file(f):
     destination = open(join('/opt/www/upload',f.name), 'wb+')
     for chunk in f.chunks():
         destination.write(chunk)
     destination.close()

def upload_file(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        print 'a post'
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print 'valid'
            handle_uploaded_file(request.FILES['file'])
            return render_to_response('debug/success.html')
    else:
        form = UploadFileForm()
    c.update({'form':form})
    return render_to_response('upload.html', c)
