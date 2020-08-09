from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json
import datetime
from registrar.models import Teacher
from registrar.models import Student
from registrar.models import Course
from registrar.models import Quick_Overview
from teacher.forms import QuickoverviewForm

# Developer Notes:
# (1) Templates
# https://docs.djangoproject.com/en/1.7/ref/templates
#


@login_required(login_url='/redirected_login')
def quickoverviews_page(request, course_id):
    course = Course.objects.get(id=course_id)
    teacher = Teacher.objects.get(user=request.user)
    
    try:
        quickoverviews = Quick_Overview.objects.filter(course=course).order_by('-quickoverview_id')
    except Quick_Overview.DoesNotExist:
        quickoverviews = None
    
    return render(request, 'teacher/quickoverview/view.html',{
        'teacher' : teacher,
        'course' : course,
        'quickoverviews' : quickoverviews,
        'user' : request.user,
        'tab' : 'quickoverview',
        'HAS_ADVERTISMENT': settings.APPLICATION_HAS_ADVERTISMENT,
        'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })


@login_required(login_url='/redirected_login')
def quickoverviews_table(request, course_id):
    course = Course.objects.get(id=course_id)
    teacher = Teacher.objects.get(user=request.user)
    
    try:
        quickoverviews = Quick_Overview.objects.filter(course=course).order_by('-quickoverview_id')
    except Quick_Overview.DoesNotExist:
        quickoverviews = None
    return render(request, 'teacher/quickoverview/table.html',{
        'teacher' : teacher,
        'course' : course,
        'quickoverviews' : quickoverviews,
        'user' : request.user,
    })


@login_required(login_url='/redirected_login')
def quickoverview_modal(request, course_id):
    if request.method == u'POST':
        # Get the quickoverview_id of post and either create a brand new form
        # for the user, or load up existing one based on the database
        # data for the particular assignment.
        quickoverview_id = int(request.POST['quickoverview_id'])
        form = None
        if quickoverview_id > 0:
            quickoverview = Quick_Overview.objects.get(quickoverview_id=quickoverview_id)
            form = QuickoverviewForm(instance=quickoverview)
        else:
            form = QuickoverviewForm()
        return render(request, 'teacher/quickoverview/modal.html',{'form' : form})


@login_required(login_url='/redirected_login')
def save_quickoverview(request, course_id):
    response_data = {'status' : 'failed', 'message' : 'unknown error with saving'}
    if request.is_ajax():
        if request.method == 'POST':
            course = Course.objects.get(id=course_id)
            quickoverview_id = int(request.POST['quickoverview_id'])
            form = None
            # If quickoverview already exists, then lets update only, else insert.
            if quickoverview_id > 0:
                try:
                    quickoverview = Quick_Overview.objects.get(quickoverview_id=quickoverview_id)
                except Quick_Overview.DoesNotExist:
                    return HttpResponse(json.dumps({
                        'status' : 'failed', 'message' : 'cannot find record'
                    }), content_type="application/json")
                form = QuickoverviewForm(instance=quickoverview, data=request.POST)
            else:
                form = QuickoverviewForm(request.POST, request.FILES)
                form.instance.course = course
            
            if form.is_valid():
                form.save()
                response_data = {'status' : 'success', 'message' : 'saved'}
            else:
                response_data = {'status' : 'failed', 'message' : json.dumps(form.errors)}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


@login_required(login_url='/redirected_login')
def delete_quickoverview(request, course_id):
    response_data = {'status' : 'failed', 'message' : 'unknown error with deleting'}
    if request.is_ajax():
        if request.method == 'POST':
            quickoverview_id = int(request.POST['quickoverview_id'])
            teacher = Teacher.objects.get(user=request.user)
            try:
                quickoverview = Quick_Overview.objects.get(quickoverview_id=quickoverview_id)
                if quickoverview.course.teacher == teacher:
                    quickoverview.delete()
                    response_data = {'status' : 'success', 'message' : 'deleted'}
                else:
                    response_data = {'status' : 'failed', 'message' : 'unauthorized deletion'}
            except Quick_Overview.DoesNotExist:
                response_data = {'status' : 'failed', 'message' : 'cannot find record'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


    