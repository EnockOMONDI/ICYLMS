# JavaScript Libraries
#                                 

SB_ADMIN_COURSE_DETAIL_CSS_LIBRARY_URLS =[
                              "assets_course_detail/css/styles.css",
                              "assets_course_detail/css/colors.css",
                              ]
SB_ADMIN_COURSE_DETAIL_JS_LIBRARY_URLS = [
                               "assets_course_detail/js/jquery.min.js",
		                       "assets_course_detail/js/popper.min.js",
		                       "assets_course_detail/js/bootstrap.min.js",
		                       "assets_course_detail/js/select2.min.js",
		                       "assets_course_detail/js/slick.js",
		                       "assets_course_detail/js/jquery.counterup.min.js",
		                       "assets_course_detail/js/counterup.min.js",
		                       "assets_course_detail/js/custom.js"
                              ] 
SB_ADMIN_COURSE_LIST_CSS_LIBRARY_URLS =[
                                        "assets_courses_list/vendor/perfect-scrollbar.css", 
                                        "assets_courses_list/vendor/fix-footer.css" ,
                                        "assets_courses_list/css/material-icons.css", 
                                        "assets_courses_list/css/fontawesome.css", 
                                        "assets_courses_list/css/preloader.css", 
                                        "assets_courses_list/css/app.css"
                                        ] 
SB_ADMIN_COURSE_LIST_JS_LIBRARY_URLS = [ 
                                        "assets_courses_list/vendor/jquery.min.js",
                                        "assets_courses_list/vendor/popper.min.js",
                                        "assets_courses_list/vendor/bootstrap.min.js",
                                        "assets_courses_list/vendor/perfect-scrollbar.min.js",
                                        "assets_courses_list/vendor/dom-factory.js",
                                        "assets_courses_list/vendor/material-design-kit.js",
                                        "assets_courses_list/vendor/fix-footer.js",
                                        "assets_courses_list/js/app.js"]
  

SB_ADMIN_2_CSS_LIBRARY_URLS =[                    
                            "css2/demo.css",
                             "css2/material-kit.min1036.css",   
                            "css2/vertical-nav.css"
                            ]
SB_ADMIN_2_JS_LIBRARY_URLS = [ "core/jquery.min.js",
                           "core/popper.min.js",
                           "core/bootstrap-material-design.min.js",
                           "js2/plugins/moment.min.js ",
                           "js2/plugins/bootstrap-datetimepicker.js",
                           "js2/plugins/nouislider.min.js", 
                           "js2/plugins/jquery.sharrre.js", 
                           "js2/plugins/bootstrap-tagsinput.js",            
                           "js2/plugins/bootstrap-selectpicker.js",                         
                           "js2/plugins/jasny-bootstrap.min.js",
                           "js2/plugins/jquery.flexisel.js",
                           "js2/modernizr.js",
                           "js2/vertical-nav.js",
                           "js2/buttons.js",
                           "js2/demo.js",
                           "js2/material-kit.min1036.js?v=2.1.1" ]

AGENCY_CSS_LIBRARY_URLS = [
    "js/jquery/1.11.1/jquery-ui.css",
    "js/bootstrap/3.3.2/css/bootstrap.min.css",
    "js/font-awesome/4.2.0/css/font-awesome.css",
    "js/font-awesome/4.2.0/css/font-awesome.min.css",
    "css/agency.css"
]

AGENCY_JS_LIBRARY_URLS = [
    "js/jquery/1.11.1/jquery.min.js",
    "js/jquery/1.11.1/jquery.tablesorter.js",
    "js/jquery/1.11.1/jquery-ui.js",
    "js/jquery-easing/1.3/jquery.easing.min.js",
    "js/bootstrap/3.3.2/js/bootstrap.min.js",
    "js/bootstrap/3.3.2/js/bootstrap.js",
    "js/classie/1.0.0/classie.js",
    "js/cbpanimatedheader/1.0.0/cbpAnimatedHeader.js",
    "js/cbpanimatedheader/1.0.0/cbpAnimatedHeader.min.js",
    "js/jqbootstrapvalidation/1.3.6/jqBootstrapValidation.js",
    "js/misc/agency.js"
]



# Custom Constants
#

# Question Types
ESSAY_QUESTION_TYPE = 1
MULTIPLECHOICE_QUESTION_TYPE = 2
TRUEFALSE_QUESTION_TYPE = 3
RESPONSE_QUESTION_TYPE = 4
QUESTION_TYPES = [
    ESSAY_QUESTION_TYPE,
    MULTIPLECHOICE_QUESTION_TYPE,
    TRUEFALSE_QUESTION_TYPE,
    RESPONSE_QUESTION_TYPE,
]

# Course Status
COURSE_UNAVAILABLE_STATUS = 0
COURSE_AVAILABLE_STATUS = 1
COURSE_SUBMITTED_FOR_REVIEW_STATUS = 2
COURSE_IN_REVIEW_STATUS = 3
COURSE_REJECTED_STATUS = 4
SHORT_COURSE_UNAVAILABLE_STATUS = 0
SHORT_COURSE_AVAILABLE_STATUS = 1
SHORT_COURSE_SUBMITTED_FOR_REVIEW_STATUS = 2
SHORT_COURSE_IN_REVIEW_STATUS = 3
SHORT_COURSE_REJECTED_STATUS = 4

# Video player choices
NO_VIDEO_PLAYER = '0'
YOUTUBE_VIDEO_PLAYER = '1'
VIMEO_VIDEO_PLAYER = '2'
BLIPTV_VIDEO_PLAYER = '3'

# File Upload Types
UNKNOWN_FILE_UPLOAD_TYPE = 0
PDF_FILE_UPLOAD_TYPE = 1
