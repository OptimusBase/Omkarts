import re
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core import serializers

from .models import UserDefaultAddress, UserAddress, Product, WishList, UserInformation, Variation
from .forms import LoginForm, RegistrationForm, UserAddressForm

# Create your views here.


def logout_view(request):
    logout(request)
    messages.success(request, "Successfully Logged out. Feel free to <a href='%s'>login</a> again." % (reverse("auth_login")), extra_tags='safe')
    return HttpResponseRedirect('%s' % (reverse("auth_login")))


def login_view(request):
    btn = "LOGIN"
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, "Successfully Logged In. Welcome Back!")
        return HttpResponseRedirect("/")
    context = {
        "form": form,
        "submit_btn": btn,
    }
    return render(request, "form.html", context)


def registration_view(request):
    form = RegistrationForm(request.POST or None)
    btn = "JOIN"
    if form.is_valid():
        new_user = form.save(commit=False)
        # new_user.first_name = "Mohit"
        new_user.save()
        messages.success(request, "Successfully Registered. Please confirm your email now.")
        return HttpResponseRedirect("/")
        # username = form.cleaned_data['username']
        # password = form.cleaned_data['password']
        # user = authenticate(username=username, password=password)
        # login(request, user)

    context = {
        "form": form,
        "submit_btn": btn,
    }
    return render(request, "form.html", context)


SHA1_RE = re.compile('^[a-f0-9]{40}$')


# def activation_view(request, activation_key):
#     if SHA1_RE.search(activation_key):
#         print "activation key is real"
#         try:
#             instance = EmailConfirmed.objects.get(activation_key=activation_key)
#         except EmailConfirmed.DoesNotExist:
#             instance = None
#             messages.success(request, "There was an error with ypur request.")
#             raise Http404
#         if instance is not None and not instance.confirmed:
#             page_message = "Confirmation Successfull! Welcome."
#             instance.activation_key = "Confirmed"
#             instance.confirmed = True
#             instance.save()
#             messages.success(request, "Successfully Confirmed. Please Login.")
#         elif instance is not None and instance.confirmed:
#             page_message = "Already Confirmed"
#             messages.success(request, "Already Registered.")
#         else:
#             page_message = ""

#     context = {"page_message": page_message}
#     return render(request, "accounts/activation_complete.html", context)


@login_required
def add_user_address(request):
    print request.GET
    try:
        next_page = request.GET.get("next")
    except:
        next_page = None
    form = UserAddressForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_address = form.save(commit=False)
            new_address.user = request.user
            new_address.save()
            is_default = form.cleaned_data["default"]
            if is_default:
                default_address, created = UserDefaultAddress.objects.get_or_create(user=request.user)
                default_address.shipping = new_address
                default_address.save()

            if next_page is not None:
                return HttpResponseRedirect(reverse(str(next_page)))

    submit_btn = "Save Address"
    form_title = "Add New Address"
    return render(request, "form.html", 
        {"form": form,
        "submit_btn": submit_btn,
        "form_title": form_title,
        })


@login_required
def view_user_address(request):
    context = {}
    current_addresses = UserAddress.objects.filter(user=request.user)
    try:
        primary_address = UserDefaultAddress.objects.get(user=request.user)
    except:
        primary_address = None
    context = {'current_addresses': current_addresses, "primary_address": primary_address}
    template = "accounts/user_address.html"
    return render(request, template, context)


@login_required
def update_default_address(request):
    post_vals = request.POST.copy()
    del post_vals['csrfmiddlewaretoken']

    form_data_str = json.dumps(post_vals)
    form_data_dict = json.loads(form_data_str)

    try:
        new_address = UserAddress.objects.get(id=int(form_data_dict['radio_id']))
        default_address, created = UserDefaultAddress.objects.get_or_create(user=request.user)
        default_address.shipping = new_address
        default_address.save()
        return HttpResponse(form_data_dict['radio_id'])
    except:
        return HttpResponse("error")


