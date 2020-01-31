from django.conf.urls import include, re_path
from . import views
from django.urls import  re_path
urlpatterns = [
    re_path(r'^login_modal$', views.login_modal),
    re_path(r'^login$', views.login_authentication),
    re_path(r'^logout$', views.logout_authentication),

]