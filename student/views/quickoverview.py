from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json
import datetime
from registrar.models import Student
from registrar.models import Course
from registrar.models import Quick_Overview


@login_required(login_url='/landpageprod')
def quickoverviews_page(request, id):
    course = Course.objects.get(id=id)
    try:
        quickoverviews = Quick_Overview.objects.filter(course=course).order_by('-quickoverview_id')
    except Quick_Overview.DoesNotExist:
        quickoverviews = None
    return render(request, 'course/quickoverview/view.html',{
        'course' : course,
        'quickoverviews' : quickoverviews,
        'user' : request.user,
        'tab' : 'quickoverviews',
        'HAS_ADVERTISMENT': settings.APPLICATION_HAS_ADVERTISMENT,
        'local_css_urls' : settings.SB_ADMIN_COURSE_DETAIL_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_COURSE_DETAIL_JS_LIBRARY_URLS,
    })
