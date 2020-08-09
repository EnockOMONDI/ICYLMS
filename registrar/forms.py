from django.db import models
from django import forms
# from django.forms import ModelForm, Textarea, TextInput
# from django.forms.extras.widgets import Select, SelectDateWidget
from registrar.models import Course
from cloudinary.forms import CloudinaryFileField
import datetime
from django.forms import ModelForm, Textarea, TextInput, NumberInput, FileField , Select, SelectDateWidget
# from django.forms.extras.widgets import Select, SelectDateWidget
# from registrar.models import Order


class CourseForm(forms.ModelForm):
    image = CloudinaryFileField(
        options = {
            'crop': 'thumb',
            'width': 200,
            'height': 200,
            'folder': 'Courses_pics'
       },
      
    )

    class Meta:
        model = Course
        fields = ['title', 'sub_title', 'category', 'description', 'start_date', 'finish_date', 'image', 'price', 'discount_price']
        labels = {
            'sub_title': 'Sub Title',
            'price': 'Price',
            'discount_price': 'discount_price',
            'start_date': 'Start Date',
            'finish_date': 'Finish Date',
        }
        widgets = {
            'title': TextInput(attrs={'class': u'form-control','placeholder': u'Enter Title'}),
            'sub_title': TextInput(attrs={'class': u'form-control','placeholder': u'Enter Sub-Title'}),
            'description': Textarea(attrs={'class': u'form-control','placeholder': u'Enter Description'}),
            'category': Select(attrs={'class': u'form-control'}),
            'start_date': SelectDateWidget(),
            'finish_date': SelectDateWidget(),
            'price': NumberInput(attrs={'class': u'form-control','placeholder': u'Course price'}),
            'discount_price': NumberInput(attrs={'class': u'form-control','placeholder': u'Course discount price'})

   }




# class CartForm(forms.Form):
#     quantity = forms.IntegerField(initial='1')
#     course_id = forms.IntegerField(widget=forms.HiddenInput)

#     def __init__(self, request, *args, **kwargs):
#         self.request = request
#         super(CartForm, self).__init__(*args, **kwargs)


# class CheckoutForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         exclude = ('paid',)

#         widgets = {
#             'address': forms.Textarea(attrs={'row': 5, 'col': 8}),
#         }