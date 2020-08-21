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

# Developer units:
# (1) Templates
# https://docs.djangoproject.com/en/1.7/ref/templates
#
# (2) JSON
# https://docs.djangoproject.com/en/1.7/topics/serialization/


@login_required(login_url='/redirect_login')
def module_units_page(request, course_id, id):
    course = Course.objects.get(id=course_id)
    try:
        module = Module.objects.get(id=id)
    except Module.DoesNotExist:
        module = None
    return render(request, 'course/module_unit/view.html',{
        'course' : course,
        'module' : module,
        'user' : request.user,
        'tab' : 'modules',
        'HAS_ADVERTISMENT': settings.APPLICATION_HAS_ADVERTISMENT,
        'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })


@login_required(login_url='/redirect_login')
def view_module_unit(request, course_id, id):
    response_data = {}
    if request.is_ajax():
        if request.method == 'POST':
            try:
                unit_id = int(request.POST['unit_id'])
                unit = Unit.objects.get(unit_id=unit_id)
            except Unit.DoesNotExist:
                unit = None
            return render(request, 'course/module_unit/details.html',{
                'unit' : unit,
                'user' : request.user,
                'HAS_ADVERTISMENT': settings.APPLICATION_HAS_ADVERTISMENT,
                'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
                'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS,
            })
