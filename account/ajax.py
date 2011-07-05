# coding=utf-8
from django.utils import simplejson
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect, csrf_exempt

@csrf_exempt
def ajax_login(request):
    import pdb; pdb.set_trace()
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            ret = simplejson.dumps({'success':True, 'redirect':'/home/'})
        else:
            ret = simplejson.dumps({'success':False, 'message':'disabled user account, please activate first'})
    else:
        ret = simplejson.dumps({'success':False, 'message':'incorrect username or password'})

    return HttpResponse(ret)
