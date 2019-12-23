from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json
from registrar.models import Student
from registrar.models import Course
from registrar.models import Announcement
from account.forms import StudentForm
from registration.form import RegisterForm
from django.db import transaction
from account.models import *
from django.contrib import messages
from django.utils.translation import gettext as _
from django.http import HttpResponse
from account.forms import UserForm,StudentForm





@transaction.atomic
def editprod(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST,instance=request.user)
        profile_form = StudentForm(request.POST, instance=request.user.student)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('/courses')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = RegisterForm(instance=request.user)
        profile_form = StudentForm(instance=request.user.student)
    return render(request,' account/productionpages/pages/profile.html', {


        'user_form': user_form,
        'profile_form': profile_form,
        'local_css_urls': [                    
                            "css2/demo.css",
                             "css2/material-kit.min1036.css",   
                            "css2/vertical-nav.css"
                            ],
        'local_js_urls': [ "core/jquery.min.js",
                           "core/popper.min.js",
                           "core/bootstrap-material-design.min.js",
                           "js2/plugins/moment.min.js ",
                           "js2/plugins/bootstrap-datetimepicker.js",
                           "js2/plugins/nouislider.min.js", 
                           "js2/plugins/jquery.sharrre.js", 
                           "js2/plugins/bootstrap-tagsinput.js",            
                           "js2/plugins/bootstrap-selectpicker.js",                         
                           "js2/plugins/jasny-bootstrap.min.js",
                           "js2/plugins/jquery.flexisel.js",
                           "js2/modernizr.js",
                           "js2/vertical-nav.js",
                           "js2/buttons.js",
                           "js2/demo.js",
                           "js2/material-kit.min1036.js?v=2.1.1" ],
         
    })


def profileprod(request):
  return render(request, 'account/productionpages/pages/profile.html',{

        'local_css_urls': [                    
                            "css2/demo.css",
                             "css2/material-kit.min1036.css",   
                            "css2/vertical-nav.css"
                            ],
        'local_js_urls': [ "core/jquery.min.js",
                           "core/popper.min.js",
                           "core/bootstrap-material-design.min.js",
                           "js2/plugins/moment.min.js ",
                           "js2/plugins/bootstrap-datetimepicker.js",
                           "js2/plugins/nouislider.min.js", 
                           "js2/plugins/jquery.sharrre.js", 
                           "js2/plugins/bootstrap-tagsinput.js",            
                           "js2/plugins/bootstrap-selectpicker.js",                         
                           "js2/plugins/jasny-bootstrap.min.js",
                           "js2/plugins/jquery.flexisel.js",
                           "js2/modernizr.js",
                           "js2/vertical-nav.js",
                           "js2/buttons.js",
                           "js2/demo.js",
                           "js2/material-kit.min1036.js?v=2.1.1" ],
         })
         