from account.views import mail
# from account.views import Uprofile
from django.urls import  re_path
from account.views import setting
from account.views import donate
from account.views import *
from account.views import profile
from account.views import profileprod



urlpatterns = [
   re_path(r'^profile$', profile.profile_page),
   re_path(r'^update_user$', profile.update_user),
   re_path(r'^inbox$', mail.mail_page),
   re_path(r'^send_private_message$', mail.send_private_message),
   re_path(r'^view_private_message$', mail.view_private_message),
   re_path(r'^delete_private_message$', mail.delete_private_message),
   re_path(r'^settings$', setting.settings_page),
   re_path(r'^update_password$', setting.update_password),
   re_path(r'^donate$', donate.donate_page),
    #productionurls
   re_path(r'^profileprod$', profileprod.profileprod),
   re_path(r'^editprod$', profileprod.editprod),
   re_path(r'^update_profile$', profile.update_profile),
   re_path(r'^view/profil/', profile.view_profil, ),

]