from django.urls import include
from django.urls import path, re_path
from . import views

app_name='ecommerce_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('product/<int:product_id>/<slug:product_slug>/',views.show_product, name='product_detail'),
    path('product/<int:module_id>/<slug:product_slug>/',views.show_units, name='module_detail'),
    path('cart/', views.show_cart, name='show_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('process-payment', views.process_payment, name='process_payment'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
    # path('short/(\d+)', views.shortcoursedetail, name='shortcoursedetail'),
    path('short2/', views.shortcoursedetail2, name='shortcoursedetail'),
    path('shortcourse/', views.shortcourseindex),
  

    path('shortcourseenroll/<int:shortcourse_id>/<slug:shortcourse_slug>/', views.shortcourseenroll),
    path('shortcourseenrollment/', views.shortcourseenrollment_page),
    path('shortcourseenrollment_table$/<int:shortcourse_id>/<slug:shortcourse_slug>/', views.shortcourseenrollment_table),
    path('shortcoursedisenroll_modal/<int:shortcourse_id>/<slug:shortcourse_slug>/', views.shortcoursedisenroll_modal),
    path('shortcoursedisenroll/<int:shortcourse_id>/<slug:shortcourse_slug>/', views.shortcoursedisenroll),
    path('shortcourse/<int:shortcourse_id>/',views.shortcourselectures_page, name='shortcourselectures_page'),

]
