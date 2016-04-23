""""Filter."""
from django import template
from products.models import Product, ProductImage
register = template.Library()


@register.filter
def wishlist_item(item):
    product = []
    product.append(item.variation)
    return product


@register.filter
def filter_product_images(product_images, product):
    """Function will return 1 variation image or 1 product image."""
    item = []
    imgs = product_images
    try:
        for img in imgs:
            if img.featured and img.active:
                item.append(img.image)
                return item
            else:
                pass
    except:
        pass

    try:
        item.append(product.image)
        return item
    except:
        pass

    return item


# @register.filter
# def filter_product_images(product):
#     item = []
#     product = Product.objects.get(slug=product.slug)
#     imgs = ProductImage.objects.filter(product=product)
#     try:
#         for img in imgs:
#             if img.featured:
#                 item.append(img)
#                 return item
#             else:
#                 featured = False
#     except:
#         pass

#     if not featured:
#         try:
#             for img in imgs:
#                 item.append(img)
#                 return item
#         except:
#             pass
#     return item
