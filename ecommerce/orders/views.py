import time
import json

import stripe
import requests

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect

# Create your views here.

from accounts.forms import UserAddressForm
from accounts.models import UserAddress
from carts.models import Cart, CartItem

from orders.forms import OrderCancellationRequestForm

from orders.models import Order, OrderCancellationRequest
from products.models import Variation
from .utils import id_generator

try:
    stripe_pub = settings.STRIPE_PUBLISHABLE_KEY
    stripe_secret = settings.STRIPE_SECRET_KEY
except Exception, e:
    print str(e)
    raise NotImplementedError(str(e))

try:
    razor_key_id = settings.RAZORPAY_KEY_ID
    razor_secret = settings.RAZORPAY_SECRET_KEY
except Exception, e:
    print str(e)
    raise NotImplementedError(str(e))


stripe.api_key = stripe_secret


def orders(request):
    """Orders."""
    context = {}
    orders = Order.objects.filter(user=request.user)
    return_product = OrderCancellationRequestForm()
    context = {"orders": orders, "return_product": return_product}
    template = "orders/orders.html"
    return render(request, template, context)


# require user login **
@login_required
def checkout(request):
    """Checkout."""
    # import ipdb; ipdb.set_trace()
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse("cart"))

    try:
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        if cart_items.count() < 1:
            return HttpResponseRedirect(reverse("cart"))

        for item in cart_items:
            variant = Variation.objects.get(id=item.variation.id)
            if item.quantity > variant.quantity:
                return HttpResponseRedirect(reverse("cart"))
    except:
        pass

    for item in cart_items:
        if item.variation.quantity <= 0:
            return HttpResponseRedirect(reverse("cart"))

    # Getting or creating new Order
    try:
        new_order = Order.objects.get(cart=cart)
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cart = cart
        new_order.user = request.user
        new_order.order_id = id_generator()
        new_order.save()

    except:
        new_order = None
        # work on some error message
        return HttpResponseRedirect(reverse("cart"))

    # Saving Order in CartItem.
    try:
        cart_order = Order.objects.get(order_id=new_order.order_id)
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            if not cart_item.order:
                cart_item.order = cart_order
                cart_item.save()
    except:
        print "Failed to save Order in CartItem. Please Check the checkout view in Orders."

    # Calculating final amount
    final_amount = 0
    if new_order is not None:
        new_order.sub_total = cart.total
        new_order.save()
        final_amount = new_order.get_final_amount()

    # Adding address
    try:
        address_added = request.GET.get("address_added")
    except:
        address_added = None

    if address_added is None:
        address_form = UserAddressForm()
    else:
        address_form = None

    current_addresses = UserAddress.objects.filter(user=request.user)
    billing_addresses = UserAddress.objects.get_billing_addresses(user=request.user)
    print billing_addresses

    # Saving nessary info at Stripe

    if request.method == "POST":
        shipping_a = request.POST['shipping_address']

        try:
            shipping_address_instance = UserAddress.objects.get(id=shipping_a)
        except:
            shipping_address_instance = None

        try:
            razor_payment_id = request.POST['razorpay_payment_id']
            url = 'https://api.razorpay.com/v1/payments/%s' % razor_payment_id
            resp = requests.get(url, data={}, auth=(razor_key_id, razor_secret))
            response = json.loads(resp.content)
            if response['error_code'] == "" or response['error_code'] == None:
                for x in new_order.cartitem_set.all():
                    x.status = "Placed"
                    x.save()
                new_order.razor_payment_id = response['id']
                new_order.payment = "Paid"
                new_order.shipping_address = shipping_address_instance
                new_order.save()
                del request.session['cart_id']
                del request.session['items_total']
                import ipdb; ipdb.set_trace()
                for item in cart_items:
                    variant = Variation.objects.get(id=item.variation.id)
                    variant.quantity -= item.quantity
                messages.success(request, "Thank your order. It has been completed!")
                return HttpResponseRedirect(reverse("user_orders"))

        except:
            messages.error(request, 'Payment Failed. Please try again later!')
            return HttpResponseRedirect(reverse("checkout"))

    context = {
        "order": new_order,
        "address_form": address_form,
        "current_addresses": current_addresses,
        "billing_addresses": billing_addresses,
        "final_amount": final_amount,
        "stripe_pub": stripe_pub,
        "razor_key_id": razor_key_id}

    template = "orders/checkout.html"
    return render(request, template, context)


@login_required
def return_product(request, order, id):
    order = Order.objects.get(id=order)
    variation = Variation.objects.get(id=id)
    form = OrderCancellationRequestForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            return_product = form.save(commit=False)
            return_product.order = order
            return_product.variation = variation
            return_product.save()

    return HttpResponseRedirect(reverse(orders))























