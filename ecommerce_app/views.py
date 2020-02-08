from django.shortcuts import render, HttpResponse, redirect, \
    get_object_or_404, reverse
from django.contrib import messages
from django.conf import settings
from .models import Product, Order, LineItem
from .forms import CartForm, CheckoutForm
from . import cart
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    all_products = Product.objects.all()
    return render(request, "ecommerce_app/index.html", {
     'all_products': all_products,
     'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
          })


def show_product(request, product_id, product_slug):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = CartForm(request, request.POST)
        if form.is_valid():
            request.form_data = form.cleaned_data
            cart.add_item_to_cart(request)
            return redirect('show_cart')

    
    form = CartForm(request, initial={'product_id': product.id})
    return render(request, 'ecommerce_app/product_detail.html', {
                                            'product': product,
                                            'form': form,
    'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
    'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
    })


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


def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            o = Order(
                name = cleaned_data.get('name'),
                email = cleaned_data.get('email'),
             
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
        form = CheckoutForm()
        return render(request, 'ecommerce_app/checkout.html',
        # {   'local_css_urls' : settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        # 'local_js_urls' : settings.SB_ADMIN_2_JS_LIBRARY_URLS
        #   },
         locals())
     
    

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
        'notify_url': 'https://www.leadershipanddevelopmentacademy.com/payment/',
                                         
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