from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from registrar.models import *
import json
import datetime

# Developer Notes:
# (1) Templates
# https://docs.djangoproject.com/en/1.7/ref/templates
#
# (2) JSON
# https://docs.djangoproject.com/en/1.7/topics/serialization/



@login_required(login_url='/redirected_login')
def modules_page(request, course_id):
    course = Course.objects.get(id=course_id)
    try:
        modules = Module.objects.filter(course_id=course_id).order_by('module_number')
    except Module.DoesNotExist:
        modules = None
    return render(request, 'course/module/view.html',{
        'course' : course,
        'modules' : modules,
        'user' : request.user,
        'tab' : 'modules',
        'HAS_ADVERTISMENT': settings.APPLICATION_HAS_ADVERTISMENT,
        'local_css_urls' : settings.SB_ADMIN_COURSE_DETAIL_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_COURSE_DETAIL_JS_LIBRARY_URLS,
    })



@login_required(login_url='/landpage')
def module(request, course_id):
    response_data = {}
    if request.is_ajax():
         if request.method == 'POST':
             # Check to see if any fields where missing from the form.
             if request.POST['id'] != '':
                 try:
                     id = int(request.POST['id'])
                     module = Module.objects.get(id=id)
                 except Module.DoesNotExist:
                     module = None
                 return render(request, 'course/module/details.html',{
                    'module' : module,
                    'user' : request.user,
                    'HAS_ADVERTISMENT': settings.APPLICATION_HAS_ADVERTISMENT,
                    'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
                    'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS,
                 })

