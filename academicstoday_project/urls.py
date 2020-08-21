from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static, settings
from django.contrib.auth import views
from django.urls import path, re_path


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    re_path(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    re_path(r'', include('landpage.urls', namespace='landpage')),
    re_path(r'', include('registration.urls', namespace='registration')),
    re_path(r'', include('login.urls', namespace='login')),
    re_path(r'', include('account.urls', namespace='account')),
    re_path(r'', include('registrar.urls', namespace='registrar')),
    re_path(r'', include('student.urls', namespace='student')),
    re_path(r'', include('teacher.urls', namespace='teacher')),
    re_path(r'', include('publisher.urls', namespace='publisher')),
    re_path(r'payment/', include('ecommerce_app.urls', namespace='ecommerce_app')),
    re_path(r'paypal/', include('paypal.standard.ipn.urls')),
    re_path('accounts/', include('django.contrib.auth.urls')),
    

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
