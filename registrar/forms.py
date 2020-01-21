from django.db import models
from django import forms
from django.forms import ModelForm, Textarea, TextInput
from django.forms.extras.widgets import Select, SelectDateWidget
from registrar.models import Course
from cloudinary.forms import CloudinaryFileField
import datetime
from django.forms import ModelForm, Textarea, TextInput, NumberInput, FileField
from django.forms.extras.widgets import Select, SelectDateWidget



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
        fields = ['title', 'sub_title', 'category', 'description', 'start_date', 'finish_date', 'image']
        labels = {
            'sub_title': 'Sub Title',
            # 'image': 'Upload Image',
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
        }

