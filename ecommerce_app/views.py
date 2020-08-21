from django.shortcuts import render, HttpResponse, redirect, \
    get_object_or_404, reverse
from django.contrib import messages
from django.conf import settings
from .models import Product, ShortCourse, Order, LineItem, ShortCourseLecture
from .forms import CartForm, CheckoutForm
from . import cart
from decimal import Decimal
from .models import Product
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json
from registrar.models import Student
from registrar.models import Teacher







def index(request):
    all_products = Product.objects.all()
    return render(request, "ecommerce_app/index.html", {
     'all_products': all_products,
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })

def home(request):
    all_products = Product.objects.all()
    return render(request, "ecommerce_app/courses/courses.html", {
     'all_products': all_products,
     'local_css_urls' : settings.SB_ADMIN_COURSE_LIST_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_COURSE_LIST_JS_LIBRARY_URLS
          })

def shortcoursedetail(request):
    return render(request, 'ecommerce_app/shortcoursedetail/detail-4.html',{
        'tab': 'shortcoursedetail',
     'local_css_urls' : settings.SB_ADMIN_COURSE_DETAIL_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_COURSE_DETAIL_JS_LIBRARY_URLS
          })
def shortcoursedetail2(request):
    return render(request, 'ecommerce_app/shortcoursedetail/detail-2.html',{
        'tab': 'shortcoursedetail2',
     'local_css_urls' : settings.SB_ADMIN_COURSE_DETAIL_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_COURSE_DETAIL_JS_LIBRARY_URLS
          })

def shortcourseindex(request):
    all_shortcourse = ShortCourse.objects.all()
  
    try:
         student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
         student = Student.objects.create(user=request.user)

    # Only fetch teacher and do not create new teacher here.
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        teacher = None

    return render(request, "ecommerce_app/shortcourseindex.html", {
      'all_shortcourse': all_shortcourse,
      'student' : student,
      'teacher' : teacher,
      'user' : request.user,
      'tab' : 'shortcourses',
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })



