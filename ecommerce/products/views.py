from django.shortcuts import render, HttpResponse, Http404
from marketing.models import Slider
# Create your views here.
# from marketing.forms import EmailForm
from products.models import Product, SubCategoryParent, SubCategoryChild, Brand, Variation
from marketing.models import CategorySlider, AllCategorySlider
from accounts.models import RecentViews
from product_filters.models import ProductFilterAttributes, ProductFilter
from product_description.models import PdpSpecificationType, PdpSpecification
import json
from django.core import serializers


def search(request):
    """Search."""
    try:
        q = request.GET.get('q')
    except:
        q = None

    if q:
        products = Product.objects.filter(title__icontains=q)
        context = {'query': q, 'products': products}
        template = 'products/results.html'
    else:
        template = 'products/home.html'
        context = {}
    return render(request, template, context)


def home(request):
    """Home Function."""
    sliders = Slider.objects.active()
    sub_cat_parent = SubCategoryParent.objects.all()
    products = Product.objects.all()
    try:
        user = request.user
        recent_views = RecentViews.objects.filter(user=user)
    except:
        recent_views = []

    popular_products = RecentViews.objects.all()

    template = 'products/home.html'
    context = {"products": products, "sub_cat_parent": sub_cat_parent, "sliders": sliders, "recent_views": recent_views, "popular_products": popular_products}
    return render(request, template, context)


def all(request):
    """Displaying all Products method."""
    products = Product.objects.all()
    context = {'products': products}
    template = 'products/all.html'
    return render(request, template, context)
    # sub_cat_child = SubCategoryChild.objects.get(slug=slug)
    # sliders = CategorySlider.objects.all_featured().filter(sub_cat_child=sub_cat_child)
    # products = Product.objects.filter(sub_category_child=sub_cat_child)
    # category = slug
    # brands = Brand.objects.all()
    # context = {'products': products, "sub_cat_child": sub_cat_child, "sliders": sliders, "slug": slug, "category": category, "brands": brands}
    # template = 'products/category.html'
    # return render(request, template, context)


def all_categories(request):
    """Displaying all Categories method."""
    sub_cat_parent = SubCategoryParent.objects.all()
    sliders = AllCategorySlider.objects.active()
    variations = Variation.objects.all()
    context = {'products': variations, "sub_cat_parent": sub_cat_parent, "sliders": sliders}
    template = 'products/all_category.html'
    return render(request, template, context)


def category_page(request, slug):
    """Displaying all Products method."""
    variations = []
    variation_count = 0
    sub_cat_child = SubCategoryChild.objects.get(slug=slug)
    products = Product.objects.filter(sub_category_child=sub_cat_child)
    for product in products:
        variations.append(product.variation_set.all())
        for prod in product.variation_set.all():
            variation_count += 1

    category = slug
    sub_cat_parent = sub_cat_child.sub_category_parent

    product_filter = ProductFilter.objects.active().filter(sub_cat_parent=sub_cat_parent)
    product_filter = ProductFilterAttributes.objects.filter(product_filter=product_filter)

    context = {'variations': variations, "sub_cat_child": sub_cat_child, "slug": slug, "category": category, "product_filter": product_filter, "variation_count": variation_count}
    template = 'products/category.html'
    return render(request, template, context)


def category_page_filter_products(request, category, spec_type_id, spec_value_id):
    """Displaying all Products method."""
    # import ipdb; ipdb.set_trace()
    variations = []
    variation_count = 0
    spec_type = PdpSpecificationType.objects.get(id=spec_type_id)
    spec_value = PdpSpecification.objects.get(id=spec_value_id)

    category = category
    sub_cat_child = SubCategoryChild.objects.get(slug=category)
    sub_cat_parent = sub_cat_child.sub_category_parent

    product_filter = ProductFilter.objects.active().filter(sub_cat_parent=sub_cat_parent)
    product_filter = ProductFilterAttributes.objects.filter(product_filter=product_filter)

    sub_cat_child = SubCategoryChild.objects.get(slug=category)
    products = Product.objects.filter(sub_category_child=sub_cat_child)
    for product in products:
        variations.append(product.variation_set.all())
        for prod in product.variation_set.all():
            variation_count += 1

    context = {'variations': variations, "sub_cat_child": sub_cat_child, "category": category, "product_filter": product_filter, "spec_type": spec_type, "spec_value": spec_value, "variation_count": variation_count}
    template = 'products/category.html'
    return render(request, template, context)


def single(request, slug, id):
    """Displaying all Products method."""
    try:
        variation = Variation.objects.get(id=id)
        product = Product.objects.get(slug=slug)
        # images = ProductImage.objects.filter(variation=variation)
        variations = Variation.objects.filter(product=product)

        try:
            user = request.user
            recent_view = RecentViews.objects.create(
                user=user,
                variation=variation)
        except:
            pass

        popular_products = RecentViews.objects.all()
        context = {'product': product, 'variations': variations, "popular_products": popular_products, "variation": variation}
        template = 'products/single.html'
        return render(request, template, context)
    except:
        raise Http404


def get_product_variation_price(request):
    """Get product_variation_price."""
    if request.method == "POST":
        data = {}
        post_vals = request.POST.copy()
        del post_vals['csrfmiddlewaretoken']

        form_data_str = json.dumps(post_vals)
        form_data_dict = json.loads(form_data_str)

        try:
            variation_id = form_data_dict['variation']
            variant = Variation.objects.get(id=variation_id)
            if variant.quantity > 3:
                stock = True
                qty = "In stock"
            elif variant.quantity > 0:
                stock = True
                qty = "only %d left" % (variant.quantity)
            elif variant.quantity == 0:
                stock = False
                qty = "Out of Stock"

            price = int(variant.price)

            variation = Variation.objects.get(id=variation_id)
            product = variation.product
            # images = ProductImage.objects.filter(variation=variation)
            variations = Variation.objects.filter(product=product)

            try:
                user = request.user
                recent_view = RecentViews.objects.create(
                    user=user,
                    product=product)
            except:
                pass

            popular_products = RecentViews.objects.all()

            # return HttpResponse(price, stock)
            variation = serializers.serialize('json', [variation])
            product = serializers.serialize('json', [product])
            variations = serializers.serialize('json', variations)
            popular_products = serializers.serialize('json', popular_products)

            data = {"price": price, "qty": qty, "stock": stock, "variation_id": variation_id, 'product': product, 'variations': variations, "popular_products": popular_products, "variation": variation}
            # print data
            # data = serializers.serialize('json', [data])
            return HttpResponse(json.dumps(data), content_type="application/json")
        except:
            return "Improper Variant selected"
    else:
        raise Http404


