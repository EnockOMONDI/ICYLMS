from django.conf.urls import patterns, include, re_path
from django.urls import  re_pathfrom registrar.views import courses
from registrar.views import enrollment
from registrar.views import teaching
from registrar.views import transcript
from registrar.views import certificate

urlpatterns = patterns('',
    # Courses
    re_path(r'^courses$', courses.courses_page),
    re_path(r'^enroll$', courses.enroll),

    # Enrollment(s)
    re_path(r'^enrollment$', enrollment.enrollment_page),
    re_path(r'^enrollment_table$', enrollment.enrollment_table),
    re_path(r'^disenroll_modal$', enrollment.disenroll_modal),
    re_path(r'^disenroll', enrollment.disenroll),
         
    # Teaching
    re_path(r'^teaching$', teaching.teaching_page),
    re_path(r'^refresh_teaching_table$', teaching.refresh_teaching_table),
                       
    re_path(r'^course_modal$', teaching.course_modal),
    re_path(r'^save_course$', teaching.save_course),
    re_path(r'^delete_course_modal$', teaching.delete_course_modal),
    re_path(r'^course_delete$', teaching.course_delete),
                    
    # Transcript
    re_path(r'^transcript$', transcript.transcript_page),
                       
    # Certificate(s)
    re_path(r'^certificates$', certificate.certificates_page),
    re_path(r'^certificates_table$', certificate.certificates_table),
    re_path(r'^change_certificate_accessiblity$', certificate.change_certificate_accessiblity),
    re_path(r'^certificate/(\d+)$', certificate.certificate_page),
    re_path(r'^certificate_permalink_modal$', certificate.certificate_permalink_modal),
)
