from django import forms
from .models import Order
from django.contrib.auth.models import User
import datetime
from django.forms import ModelForm, Textarea, TextInput, NumberInput, FileField, Select
from django.contrib.auth.models import User
from account.models import PrivateMessage,Student

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
        self.fields['name'].initial = user.username
        self.fields['email'].initial = user.email
    

# class CheckoutForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         exclude = ('paid',)
#         fields = { 'name', 'email'}
#         labels = {
#            'email' :'email :',
#            'name' : 'name :'

          
#         }

#         widgets = {
         

#             'name': TextInput(attrs={'class': u'form-control','placeholder': u'Enter your name here'}),
#             'email': TextInput(attrs={'class': u'form-control','placeholder': u'Enter your email here'}),



#         }
