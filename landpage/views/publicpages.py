import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404,HttpResponseRedirect

from django.contrib.auth.models import User


#newhomepage         
def home_page(request):
    return render(request, 'publicpages/index.html',{
        'tab': 'home_page',
       'local_css_urls' : settings.SB_ADMIN_COURSE_DETAIL_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_COURSE_DETAIL_JS_LIBRARY_URLS
 })


def platform_overview(request):
    return render(request, 'publicpages/platformoverview.html',{
        'tab': 'platform_overview',
       'local_css_urls' : settings.SB_ADMIN_COURSE_DETAIL_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_COURSE_DETAIL_JS_LIBRARY_URLS
 })

def our_story(request):
    return render(request, 'publicpages/ourstory.html',{
        'tab': 'whoweare',
       'local_css_urls' : settings.SB_ADMIN_COURSE_DETAIL_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_COURSE_DETAIL_JS_LIBRARY_URLS
 })


def scholarship(request):
    return render(request, 'publicpages/scholarship.html',{
       'tab': 'scholarship',
       'local_css_urls' : settings.SB_ADMIN_COURSE_DETAIL_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_COURSE_DETAIL_JS_LIBRARY_URLS
 })

def contactus(request):
    return render(request, 'publicpages/contactus.html',{
        'tab': 'contactus',
        'local_css_urls' : settings.SB_ADMIN_COURSE_DETAIL_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_COURSE_DETAIL_JS_LIBRARY_URLS
 })