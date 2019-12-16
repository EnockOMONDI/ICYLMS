from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json
from registrar.models import Student
from registrar.models import Course
from registrar.models import Announcement
from account.forms import UserForm






# @login_required(login_url='/landpageprod')
# def profile_page(request):
#     return render(request, 'account/profile/view.html',{
#         'user': request.user,
#         'form': UserForm(instance=request.user),
#         'tab': 'profile',
#         'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
#         'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
#     })


def profileprod(request):
    return render(request, 'account/productionpages/pages/profile.html',{
        'user': request.user,
        'form': UserForm(instance=request.user),
        'tab': 'profileprod',
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

# @login_required()
# def update_user(request):
#     response_data = {'status' : 'failed', 'message' : 'unknown deletion error'}
#     if request.is_ajax():
#         if request.method == 'POST':
#             form = UserForm(instance=request.user, data=request.POST)
#             if form.is_valid():
#                 form.instance.username = form.instance.email
#                 form.save()
#                 response_data = {'status' : 'success', 'message' : 'updated user'}
#             else:
#                 response_data = {'status' : 'failed', 'message' : json.dumps(form.errors)}
#     return HttpResponse(json.dumps(response_data), content_type="application/json")
