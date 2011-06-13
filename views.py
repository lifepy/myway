from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from django.contrib.auth.forms import AuthenticationForm

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
