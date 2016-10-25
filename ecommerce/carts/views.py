from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.
from products.models import Product, Variation
from accounts.models import WishList
from .models import Cart, CartItem


def view(request):
    """VIew."""
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
    if the_id:
        new_total = 0.00
        for item in cart.cartitem_set.filter(active=True):
            line_total = float(item.variation.price) * item.quantity
            new_total += line_total

        request.session['items_total'] = CartItem.objects.filter(cart=cart, active=True).count()
        cart.total = new_total
        cart.save()
        context = {"cart": cart}
    else:
        empty_message = "Your Cart is empty, please keep shopping."
        context = {"empty": True, "empty_message": empty_message}

    template = "cart/view.html"
    return render(request, template, context)


def remove_from_cart(request, id):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse("cart"))
    cartitem = CartItem.objects.get(id=id)
    cartitem.active = False
    cartitem.save()
    return HttpResponseRedirect(reverse("cart"))


def add_to_cart(request, slug):
    request.session.set_expiry(120000)

    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    try:
        cart = Cart.objects.get(id=the_id)
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)

    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExits:
        pass
    except:
        pass

    # product_var = [] # product variation
    if request.method == "POST":
        qty = request.POST['qty']
        variation_id = request.POST['variation-form']
        variation = Variation.objects.get(id=variation_id)
        # for item in request.POST:
        #     key = item
        #     val = request.POST[key]
        #     try:
        #         v = Variation.objects.get(product=product, category__iexact=key, title__iexact=val)
        #         product_var.append(v)
        #     except:
        #         pass

        try:
            if variation.quantity <= 0:
                print "variation quantity is <= 0, this error is caught in try block in add to cart"
                # logger.error('variation quantity is <= 0, this error is caught in try block in add to cart')
                return HttpResponseRedirect(reverse("home"))
        except:
            print "variation quantity error, this error is caught in except block in add to cart"
            # logger.error('variation quantity error, this error is caught in except block in add to cart')
            return HttpResponseRedirect(reverse("home"))

        user_cartitems_list = CartItem.objects.filter(cart=cart, active=True)
        variant_added = False
        if user_cartitems_list.count() > 0:
            for item in user_cartitems_list:
                if variant_added is False:
                    if item.variation.id == variation.id:
                        query = CartItem.objects.get(id=item.id)
                        query.quantity += int(qty.encode('utf8'))
                        query.save()
                        variant_added = True

                    else:
                        cart_item = CartItem.objects.create(
                            cart=cart,
                            product=product,
                            variation=variation,
                            line_total=variation.price)
                        cart_item.quantity = qty
                        cart_item.save()
                        variant_added = True
        else:
            cart_item = CartItem.objects.create(
                cart=cart,
                product=product,
                variation=variation,
                line_total=variation.price)
            cart_item.quantity = qty
            cart_item.save()
            variant_added = True

        # if len(product_var) > 0:
        #     cart_item.variations.add(*product_var)

        # Removing Item from Wish list.
        try:
            query = WishList.objects.get(user=request.user, variation=variation)
            query.active = False
            query.save()
        except:
            pass

        return HttpResponseRedirect(reverse("cart"))
    else:
        return HttpResponseRedirect(reverse("cart"))
