import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404,HttpResponseRedirect
# from .models import Image,Profile,Comment,County
# from .forms import EditProfileForm
from django.contrib.auth.models import User


def landpageprod_page(request):
    return render(request, 'productionpages/page/index2.html',{
        'tab': 'landpageprod',
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })

def welcome(request):
    return render(request, 'productionpages/page/welcome.html',{
        'tab': 'welcomepage',
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })

def about_us(request):
    return render(request, 'productionpages/page/aboutus.html',{
        'tab': 'aboutus',
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })

# def enroll(request):
#     return render(request, 'productionpages/page/enroll.html',{
#         'tab': 'enroll',
#      'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
#         'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
#           })


def benefits(request):
    return render(request, 'productionpages/page/benefits.html',{
        'tab': 'benefits',
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })

def studentfaqs(request):
    return render(request, 'productionpages/page/studentfaqs.html',{
        'tab': 'studentfaqs',
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })


def sdgfaqs(request):
    return render(request, 'productionpages/page/sdgfaqs.html',{
        'tab': 'sdgfaqs',
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })

def sdgdigitallab(request):
    return render(request, 'productionpages/page/sdgdigitallab.html',{
        'tab': 'sdgdigitallab',
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })


def contactus(request):
    return render(request, 'productionpages/page/contactus.html',{
        'tab': 'contactus',
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })






# def profileprod(request):
#     title = 'LADA | profile'
#     current_user = request.user
#     profile = Profile.get_profile()
#     image = Image.get_images()
#     comments = Comment.get_comment()
#     return render(request,'productionpages/page/profileprod.html',
#                          {"title":title,
#                           "comments":comments,
#                            "image":image,
#                            "user":current_user,
#                             "profile":profile,
#        'local_css_urls': [                    
#                             "css2/demo.css",
#                              "css2/material-kit.min1036.css",   
#                             "css2/vertical-nav.css"
#                             ],
#         'local_js_urls': [ "core/jquery.min.js",
#                            "core/popper.min.js",
#                            "core/bootstrap-material-design.min.js",
#                            "js2/plugins/moment.min.js ",
#                            "js2/plugins/bootstrap-datetimepicker.js",
#                            "js2/plugins/nouislider.min.js", 
#                            "js2/plugins/jquery.sharrre.js", 
#                            "js2/plugins/bootstrap-tagsinput.js",            
#                            "js2/plugins/bootstrap-selectpicker.js",                         
#                            "js2/plugins/jasny-bootstrap.min.js",
#                            "js2/plugins/jquery.flexisel.js",
#                            "js2/modernizr.js",
#                            "js2/vertical-nav.js",
#                            "js2/buttons.js",
#                            "js2/demo.js",
#                            "js2/material-kit.min1036.js?v=2.1.1" ],
#          })


# def edit(request):
#     title = 'LADA | edit profile'
#     current_user = request.user
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST,request.FILES)
#         if form.is_valid():
#             update = form.save(commit=False)
#             update.user = current_user
#             update.save()
#             return redirect('/profileprod')
#     else:
#         form = EditProfileForm()
#     return render(request,'productionpages/page/edit.html', { 
#                                                "title":title,
#                                                 "form":form
#                                                   'local_css_urls': [                    
#                             "css2/demo.css",
#                              "css2/material-kit.min1036.css",   
#                             "css2/vertical-nav.css"
#                             ],
#         'local_js_urls': [ "core/jquery.min.js",
#                            "core/popper.min.js",
#                            "core/bootstrap-material-design.min.js",
#                            "js2/plugins/moment.min.js ",
#                            "js2/plugins/bootstrap-datetimepicker.js",
#                            "js2/plugins/nouislider.min.js", 
#                            "js2/plugins/jquery.sharrre.js", 
#                            "js2/plugins/bootstrap-tagsinput.js",            
#                            "js2/plugins/bootstrap-selectpicker.js",                         
#                            "js2/plugins/jasny-bootstrap.min.js",
#                            "js2/plugins/jquery.flexisel.js",
#                            "js2/modernizr.js",
#                            "js2/vertical-nav.js",
#                            "js2/buttons.js",
#                            "js2/demo.js",
#                            "js2/material-kit.min1036.js?v=2.1.1" ],
#          })
         