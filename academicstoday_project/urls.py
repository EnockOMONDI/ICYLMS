from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static, settings
from django.contrib.auth import views
from django.urls import path, re_path


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    re_path(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    re_path(r'', include('landpage.urls')),
    re_path(r'', include('registration.urls')),
    re_path(r'', include('login.urls')),
    re_path(r'', include('account.urls')),
    re_path(r'', include('registrar.urls')),
    re_path(r'', include('student.urls')),
    re_path(r'', include('teacher.urls')),
    re_path(r'', include('publisher.urls')),
    re_path(r'payment/', include('ecommerce_app.urls')),
    re_path(r'paypal/', include('paypal.standard.ipn.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
