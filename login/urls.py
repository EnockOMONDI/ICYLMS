from django.conf.urls import  include, url
from django.urls import  include, re_path, path
from django.contrib.auth import views as auth_views
from . import views
app_name="login"
urlpatterns = [
	path('accounts/password_reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='login/password_reset.html',
             email_template_name='registration/password_reset_email.html',
             subject_template_name='registration/password_reset_subject.txt',
        ),
       name='password_reset'),
    path('accounts/password_reset/', views.password_reset_request, name='password_reset'),

    # path('accounts/change-password/', auth_views.PasswordChangeView.as_view(template_name='login/password_change.html'), name='password_change'),
    # path('accounts/password_change/done/', auth_views.PasswordChangeView.as_view(template_name='login/password_change.html'), name='password_change_done'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='login/password_reset_done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',  auth_views.PasswordResetConfirmView.as_view(template_name='login/password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='login/password_reset_complete.html'), name='password_reset_complete'),
    url(r'^login_modal$', views.login_modal),
    url(r'^redirected_login$', views.login_redirect),
    url(r'^redirectedlogin$', views.trainingbits_redirect),
    url(r'^login$', views.login_authentication),
    url(r'^logout$', views.logout_authentication),

]