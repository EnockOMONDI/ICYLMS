from django.conf.urls import patterns, include, re_path

from landpage.views import txt
from landpage.views import landpage
from landpage.views import privacy
from landpage.views import terms
from landpage.views import forgot_password
from landpage.views import google
from landpage.views import landpageprod

from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = patterns('',
    # Custom Files
    re_path(r'^robots\.txt$', txt.robots_txt_page, name='robots'),
    re_path(r'^humans\.txt$', txt.humans_txt_page, name='humans'),
                       
    # Google Verify
    re_path(r'^googlee81f1c16590924d1.html$', google.google_verify_page, name='google_plus_verify'),
    re_path(r'^googlee81f1c16590924d1$', google.google_verify_page),
                       
    # Landpage
    re_path(r'^$',landpageprod.landpageprod_page, name='landpageprod'),
    re_path(r'^landpage$', landpage.landpage_page),
    re_path(r'^course_preview_modal$', landpage.course_preview_modal),
    re_path(r'^save_contact_us_message$', landpage.save_contact_us_message),

     #productionpages
    re_path(r'^landpageprod$', landpageprod.landpageprod_page, name='landpageprod'),
    re_path(r'^welcome$', landpageprod.welcome, name='welcome'),
    re_path(r'^aboutus$', landpageprod.about_us, name='aboutus'),
    re_path(r'^contactus$', landpageprod.contact_us, name='contactus'),
    # re_path(r'^graduants$', landpageprod.graduants_page, name='graduantspage'),
    # re_path(r'^edit/', views.edit, name='edit'),
                       
    # Off-Convas Stuff
    re_path(r'^terms$', terms.terms_page, name='terms'),
    re_path(r'^privacy', privacy.privacy_page, name='privacy'),
    re_path(r'^forgot_password$', forgot_password.forgot_password_page, name='forgot_password'),
    re_path(r'^reset_password$', forgot_password.reset_password, name='reset_password'),
                       
    # Sitemap
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
)

# Captchas
urlpatterns += patterns('',
    re_path(r'^captcha/', include('captcha.urls')),
)