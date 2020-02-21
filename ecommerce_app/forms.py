from django import forms
from .models import Order
from django.contrib.auth.models import User
import datetime
from django.forms import ModelForm, Textarea, TextInput, NumberInput, FileField, Select
from django.contrib.auth.models import User
from account.models import PrivateMessage,Student
from cloudinary.forms import CloudinaryFileField
from django import forms
from django.forms import ModelForm

class CartForm(forms.Form):
    quantity = forms.Field(initial=1 , disabled=True, widget=forms.HiddenInput)
    product_id = forms.IntegerField(widget=forms.HiddenInput)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(CartForm, self).__init__(*args, **kwargs)



class CheckoutForm(forms.Form):
    name = forms.Field()
    email= forms.Field()
 
    
    def __init__(self, request, *args, **kwargs):
        self.request = request
        user=self.request.user
        super(CheckoutForm, self).__init__(*args, **kwargs)
        self.fields['name'].initial = user.first_name + " " + user.last_name
        self.fields['email'].initial = user.email

# class CheckoutForm(forms.ModelForm):
#     fields = { 'name','email'}
#     labels = {
#             'name': 'name :',
#             'email': 'email :',}

#     widgets = { 
#             'email': TextInput(attrs={'class': u'form-control','placeholder': u'Enter your email email'}),
#             'name': TextInput(attrs={'class': u'form-control','placeholder': u'Enter your Bio here'}),}
  
    
#     def __init__(self, request, *args, **kwargs):
#         self.request = request
#         user=self.request.user
#         super(CheckoutForm, self).__init__(*args, **kwargs)
#         self.fields['name'].initial = user.first_name + " " + user.last_name
#         self.fields['email'].initial = user.email


 
