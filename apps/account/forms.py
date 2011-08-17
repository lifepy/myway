import random, hashlib, datetime
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

from models import UserProfile

def validate_username_not_exist(value):
    try:
        User.objects.get(username=value)
    except User.DoesNotExist:
        return
    raise ValidationError(_("The username is already taken"))

class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new user account
    """
    username = forms.RegexField(label = _("Username"), max_length = 40, required = True,
                                regex = r'^[\w.@+-_]+',
                                help_text = _("Required. 40 characters or fewer. Letters, digits and @/./+/-/_ only."),
                                error_messages={
                                    'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters"),
                                })
    
    email = forms.EmailField(label = _("Email"), max_length=40, required=True)
    password1 = forms.CharField(label = _("Password"), required=True, widget = forms.PasswordInput)
    password2 = forms.CharField(label = _("Password Confirmation"), required=True, widget = forms.PasswordInput)

    # Optional fields
    last_name = forms.CharField(label = _("Last Name"), max_length=40, required=False)
    first_name = forms.CharField(label = _("First Name"), max_length=40, required=False)

    class Meta:
        model = User
        fields = ("username", "email", "last_name", "first_name")

    def clean_username(self):
        """
        Verify username not existed in database
        """
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError(_("A user with that username already exists."))
    
    def clean_password2(self):
        """
        Verify password2 is the same as password1
        """
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise ValidationError(_("The two password field didn't match"))
        return password2

    def save(self, commit=True):
        """
        Save User and related UserProfile object into database

        NOTICE: saved user has is_active set as False by default. A user account will be activated only
        if the user clicks confirmation link sent to his/her mailbox.
        """
        user = super(RegistrationForm, self).save(commit=False)
        password = self.cleaned_data['password2']
        user.set_password(password)
        user.is_active = False
        if commit:
            user.save()
        
        # Build user profile and activation key
        salt = hashlib.new('sha',str(random.random())).hexdigest()[:-5]
        activation_key = hashlib.new('sha',salt+user.username).hexdigest()
        expire_time = datetime.datetime.today() + datetime.timedelta(2)

        profile = UserProfile(user=user, activation_key=activation_key, expire_time=expire_time)
        if commit:
            profile.save()

        return user, profile
