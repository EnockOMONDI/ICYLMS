from django.shortcuts import render,redirect
from django.core import serializers
import json
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

from account.forms import UserForm,StudentForm
from registration.form import RegisterForm
from django.db import transaction
from registrar.models import *
from account.models import *
from registrar.forms import CourseForm
from django.contrib import messages
from django.utils.translation import gettext as _
from registrar.forms import CourseForm
from registrar.models import CourseFinalMark
import datetime
from account.models import PrivateMessage
from account.forms import PrivateMessageForm

@login_required(login_url='/landpage')
def mail_page(request):
    try:
        email = request.user.email
        messages = PrivateMessage.objects.filter(to_address=email)
    except PrivateMessage.DoesNotExist:
        messages = None
    
    return render(request, 'account/mail/view.html',{
        'messages': messages,
        'user': request.user,
        'tab': 'inbox',
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })


@login_required()
def send_private_message(request):
    response_data = {'status' : 'failed', 'message' : 'unknown error'}
    if request.is_ajax():
        if request.method == 'POST':
            title = request.POST['title']
            text = request.POST['message']
            email = request.POST['email']
            
            # Validate email exists on system.
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                response_data = {'status' : 'failure', 'message' : 'email does not exist in our system'}
                return HttpResponse(json.dumps(response_data), content_type="application/json")

            PrivateMessage.objects.create(
                title=title,
                text=text,
                to_address=email,
                from_address=request.user.email,
            ).save()

            response_data = {'status' : 'success', 'message' : 'private message sent'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


@login_required()
def view_private_message(request):
    response_data = {'status' : 'failed', 'message' : 'unknown error'}
    if request.is_ajax():
        if request.method == 'POST':
            message_id = int(request.POST['message_id'])
            try:
                message = PrivateMessage.objects.get(id=message_id)
            except PrivateMessage.DoesNotExist:
                message = None
            
            form = PrivateMessageForm(instance=message)
            return render(request, 'account/mail/modal.html',{
                'form': form,
                'user': request.user,
                'tab': 'inbox',
                'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
                'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
            })


@login_required()
def delete_private_message(request):
    response_data = {'status' : 'failed', 'message' : 'unknown error'}
    if request.is_ajax():
        if request.method == 'POST':
            message_id = int(request.POST['message_id'])
            try:
                message = PrivateMessage.objects.get(
                    id=message_id,
                ).delete()
            except PrivateMessage.DoesNotExist:
                message = None
            
            response_data = {'status' : 'success', 'message' : 'deleted private message'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")




@login_required()
def disenroll_modal(request):
    # Create our student account which will build our registration around.
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        student = Student.objects.create(user=request.user)

    course_id = int(request.POST['course_id'])
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        course = None
    return render(request, 'account/productionpages/pages/disenrollmodal.html',{
        'student' : student,
        'course': course,
        'user' : request.user,
    })


@login_required()
def disenroll(request):
    response_data = {'status' : 'failure', 'message' : 'unsupported request format'}
    if request.is_ajax():
        course_id = int(request.POST['course_id'])
        student = Student.objects.get(user=request.user)
        try:
            course = Course.objects.get(id=course_id)
            course.students.remove(student)
            response_data = {'status' : 'success', 'message' : 'disenrolled' }
        except Course.DoesNotExist:
            response_data = {'status' : 'failed', 'message' : 'record does not exist' }
    return HttpResponse(json.dumps(response_data), content_type="application/json")





@login_required(login_url='/landpageprod')
def profile_page(request):
    return render(request, 'account/profile/view.html',{
        'user': request.user,
        'form': UserForm(instance=request.user),
        'tab': 'profile',
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })


@login_required()
def update_user(request):
    response_data = {'status' : 'failed', 'message' : 'unknown deletion error'}
    if request.is_ajax():
        if request.method == 'POST':
            form = UserForm(instance=request.user, data=request.POST)
            if form.is_valid():
                form.instance.username = form.instance.email
                form.save()
                response_data = {'status' : 'success', 'message' : 'updated user'}
            else:
                response_data = {'status' : 'failed', 'message' : json.dumps(form.errors)}
    return HttpResponse(json.dumps(response_data), content_type="application/json")

@login_required()
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':

        # user_form = RegisterForm(request.POST,instance=request.user)
        profile_form = StudentForm(request.POST,files=request.FILES, instance=request.user.student)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('/view/profile/')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        profile_form = StudentForm(instance=request.user.student)
    return render(request, 'account/productionpages/pages/edit3.html', {
        # 'user_form': user_form,
        'profile_form': profile_form,
    'local_css_urls' : settings.SB_ADMIN_COURSE_DETAIL_CSS_LIBRARY_URLS,
   'local_js_urls' : settings.SB_ADMIN_COURSE_DETAIL_JS_LIBRARY_URLS,
   }) 
 
 

    
@login_required()
def view_profile(request):
    try:
        student = request.user.student
    except Student.DoesNotExist:
        student = Student.objects.create(user=request.user)
    try:
        courses = Course.objects.filter(students__student_id=student.student_id)
    except Course.DoesNotExist:
        courses = None
    try:
        marks = CourseFinalMark.objects.filter(student=student)
    except CourseFinalMark.DoesNotExist:
        marks = None
        
  
    return render(request, 'account/productionpages/pages/profile2.html',{
   'courses': courses,
   'user' : request.user,    
   'student':student,
   'marks': marks,
   'local_css_urls' : settings.SB_ADMIN_COURSE_DETAIL_CSS_LIBRARY_URLS,
   'local_js_urls' : settings.SB_ADMIN_COURSE_DETAIL_JS_LIBRARY_URLS,
   }) 

                               
@login_required()
def trainingbits(request):
    return render(request, 'account/productionpages/pages/trainingbits.html',{
        'local_css_urls': [                    
                            "css2/demo.css",
                             "css2/material-kit.min1036.css",   
                            "css2/vertical-nav.css"
                            ],
        'local_js_urls': ["core/jquery.min.js",
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
                           "js2/material-kit.min1036.js?v=2.1.1" ],})

@login_required(login_url='/landpageprod')
def change_certificate_accessiblity(request):
    response_data = {'status' : 'failed', 'message' : 'unknown error with saving'}
    if request.is_ajax():
        if request.method == 'POST':
            credit_id = int(request.POST['credit_id'])
            try:
                mark = CourseFinalMark.objects.get(credit_id=credit_id)
                if mark.is_public:
                    mark.is_public = False
                else:
                    mark.is_public = True
                mark.save()
                response_data = {'status' : 'success', 'message' : 'certificate accessiblity changed'}
            except CourseFinalMark.DoesNotExist:
                response_data = {'status' : 'failure', 'message' : 'certificate does not exist'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


@login_required()
def certificate_page(request, credit_id):
    # Create our student account which will build our registration around.
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        student = Student.objects.create(user=request.user)
    try:
        mark = CourseFinalMark.objects.get(credit_id=credit_id)
    except CourseFinalMark.DoesNotExist:
        mark = None

    return render(request, 'registrar/certificate/certificate.html',{
        'student': student,
        'mark': mark,
        'user': request.user,
        'tab': 'certificates',
        'HAS_ADVERTISMENT': settings.APPLICATION_HAS_ADVERTISMENT,
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS
    })


@login_required()
def certificate_permalink_modal(request):
    credit_id = int(request.POST['credit_id'])
    try:
        mark = CourseFinalMark.objects.get(credit_id=credit_id)
    except CourseFinalMark.DoesNotExist:
        mark = None
    return render(request, 'registrar/certificate/permalink_modal.html',{
        'mark': mark,
        'user': request.user,
        'tab': 'certificates',
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS
    })
