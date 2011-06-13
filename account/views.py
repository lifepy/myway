import datetime
from django.shortcuts import render_to_response, get_object_or_404
from django.utils.translation import ugettext as _
from django.core.mail import send_mail

# for csrf attack
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext
from account.forms import RegistrationForm
from account.models import UserProfile

@csrf_protect
def register(request):
    '''
    present a registration form, once completed by user, the system will send email containing
    confirmation link. The registration completes only if the user confirms the link.
    '''
    page_url = 'account/register.html' 
    if request.user.is_authenticated():
        # They already logged in, don't let them register again
        return render_to_response(page_url, {'has_account':True}, context_instance=RequestContext(request))
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user, profile = form.save()

            # Send email with confirmation link
            domain_name = "langtou.me"
            sender_email = "noreply@myway.com"
            email_subject = "Your new %s account confirmation" % domain_name
            email_body = _("Howdy, %s,\n\nThank you so much for signing up at langtou.me. We focus on providing you an intuitive way to plan and share your trips, Have fun!\n\nTo activate your account, click this link within 48 hours:\n\nhttp://localhost:8000/account/confirm/%s\n\nHappiness only real when shared.\n\nBest wishes,\nMyWay Team.") % (user.username, profile.activation_key)
            # print email_body
            send_mail(email_subject, email_body, sender_email, [user.email])

            return render_to_response(page_url, {'created':True}, context_instance=RequestContext(request))
    else:
        form = RegistrationForm()
    return render_to_response(page_url, {'form':form}, context_instance=RequestContext(request))

@csrf_exempt
def confirm(request, activation_key):
    '''
    takes in a hash and activate corresponding user
    '''
    page_url = 'account/confirm.html'
    if request.user.is_authenticated():
        return render_to_response(page_url, {'has_account':True})
    profile = get_object_or_404(UserProfile, activation_key=activation_key)
    if profile.expire_time < datetime.datetime.today():
        return render_to_response(page_url, {'expired':True})
    user = profile.user
    user.is_active = True
    user.save()
    return render_to_response(page_url, {'success':True})
