from django.shortcuts import render
from django.core import serializers
from django.core.mail import send_mail

import json
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import  BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes



def login_modal(request):
    return render(request, 'login/modal.html',{
         'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })

def login_redirect(request):
    return render(request, 'login/login.html',{
         'local_css_urls' : settings.SB_ADMIN_2020UI_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2020UI_JS_LIBRARY_URLS
          })

def trainingbits_redirect(request):
    return render(request, 'login/login2.html',{
         'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })


def login_authentication(request):
    response_data = {'status' : 'failure', 'message' : 'an unknown error occured'}
    if request.is_ajax():
        if request.method == 'POST':
            user = authenticate(
                username=request.POST.get('username').lower(),
                password=request.POST.get('password')
            )
            
            # Does the user exist for the username and has correct password?
            if user is not None:
                # Is user suspended or active?
                if user.is_active:
                    response_data = {'status' : 'success', 'message' : 'logged on'}
                    login(request, user)
                else:
                    response_data = {'status' : 'failure', 'message' : 'you are suspended'}
            else:
                response_data = {'status' : 'failure', 'message' : 'wrong username or password'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def logout_authentication(request):
    response_data = {'status' : 'success', 'message' : 'you have been succesfully  logged off'}
    if request.is_ajax():
        if request.method == 'POST':
            logout(request)
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "registration/password_reset_email.html"
					c = {
					"email":user.email,
					'domain':'leadershipanddevelopmentacademy.com',
					'site_name': 'LADA',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'https',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'leadershipacademyafrica@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("accounts/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="login/password_reset.html", context={"password_reset_form":password_reset_form})
