from django.conf.urls import  include, url

from registrar.views import courses
from registrar.views import enrollment
from registrar.views import teaching
from registrar.views import transcript
from registrar.views import certificate
from registrar.views import purchase
# from registrar.views import payment
app_name = 'registrar'

urlpatterns = [
    # Courses
    url(r'^courses$', courses.courses_page),
    url(r'^enroll$', courses.enroll),
    url(r'^shortcourses$', courses.shortcourses, name='shortcourses'),
    url(r'^enroll/shortcourse/(?P<id>\d+)/$', courses.enroll_short , name='enrollshort' ),
    url(r'^shortcourses/(?P<id>\d+)/$', courses.shortcourse_detail, name='shortcourse_detail'),


   

    # Enrollment(s)
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
    url(r'^make_purchase/(\d+)$', purchase.make_purchase, name='make_purchase'),
    url(r'^process_payment/1/', purchase.process_payment, name='process_payment'),
    # url(r'^payment-done/', payment.payment_done, name='payment_done'),
    # url(r'^payment-cancelled/', payment.payment_canceled, name='payment_cancelled'),
    # url(r'^paypal/', include('paypal.standard.ipn.urls')),
    


]


