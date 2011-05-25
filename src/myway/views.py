from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from django.contrib.auth.forms import AuthenticationForm

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('my/home')
    
    return render_to_response('index.html', context_instance=RequestContext(request, {'form': AuthenticationForm()}))

def about(request):
    return render_to_response('about.html', context_instance=RequestContext(request))

def test(request):
    return render_to_response('test.html')