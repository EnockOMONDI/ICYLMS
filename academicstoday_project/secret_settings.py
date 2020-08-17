import sys
import cloudinary
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

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'leadershipacademyafrica@gmail.com'
EMAIL_HOST_PASSWORD = 'hrznsyzmgrrvlkhl'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Leadership and development academy <info@leadershipanddevelopmentacademy.com>'



# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'apikey'
# EMAIL_HOST_PASSWORD = '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'
# EMAIL_USE_TLS = True
 
PAYPAL_RECEIVER_EMAIL = 'africaforsdgs2019@gmail.com'
PAYPAL_TEST = False  
PAYPAL_CLIENT_ID = 'AYxM9ft3x-ODD8P60XP1fI7cljyjve2vY3Oaa2rzsyIMad7VcxhJABtlJBzhcP6-eztRghDfg3kn4Ato'
PAYPAL_CLIENT_SECRET = 'EDe6n1w19IPRTPdBwm10QSBxyF5o9ZEeH0R7mSJeI7yGLvhMS-7mOwMgcNPhUZg6zUpPUlnKsIDWE3Y3'

# PAYPAL_RECEIVER_EMAIL = 'rennyopascal@gmail.com'
# PAYPAL_TEST = False  
# PAYPAL_CLIENT_ID = 'AXvkBngcxRDy96UenCWYPR5BPzGo-N40NT5wj1n7yeRiTtGq-U8qTbJQlznNY9uQ9lGb7pkPbImbCYzd'
# PAYPAL_CLIENT_SECRET = 'EFZ6RzSswSiZpM3AwZ_HVIjEfE0UP-SYKv_NMALWhe7Ula-tP_3kqJjI5UxqEF76S3ZD7AFlhug4eTb_'
UPLOADCARE = {
  # Don’t forget to set real keys when it gets real :)

  'pub_key': 'd4d69f96f2e2dde353d1',
  'secret': 'a31559dd611e70c202f4',
}

cloudinary.config(
  cloud_name ='lada' ,
  api_key = '991846289858872',
  api_secret = 'PxriDvQELG9426d-3KZ1_OtbsVE',
  secure = True
)


#---------------------------------------------------------------------------#
# Application Specific Settings                                             #
#---------------------------------------------------------------------------#
# (Disable Ads when running Unit-Tests)
if 'test' in sys.argv:
    APPLICATION_HAS_ADVERTISMENT = False  # (DO NOT MODIFY)
else:
    APPLICATION_HAS_ADVERTISMENT = False  # (True = Yes I want advertisments)
APPLICATION_HAS_PUBLIC_ACCESS_TO_TEACHERS = True