""""Filter."""
from django import template
from carts.models import CartItem
register = template.Library()


@register.filter
def filter_cartitems(order):
    # import ipdb; ipdb.set_trace()
    cartitems = CartItem.objects.filter(order=order)
    return cartitems


@register.filter
def multiply(value, arg):
    return value * arg


@register.filter
def filter_product_images(product_images, product):
    """Function will return 1 variation image or 1 product image."""
    item = []
    imgs = product_images
    try:
        for img in imgs:
            if img.thumbnail and img.active:
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
# def filter_product_images(product_images):
#     item = []
#     imgs = product_images
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