@login_required(login_url='/landpage')
def shortcourselectures_page(request, shortcourse_id):
    shortcourse = ShortCourse.objects.get(id=shortcourse_id)
    try:
        shortcourselectures = ShortCourseLecture.objects.filter(shortcourse_id=shortcourse_id).order_by('week_num', 'lecture_num')
    except ShortCourseLecture.DoesNotExist:
        shortcourselectures = None
    return render(request, 'ecommerce_app/details.html',{
        'shortcourse' : shortcourse,
        'shortcourselectures' : shortcourselectures,
        'NO_VIDEO_PLAYER': settings.NO_VIDEO_PLAYER,
        'YOUTUBE_VIDEO_PLAYER': settings.YOUTUBE_VIDEO_PLAYER,
        'VIMEO_VIDEO_PLAYER': settings.VIMEO_VIDEO_PLAYER,
        'BLIPTV_VIDEO_PLAYER': settings.BLIPTV_VIDEO_PLAYER,
        'user' : request.user,
        'tab' : 'lectures',
        'HAS_ADVERTISMENT': settings.APPLICATION_HAS_ADVERTISMENT,
        'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })


@login_required()
def shortcourseenroll(request):
    response_data = {'status' : 'failure', 'message' : 'unsupported request format'}
    if request.is_ajax():
        shortcourse_id = int(request.POST['shortcourse_id'])
        student = Student.objects.get(user=request.user)
        shortcourse = ShrotCourse.objects.get(id=shortcourse_id)

        # Lookup the course in the students enrollment history and if the
        # student is not enrolled, then enroll them now.
        try:
            ShortCourse.objects.get(
                students__student_id=student.student_id,
                id=shortcourse_id
            )
        except ShortCourse.DoesNotExist:
            shortcourse.students.add(student)
        response_data = {'status' : 'success', 'message' : 'enrolled to th short course' }

    return HttpResponse(json.dumps(response_data), content_type="application/json")



@login_required(login_url='/landpage')
def shortcourseenrollment_page(request):
    # Create our student account which will build our registration around.
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        student = Student.objects.create(user=request.user)
    try:
        shortcourses = ShortCourse.objects.filter(students__student_id=student.student_id)
    except ShortCourse.DoesNotExist:
        shortcourses = None
    return render(request, 'ecommerce_app/view.html',{
        'student' : student,
        'shortcourses': shortcourses,
        'user' : request.user,
        'tab' : 'shortcourseenrollment',
        'HAS_ADVERTISMENT': settings.APPLICATION_HAS_ADVERTISMENT,
        'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
    })


@login_required()
def shortcourseenrollment_table(request):
    # Create our student account which will build our registration around.
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        student = Student.objects.create(user=request.user)
    try:
        shortcourses = ShortCourse.objects.filter(students__student_id=student.student_id)
    except ShortCourse.DoesNotExist:
        shortcourses = None
    return render(request, 'ecommerce_app/table.html',{
        'student' : student,
        'shortcourses': shortcourses,
        'user' : request.user,
        'tab' : 'shortcourseenrollment',
    })

@login_required()
def shortcoursedisenroll_modal(request):
    # Create our student account which will build our registration around.
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        student = Student.objects.create(user=request.user)

    shortcourse_id = int(request.POST['shortcourse_id'])
    try:
        shortcourse = ShortCourse.objects.get(id=shortcourse_id)
    except ShortCourse.DoesNotExist:
        shortcourse = None
    return render(request, 'ecommerce_app/disenroll_modal.html',{
        'student' : student,
        'shortcourse': shortcourse,
        'user' : request.user,
    })


@login_required()
def shortcoursedisenroll(request):
    response_data = {'status' : 'failure', 'message' : 'unsupported request format'}
    if request.is_ajax():
        shortcourse_id = int(request.POST['course_id'])
        student = Student.objects.get(user=request.user)
        try:
            shortcourse = ShortCourse.objects.get(id=shortcourse_id)
            shortcourse.students.remove(student)
            response_data = {'status' : 'success', 'message' : 'disenrolled' }
        except ShortCourse.DoesNotExist:
            response_data = {'status' : 'failed', 'message' : 'record does not exist' }
    return HttpResponse(json.dumps(response_data), content_type="application/json")
def show_cart(request):
    if request.method == 'POST':
        if request.POST.get('submit') == 'Update':
            cart.update_item(request)
        if request.POST.get('submit') == 'Remove':
            cart.remove_item(request)

    cart_items = cart.get_all_cart_items(request)
    cart_subtotal = cart.subtotal(request)
    return render(request, 'ecommerce_app/cart.html', {
      'cart_items': cart_items,
      'cart_subtotal': cart_subtotal,
       'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })

def show_product(request, product_id, product_slug):
    product = get_object_or_404(Product, id=product_id)
    modules =product.modules.all()
    if request.method == 'POST':
        form = CartForm(request, request.POST)
        if form.is_valid():
            request.form_data = form.cleaned_data
            cart.add_item_to_cart(request)
            return redirect('show_cart')
           

    
    form = CartForm(request, initial={'product_id': product.id})
    return render(request, 'ecommerce_app/product_detail.html', {
                                            'product': product,
                                            'modules': modules,
                                            'form': form,
    'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
    'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
    })

def show_units(request, product_id, modules_id, product_slug):
    module = get_object_or_404(Modules, id=modules_id)
    units = module.units.all()
    if request.method == 'POST':
        form = CartForm(request, request.POST)
        if form.is_valid():
            request.form_data = form.cleaned_data
            cart.add_item_to_cart(request)
            return redirect('show_cart')
           

    
    form = CartForm(request, initial={'product_id': product.id})
    return render(request, 'ecommerce_app/module_units.html', {
                                            'product': product,
                                            'modules': modules,
                                            'form': form,
                                            'units': units,
    'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
    'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
    })






def checkout(request):
   
    if request.method == 'POST':
        form = CheckoutForm(request, request.POST)
        
        if form.is_valid():
            request.form_data = form.cleaned_data
            data = request.form_data
            o = Order(
                name = data.get('name'),
                email =data.get('email'),
             
            )
            o.save()

            all_items = cart.get_all_cart_items(request)
            for cart_item in all_items:
                li = LineItem(
                    product_id = cart_item.product_id,
                    price = cart_item.price,
                    quantity = cart_item.quantity,
                    order_id = o.id
                )

                li.save()

            cart.clear(request)

            request.session['order_id'] = o.id

            messages.add_message(request, messages.INFO, 'Order Placed!')
            return redirect('process_payment')
    else:
        form = CheckoutForm(request)
        return render(request, 'ecommerce_app/checkout.html',
        { 
        'form':form,
        'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
            })
     
    

def process_payment(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()
 
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % order.total_cost(),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',
        'notify_url': 'https://www.leadershipanddevelopmentacademy.com/paypal/',
                                         
        'return_url': 'https://www.leadershipanddevelopmentacademy.com/payment/payment-done/',
        'cancel_return': 'https://www.leadershipanddevelopmentacademy.com/payment/payment-cancelled/'
                                             
    }
 
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'ecommerce_app/process_payment.html', {'order': order, 'form': form,
        'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })

@csrf_exempt
def payment_done(request):
    return render(request, 'ecommerce_app/payment_done.html',
       {   'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          },)
 
 
@csrf_exempt
def payment_canceled(request):
    return render(request, 'ecommerce_app/payment_cancelled.html',
       {   'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          },)