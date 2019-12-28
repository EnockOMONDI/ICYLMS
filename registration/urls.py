from django.conf.urls import patterns, include, url
from . import views
from .views import *


urlpatterns = patterns('',
    url(r'^register_modal$', views.register_modal),
    url(r'^register$', views.register),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
  
    url(r'^sent$', activation_sent_view, name="activation_sent"), 
    url(r'^send$', views.send_email, name="activation_sent"), 
)