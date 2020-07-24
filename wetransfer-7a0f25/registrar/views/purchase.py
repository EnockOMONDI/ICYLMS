from django.shortcuts import render, HttpResponse, redirect,get_object_or_404, reverse
from django.contrib import messages
from django.conf import settings
from registrar.models import Course, Purchase_Course

from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from registrar.models import Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout




def make_purchase(request):
    course = get_object_or_404(Course, pk=course_id)
    student = get_object_or_404(User, user=request.user)
    purchase_course = Purchase_Course.objects.get_or_create(student=student,course=course)
    return redirect('process_payment')

    
def make_purchases(request,id):
    course = get_object_or_404(Course, id=course_id)
    student = get_object_or_404(User, user=request.user)
    purchase_course = Purchase_Course.objects.get_or_create(student=student,course=course)
                                                

    if request.method == 'POST':
        form = CartForm(request, request.POST)
        if form.is_valid():
            request.form_data = form.cleaned_data
            cart.add_item_to_cart(request)
            return redirect('show_cart')

    
    form = CartForm(request, initial={'course_id': course.id})
    return render(request, 'registrar/payment/course_detail.html', {
                                            'course': course,
                                            'form': form,
                                            })


def show_cart(request):

    if request.method == 'POST':
        if request.POST.get('submit') == 'Update':
            cart.update_item(request)
        if request.POST.get('submit') == 'Remove':
            cart.remove_item(request)

    cart_items = cart.get_all_cart_items(request)
    cart_subtotal = cart.subtotal(request)
    return render(request, 'registrar/payment/cart.html', {
                                            'cart_items': cart_items,
                                            'cart_subtotal': cart_subtotal,
                                            })


def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            o = Order(
                name = cleaned_data.get('name'),
                email = cleaned_data.get('email'),
                postal_code = cleaned_data.get('postal_code'),
                address = cleaned_data.get('address'),
            )
            o.save()

            all_items = cart.get_all_cart_items(request)
            for cart_item in all_items:
                li = LineItem(
                    course_id = cart_item.course_id,
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
        form = CheckoutForm()
        return render(request, 'registrar/payment/checkout.html', locals())

def process_payment(request,course_id):
    course = get_object_or_404(Course, pk=course_id)
    student = get_object_or_404(User, user=request.user)
    purchase_course = Purchase_Course.objects.get_or_create(student=student,course=course)
    host = request.get_host()
 
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': purchase_course.price,
        'item_name':purchase_course.course.title,
        'invoice': str(purchase_course.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('payment_cancelled')),
    }
 
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'registrar/payment/process_payment.html', {' purchase_course': purchase_course , 'form': form})

@csrf_exempt
def payment_done(request):
    return render(request, 'registrar/payment/payment_done.html')
 
 
@csrf_exempt
def payment_canceled(request):
    return render(request, 'registrar/payment/payment_cancelled.html')