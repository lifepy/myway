from django.utils.translation import ugettext_lazy as _
from django import forms

from models import Address, Item, Order, Package

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('package')

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        exclude = ('order')

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('sender','tracking_no')

class LoginForm(forms.Form):
    username = forms.RegexField(label = _("Username"), max_length = 40, required = True,
                                regex = r'^[\w.@+-_]+',
                                help_text = _("Required. 40 characters or fewer. Letters, digits and @/./+/-/_ only."),
                                error_messages={
                                    'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters"),
                                })
    
    password = forms.CharField(label = _("Password"), required=True, widget = forms.PasswordInput)
