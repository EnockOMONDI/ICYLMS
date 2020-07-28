from django.conf.urls import  include, url
from . import views

app_name="registration"
urlpatterns = [
    url(r'^register_modal$', views.register_modal),
    url(r'^register$', views.register),
    url(r'^redirected-register$', views.redirectedregister),
]