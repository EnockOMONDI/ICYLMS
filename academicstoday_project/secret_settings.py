import sys

#---------------------------------------------------------------------------#
# Generic                                                                   #
#---------------------------------------------------------------------------#
SECRET_DEBUG = True
SECRET_KEY = 'xd#vc@mec1c0+wz^y&_i^-og&oy$mkn%_yky&xe^fo()mio$up'
# SECRET_ALLOWED_HOSTS = ['*']


#---------------------------------------------------------------------------#
# Database                                                                  #
#---------------------------------------------------------------------------#
# SECRET_DB_USER = "sean"
# SECRET_DB_PASSWORD = "Aggreyomondi90"


#---------------------------------------------------------------------------#
# Email                                                                     #
#---------------------------------------------------------------------------#
SECRET_EMAIL_HOST = 'smpt.gmail.com'
SECRET_EMAIL_PORT = 578
SECRET_EMAIL_HOST_USER = 'enockomondike@gmail.com'
SECRET_EMAIL_HOST_PASSWORD = 'seanielllivekeke'
# settingspasswordis pass for settings@lada.com


#---------------------------------------------------------------------------#
# Application Specific Settings                                             #
#---------------------------------------------------------------------------#
# (Disable Ads when running Unit-Tests)
if 'test' in sys.argv:
    APPLICATION_HAS_ADVERTISMENT = False  # (DO NOT MODIFY)
else:
    APPLICATION_HAS_ADVERTISMENT = False  # (True = Yes I want advertisments)
APPLICATION_HAS_PUBLIC_ACCESS_TO_TEACHERS = True