from django.contrib import admin

# Register your models here.

from .models import Order
from carts.models import CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        CartItemInline
    ]
    class Meta:
    	"""String."""
        model = Order

admin.site.register(Order, OrderAdmin)
