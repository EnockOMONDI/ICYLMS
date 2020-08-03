from django.shortcuts import render
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json
from landpage.models import CoursePreview
from registrar.models import *
from registrar.forms import CourseForm
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.utils.translation import gettext as _
from django.urls import reverse_lazy, reverse



@login_required(login_url='/login_modal')
def courses_page(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    courses = Course.objects.filter(status=settings.COURSE_AVAILABLE_STATUS)
    course_list = Course.objects.filter(status=settings.COURSE_AVAILABLE_STATUS)
 
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        courses = Course.objects.filter(category=category)
   

    # Create our student account which will build our registration around.
    try:
         student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
         student = Student.objects.create(user=request.user)

    # Only fetch teacher and do not create new teacher here.
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        teacher = None

    return render(request, 'ecommerce_app/courses/courses2.html',context={
        'category': category,
        'categories': categories,
        'courses' : courses,
        'student' : student,
        'teacher' : teacher,
        'user' : request.user,
        'tab' : 'courses',
        'HAS_ADVERTISMENT': settings.APPLICATION_HAS_ADVERTISMENT,
        'local_css_urls' : settings.SB_ADMIN_COURSE_LIST_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_COURSE_LIST_JS_LIBRARY_URLS
    })

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    # Create our student account which will build our registration around.
    try:
         student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
         student = Student.objects.create(user=request.user)

    # Only fetch teacher and do not create new teacher here.
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        teacher = None
    try:
        lectures = Lecture.objects.filter(course_id=course_id).order_by('week_num', 'lecture_num')
    except Lecture.DoesNotExist:
        lectures = None
    return render(request, 'ecommerce_app/courses/coursedetail.html',context= {
    'course' : course,
     'student' : student,
     'teacher' : teacher,
     'lectures':lectures,
     'user' : request.user,
     'local_css_urls' : settings.SB_ADMIN_COURSE_DETAIL_CSS_LIBRARY_URLS,
    'local_js_urls' : settings.SB_ADMIN_COURSE_DETAIL_JS_LIBRARY_URLS, 
     'local_plugins_urls ':settings.SB_ADMIN_COURSE_DETAIL_CSS_PLUGINS_URLS})    


@login_required()
def enroll(request, course_id):
    response_data = {'status' : 'failure', 'message' : 'unsupported request format'}
    if request.is_ajax():
        course_id = int(request.POST['course_id'])
        student = Student.objects.get(user=request.user)
        course = Course.objects.get(id=course_id)

        # Lookup the course in the students enrollment history and if the
        # student is not enrolled, then enroll them now.
        try:
            Course.objects.get(
                students__student_id=student.student_id,
                id=course_id
            )
        except Course.DoesNotExist:
            course.students.add(student)
        response_data = {'status' : 'success', 'message' : 'enrolled' }

    return HttpResponse(json.dumps(response_data), content_type="application/json")

# Developer Notes: Pagination
# https://docs.djangoproject.com/en/1.8/topics/pagination/

def enroll_course(request,id):
    if request.method=='POST':
        course = get_object_or_404(Course, id=id)
        student = Student.objects.get(user=request.user)
        course.students.add(student)
        messages.success(request, _('you have successfully enrolled'))
        return redirect('student:announcements_page', id)