@login_required
def add_wish_list(request):
    post_vals = request.POST.copy()
    del post_vals['csrfmiddlewaretoken']

    form_data_str = json.dumps(post_vals)
    form_data_dict = json.loads(form_data_str)
    try:
        user = request.user
        variation = Variation.objects.get(id=form_data_dict['product_variation_id'])
        product = variation.product
        try:
            wish = WishList.objects.get(user=user, variation=variation, product=product)
            if wish.active:
                data = "Item already added to Wish List."
            else:
                wish.active = True
                wish.save()
                data = "Added to Wish List"
        except:
            WishList.objects.create(
                user=user,
                product=product,
                variation=variation,
                active=True)
            data = "Added to Wish List"
    except:
        data = "Failed adding to Wish List. Please Try again later!"
    return HttpResponse(data)


@login_required
def view_wist_list(request):
    context = {}
    user = request.user
    wish_list = WishList.objects.filter(user=user, active=True)
    context = {"wish_list": wish_list}
    template = "accounts/user_wishList.html"
    return render(request, template, context)


@login_required
def remove_from_wishlist(request, slug, id):
    context = {}
    user = request.user
    variation = Variation.objects.get(id=id)
    try:
        product = Product.objects.get(slug=slug)
        query = WishList.objects.get(user=user, product=product, variation=variation)
        query.active = False
        query.save()
        context = {"data": "Item removed from Wish List."}
    except:
        context = {"data": "Failed to remove from Wish List. Please try again later."}

    wish_list = WishList.objects.filter(user=user)
    context["wish_list"] = wish_list
    template = "accounts/user.html"
    return HttpResponseRedirect('%s' % (reverse("view_wist_list")))


@login_required
def account_settings(request):
    # import ipdb; ipdb.set_trace()
    context = {}
    user = request.user
    try:
        user_info = UserInformation.objects.get(user=user)
    except:
        UserInformation.objects.create(user=user)
        user_info = UserInformation.objects.get(user=user)
    context = {"user": user, "user_info": user_info}
    template = "accounts/user/account_settings.html"
    return render(request, template, context)


@login_required
def user_account_info_update(request):
    """Storing User Information."""
    data = {}
    post_vals = request.POST.copy()
    del post_vals['csrfmiddlewaretoken']

    form_data_str = json.dumps(post_vals)
    form_data_dict = json.loads(form_data_str)

    try:
        email = form_data_dict['email']

        user_info = request.user
        user_info.email = email
        user_info.save()

        data = user_info
        data = serializers.serialize('json', [data])
        return HttpResponse(data)

    except:
        data = "Failed to update User Account Info."
        data = serializers.serialize('json', [data])
        return HttpResponse(data)


@login_required
def user_personal_info_update(request):
    """Storing User Information."""
    data = {}
    post_vals = request.POST.copy()
    del post_vals['csrfmiddlewaretoken']

    form_data_str = json.dumps(post_vals)
    form_data_dict = json.loads(form_data_str)

    try:
        name = form_data_dict['name']
        gender = form_data_dict['gender']
        # birthdate = form_data_dict['birthdate']
        country = form_data_dict['country']

        user = request.user
        try:
            user_info = UserInformation.objects.get(user=user)
            if name != "":
                user_info.name = name
            if gender != "":
                user_info.gender = gender
            # if birthdate != "":
            #     user_info.birthdate = birthdate
            if country != "":
                user_info.country = country
        except UserInformation.DoesNotExist:
            user_info = UserInformation(
                user=user,
                name=name,
                gender=gender,
                # birthdate=birthdate,
                country=country)

        user_info.save()
        try:
            name = form_data_dict['name']

            django_user = request.user
            django_user.first_name = name

            django_user.save()
        except:
            pass

        data = user_info
        data = serializers.serialize('json', [data])
        return HttpResponse(data)

    except:
        data = "Failed to update User Account Info."
        data = serializers.serialize('json', [data])
        return HttpResponse(data)

































