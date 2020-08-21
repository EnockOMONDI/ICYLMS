from django.conf.urls import  include, url

from registrar.views import courses
from registrar.views import enrollment
from registrar.views import teaching
from registrar.views import transcript
from registrar.views import certificate
from student.views import quickoverview
# from registrar.views import payment
app_name="registrar"
urlpatterns = [
    # Courses
    url(r'^courses$', courses.courses_page , name='courses'),
    url(r'^courses/(?P<category_slug>[-\w]+)/$', courses.courses_page, name='courses_list_by_category'),
    url(r'^course/(\d+)/$', courses.course_detail ,name='course_detail'),
    url(r'^enroll/(?P<id>\d+)/$', courses.enroll_course , name='enroll' ),

    url(r'^course/(\d+)/$', quickoverview.quickoverviews_page, name='quickoverview_page'),

    # Enrollment(s)
    url(r'^view/profile/enrollment$', enrollment.enrollment_page),
    url(r'^view/profile/', enrollment.enrollment_table),
    url(r'^view/profile/', enrollment.disenroll_modal),
    url(r'^view/profile/', enrollment.disenroll),
    url(r'^enrollment$', enrollment.enrollment_page),
    url(r'^enrollment_table$', enrollment.enrollment_table),
    url(r'^disenroll_modal$', enrollment.disenroll_modal),
    url(r'^disenroll', enrollment.disenroll),
         
    # Teaching
    url(r'^teaching$', teaching.teaching_page),
    url(r'^refresh_teaching_table$', teaching.refresh_teaching_table),
                       
    url(r'^course_modal$', teaching.course_modal),
    url(r'^save_course$', teaching.save_course),
    url(r'^delete_course_modal$', teaching.delete_course_modal),
    url(r'^course_delete$', teaching.course_delete),
                    
    # Transcript
    url(r'^view/profile/$', transcript.transcript_page),
    url(r'^transcript$', transcript.transcript_page),
                       
    # Certificate(s)
    url(r'^certificates$', certificate.certificates_page),
    url(r'^certificates_table$', certificate.certificates_table),
    url(r'^change_certificate_accessiblity$', certificate.change_certificate_accessiblity),
    url(r'^certificate/(\d+)$', certificate.certificate_page),
    url(r'^certificate_permalink_modal$', certificate.certificate_permalink_modal),
    # url(r'^allcourse/', payment.index, name='index'),
    # url(r'^course/<int:course_id>/',payment.show_course, name='course_detail'),
    # url(r'^cart/', payment.show_cart, name='show_cart'),
    # url(r'^checkout/', payment.checkout, name='checkout'),
    # url(r'^process-payment/', payment.process_payment, name='process_payment'),
    # url(r'^payment-done/', payment.payment_done, name='payment_done'),
    # url(r'^payment-cancelled/', payment.payment_canceled, name='payment_cancelled'),
    # url(r'^paypal/', include('paypal.standard.ipn.urls')),
    


]


