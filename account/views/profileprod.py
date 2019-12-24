from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json
from registrar.models import Student
from registrar.models import Course
from registrar.models import Announcement
from account.forms import UserForm



def profileprod(request):
    return render(request, 'account/productionpages/pages/profile.html',{
        'user': request.user,
        'form': UserForm(instance=request.user),
        'tab': 'profileprod',
        'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })


def editprod(request):
    title = 'LADA | edit profile'
    # current_user = request.user
    # if request.method == 'POST':
    #     form = EditProfileForm(request.POST,request.FILES)
    #     if form.is_valid():
    #         update = form.save(commit=False)
    #         update.user = current_user
    #         update.save()
    #         # return redirect('/profileprod')
    # else:
    #     form = EditProfileForm()
    return render(request,'account/productionpages/pages/edit.html', { 
        # "title":title,
        # "form":form,
        'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })      