from django.conf.urls import  include, url
from . import views

urlpatterns = [
    url(r'^login_modal$', views.login_modal),
    url(r'^redirected_login$', views.login_redirect),
    url(r'^redirectedlogin$', views.trainingbits_redirect),
    url(r'^login$', views.login_authentication),
    url(r'^logout$', views.logout_authentication),

]