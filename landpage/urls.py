from django.urls import include
from django.urls import path, re_path
from landpage.views import txt
from landpage.views import landpage
from landpage.views import privacy
from landpage.views import terms
from landpage.views import forgot_password
from landpage.views import google
from landpage.views import landpageprod
from landpage.views import publicpages

from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

app_name = 'landpage'
sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    # Custom Files
    re_path(r'^robots\.txt$', txt.robots_txt_page, name='robots'),
    re_path(r'^humans\.txt$', txt.humans_txt_page, name='humans'),
                       
    # Google Verify
    re_path(r'^googlee81f1c16590924d1.html$', google.google_verify_page, name='google_plus_verify'),
    re_path(r'^googlee81f1c16590924d1$', google.google_verify_page),

    # publicpages
    re_path(r'^$', publicpages.home_page, name='home'),
    re_path(r'^welcome/', publicpages.welcome, name='welcome'),
    re_path(r'^home_page$', publicpages.home_page, name='homepage'),
    re_path(r'^platformoverview$', publicpages.platform_overview, name='platformoverview'),
    re_path(r'^ourstory$', publicpages.our_story, name='ourstory'),
    re_path(r'^scholarship$', publicpages.scholarship , name='scholarship'),
    re_path(r'^contact$', publicpages.contactus , name='contact'),
    re_path(r'^programs/', publicpages.programs, name='programs'), 
    re_path(r'^videos/', publicpages.videos, name='videos'),   
    re_path(r'^events/', publicpages.product_list, name='product_list'),
    re_path(r'^media/', publicpages.media_list, name='media_list'),
    re_path(r'^blog/', publicpages.blog_list, name='blog_list'),
    re_path(r'^pastevents/', publicpages.events404, name='events404'),
    re_path(r'^contact/', publicpages.contact, name='contact'),
    re_path(r'^appointement/', publicpages.appointement, name='appointement'),
    re_path(r'^eventbooking/', publicpages.eventbooking, name='eventbooking'),
    re_path(r'^(?P<mediacategory_slug>[-\w]+)/$', publicpages.media_list, name='media_list_by_category'), 
    re_path(r'^(?P<blogcategory_slug>[-\w]+)/$', publicpages.blog_list, name='blog_list_by_category'), 
    re_path(r'^(?P<id>\d+)/(?P<blogcategory_slug>[-\w]+)/$', publicpages.blog_detail, name='blog_detail'),
   

                      
    # Landpage
    re_path(r'^$',landpageprod.landpageprod_page, name='landpageprod'),
    re_path(r'^landpage$', landpage.landpage_page),
    re_path(r'^course_preview_modal$', landpage.course_preview_modal),
    re_path(r'^save_contact_us_message$', landpage.save_contact_us_message),

     
     #productionpages
   
    re_path(r'^landpageprod$', landpageprod.landpageprod_page, name='landpageprod'),
    re_path(r'^aboutus$', landpageprod.about_us, name='aboutus'),
    re_path(r'^enrollnow$', landpageprod.enrollnow, name='enrollnow'),
    re_path(r'^studentfaqs$', landpageprod.studentfaqs, name='studentfaqs'),
    re_path(r'^sdgfaqs$', landpageprod.sdgfaqs, name='sdgfaqs'),
    re_path(r'^benefits', landpageprod.benefits, name=' benefits'),
    re_path(r'^contactus$', landpageprod.contactus, name='contactus'), 
    re_path(r'^sdgdigitallab$', landpageprod.sdgdigitallab, name='sdgdigitallab'), 
    re_path(r'^volunteerpage$', landpageprod.volunteer, name='volunteer'),
    re_path(r'^digitallab$', landpageprod.digitallab , name='digitallab '),
    re_path(r'^scholarship-application-form$', landpageprod.scholarship , name='scholarship2'),
    re_path(r'^paymentfaqs', landpageprod.paymentfaqs , name='paymentfaqs'),

    
    # re_path(r'^edit/', publicpages.edit, name='edit'),
                  
    # Off-Convas Stuff
    re_path(r'^terms$', terms.terms_page, name='terms'),
    re_path(r'^privacy', privacy.privacy_page, name='privacy'),
    re_path(r'^forgot_password$', forgot_password.forgot_password_page, name='forgot_password'),
    re_path(r'^reset_password$', forgot_password.reset_password, name='reset_password'),
                       
    # Sitemap
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.publicpages.sitemap'),
    re_path(r'^captcha/', include('captcha.urls')),
]