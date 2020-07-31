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




def about_us(request):
    return render(request, 'productionpages/page/aboutus.html',{
        'tab': 'aboutus',
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })

def enrollnow(request):
    return render(request, 'productionpages/page/enroll.html',{
        'tab': 'enroll',
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })


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

def scholarship(request):
    return render(request, 'productionpages/page/scholarship.html',{
        'tab': 'contactus',
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })


def volunteer(request):
    return render(request, 'productionpages/page/volunteersignup.html',{
        'tab': 'volunteer',
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })

def digitallab(request):
    return render(request, 'productionpages/page/digitallab.html',{
        'tab': 'volunteer',
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })

def paymentfaqs(request):
    return render(request, 'productionpages/page/paymentfaqs.html',{
        'tab': 'volunteer',
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })




