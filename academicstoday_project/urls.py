from django.conf.urls import include,re_path
from django.contrib import admin
from django.conf.urls.static import static, settings

urlpatterns = [
    # Examples:
    # re_path(r'^$', 'academicstoday_project.views.home', name='home'),
    # re_path(r'^blog/', include('blog.urls')),

    re_path(r'^admin/', include(admin.site.urls)),
               
    re_pathhis regex makes the default URL for the website to launch this view.
    re_path(r'', include('landpage.urls')),
    re_path(r'', include('registration.urls')),
    re_path(r'', include('login.urls')),
    re_path(r'', include('account.urls')),
    re_path(r'', include('registrar.urls')),
    re_path(r'', include('student.urls')),
    re_path(r'', include('teacher.urls')),
    re_path(r'', include('publisher.urls')),
    
]+ sre_pathic(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
re_pathre_pathre_path