from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static, settings
from django.contrib.auth import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'academicstoday_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^admin/', include(admin.site.urls)),
               
    # This regex makes the default URL for the website to launch this view.
    url(r'', include('landpage.urls')),
    url(r'', include('registration.urls')),
    url(r'', include('login.urls')),
    url(r'', include('account.urls')),
    url(r'', include('registrar.urls')),
    url(r'', include('student.urls')),
    url(r'', include('teacher.urls')),
    url(r'', include('publisher.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
