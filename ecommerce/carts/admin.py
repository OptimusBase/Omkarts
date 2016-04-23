from django.contrib import admin

# Register your models here.
from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0


class CartAdmin(admin.ModelAdmin):
    inlines = [
        CartItemInline
    ]
    class Meta:
        model = Cart

admin.site.register(Cart, CartAdmin)


class CartItemAdmin(admin.ModelAdmin):
    list_filter = ['cart']
    class Meta:
        model = CartItem


admin.site.register(CartItem, CartItemAdmin)
