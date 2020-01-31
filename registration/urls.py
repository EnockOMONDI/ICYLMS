from django.conf.urls import include, re_path
from . import views
from .views import *


urlpatterns = [
    re_path(r'^register_modal$', views.register_modal),
    re_path(r'^register$', views.register),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
  
]