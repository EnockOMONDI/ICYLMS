import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404,HttpResponseRedirect
from registrar.models import *
from django.shortcuts import render, get_object_or_404
from landpage.models import Event, Media, Blog, BlogCategory, MediaCategory, EventCategory
from django.contrib.auth.models import User


#newhomepage         
def home_page(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    courses = Course.objects.filter(status=settings.COURSE_AVAILABLE_STATUS)
    course_list = Course.objects.filter(status=settings.COURSE_AVAILABLE_STATUS)
 
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        courses = Course.objects.filter(category=category)

        

    return render(request, 'publicpages/index.html',{
        'category': category,
        'categories': categories,
        'courses' : courses,
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

def welcome(request):
    return render(request, 'publicpages/welcome.html',{
    'tab': 'welcomepage',
  'local_css_urls' : settings.SB_ADMIN_COURSE_DETAIL_CSS_LIBRARY_URLS,
   'local_js_urls' : settings.SB_ADMIN_COURSE_DETAIL_JS_LIBRARY_URLS

 })


def product_list(request, eventcategory_slug=None):
    eventcategory = None
    eventcategories = EventCategory.objects.all()
    events = Event.objects.filter(available=True)
    if eventcategory_slug:
        eventcategory = get_object_or_404(EventCategory, slug=eventcategory_slug)
        events = Event.objects.filter(eventcategory=eventcategory)

    context = {
        'eventcategory': eventcategory,
        'eventcategories': eventcategories,
        'events': events
    }
    return render(request, 'publicpages/eventlist.html', context)

def blog_list(request, blogcategory_slug=None):
    blogcategory = None
    blogcategories = BlogCategory.objects.all()
    blogs = Blog.objects.filter(available=True)
    if blogcategory_slug:
        blogcategory = get_object_or_404(BlogCategory, slug=blogcategory_slug)
        blogs = Blog.objects.filter(blogcategory=blogcategory)

    context = {
        'blogcategory': blogcategory,
        'blogcategories': blogcategories,
        'blogs': blogs
    }
    return render(request, 'publicpages/bloglist.html', context)


def media_list(request, mediacategory_slug=None):
    mediacategory = None
    mediacategories = MediaCategory.objects.all()
    medias = Media.objects.filter(available=True)
    if mediacategory_slug:
        mediacategory = get_object_or_404(MediaCategory, slug=mediacategory_slug)
        medias = Media.objects.filter(mediacategory=mediacategory)

    context = {
        'mediacategory': mediacategory,
        'mediacategories': mediacategories,
        'medias': medias
    }
    return render(request, 'publicpages/medialist.html', context)







def blog_detail(request, id, blogcategory_slug):
    blog = get_object_or_404(Blog, id=id, slug=blogcategory_slug, available=True )
    context = {
        'blog': blog
        
    }
    return render(request, 'publicpages/blogdetail.html', context)


def programs(request):
  return render(request, 'publicpages/programs.html')

def videos(request):
  return render(request, 'publicpages/videos.html')

def contact(request):
  return render(request, 'publicpages/contact.html')

def events404(request):
  return render(request, 'publicpages/events404.html')

def appointement(request):
  return render(request, 'publicpages/bookingappointement.html')

def eventbooking(request):
  return render(request, 'publicpages/bookingevent.html')

