import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from registration.form import RegisterForm
from django.db import transaction
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import send_mail



def register_modal(request):
    form = RegisterForm()
    return render(request, 'register/modal.html',{
        'form': form,
    })
def create_user(form):
    # Create the user in our database
    email = form['email'].value().lower()
    try:
        user = User.objects.create_user(
            email,  # Username
            email,  # Email
            form['password'].value(),
        )
        user.first_name = form['first_name'].value()
        user.last_name = form['last_name'].value()
        user.is_active = True   # Need email verification to change status.
        user.save()
        send_mail('Subject here','Here is the message.',settings.EMAIL_HOST_USER,[email],fail_silently=False,))
        
    except Exception as e:
        return {
            'status' : 'failure',
            'message' : 'An unknown error occured, failed registering user.'
    }

    # Return success status
    return {
        'status' : 'success',
        'message' : 'user registered'
        
    }



   
def register(request):
    response_data = {}
    if request.is_ajax():
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            # Validate the form: the captcha field will automatically
            # check the input
            if form.is_valid():
                response_data = create_user(form)
               

                
            else:
                response_data = {'status' : 'failed', 'message' : json.dumps(form.errors)}
                
    else:
        response_data = {'status' : 'failure', 'message' : 'Not acceptable request made.' }
    return HttpResponse(json.dumps(response_data),content_type="application/json",)


def activation_sent_view(request):
    return render(request, 'register/activation_sent.html')    





    

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
