""""Filter."""
from django import template
from products.models import Product, SubCategoryParent, Brand, Variation
from django.template.defaultfilters import slugify
from collections import Counter
register = template.Library()


@register.filter
def filter_products(products, sub_cat_parent_name):
    sub_cat_parent_name = SubCategoryParent.objects.get(sub_cat_parent_name=sub_cat_parent_name)
    products = Product.objects.filter(sub_category_parent=sub_cat_parent_name)
    return products


@register.filter
def filter_product_images(product_images, product):
    """Function will return 1 variation image or 1 product image."""
    item = []
    imgs = product_images
    try:
        for img in imgs:
            if img.thumbnail and img.active:
                item.append(img)
                return item
            else:
                pass
    except:
        pass

    try:
        item.append(product)
        return item
    except:
        pass

    return item


@register.filter
def filter_product_images_2(product_images, product):
    """Function will return all the variation images."""
    item = []
    imgs = product_images
    try:
        for img in imgs:
            if img.active:
                item.append(img.image)
            else:
                pass
        if len(item) > 0:
            return item
    except:
        pass

    try:
        item.append(product.image)
        return item
    except:
        pass

    return item


@register.filter
def filter_unique_products(recent_views):
    items = []
    item_id = []
    for recent_view in recent_views:
        if not recent_view.variation.id in item_id:
            items.append(recent_view.variation)
            item_id.append(recent_view.variation.id)

    return items


@register.filter
def filter_popular_products(recent_views):
    items = []
    item_id = []
    items_list = []
    count = Counter(recent_views)
    popular_products = count.most_common(10)

    for x in range(0, len(popular_products)):
        items_list.append(popular_products[x][0])

    recent_views = items_list

    for recent_view in recent_views:
        if not recent_view.variation.id in item_id:
            items.append(recent_view)
            item_id.append(recent_view.variation.id)

    return items


@register.filter
def sort(content):
    return sorted(content, key=lambda x: x.order)


@register.filter
def check_brands(sub_cat_parent):
    brands_list = []
    for brand in sub_cat_parent.brandconfiguration_set.all().order_by('order'):
        if brand.featured and brand.brand.active:
            brands_list.append(brand)
    return brands_list


@register.filter
def filter_brands(products, brand):
    products = Product.objects.filter(brand=brand)
    return products


@register.filter
def filter_category_products(products, sub_cat_parent_name):
    product_variations = []
    sub_cat_parent_name = SubCategoryParent.objects.get(sub_cat_parent_name=sub_cat_parent_name)
    products = Product.objects.filter(sub_category_parent=sub_cat_parent_name)
    for product in products:
        variations = Variation.objects.filter(product=product)
        for variation in variations:
            product_variations.append(variation)
    return product_variations


@register.filter
def filter_products_2(variations, brand):
    product_variations = []
    for variation in variations:
        if variation.product.brand.brand_name == brand.brand.brand_name:
            product_variations.append(variation)
    return product_variations


# @register.filter
# def test_tag(values):
#     import ipdb; ipdb.set_trace()
#     val = []
#     for value in values:
#         val.append(value)
#     return val


@register.filter
def get_thumbnail_img(variation):
    try:
        variations = variation.productimage_set.filter(thumbnail=True)
        for variant in variations:
            return variant.image.name
    except:
        pass
    return variation.product.image.name


@register.filter
def custom_product_filters_1(variations, spec_type):
    # import ipdb; ipdb.set_trace()
    variations_list = []
    for variation in variations:
        for spec in variation.pdpspecification_set.all():
            if spec.specification_type.specification_type == spec_type.specification_type:
                variations_list.append(variation)
    return variations_list


@register.filter
def custom_product_filters_2(variations, spec_type):
    # import ipdb; ipdb.set_trace()
    variations_list = []
    for variation in variations:
        for spec in variation.pdpspecification_set.all():
            if spec.specification_value == spec_type.specification_value:
                variations_list.append(variation)
    return variations_list
    return variations


@register.filter
def unique_specs(specs):
    items = []
    items_list = []

    for spec in specs:
        string = spec.specification_value
        string = slugify(string)
        if not string in items_list:
            items.append(spec)
            items_list.append(string)
    return items
















