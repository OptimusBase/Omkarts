from django.contrib import admin

# Register your models here.

from orders.models import Order, OrderCancellationRequest
from carts.models import CartItem


class CartItemInline(admin.TabularInline):
    """CartItemInline."""

    model = CartItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('razor_payment_id',)
    inlines = [
        CartItemInline
    ]

    class Meta:
        """String."""

        model = Order

admin.site.register(Order, OrderAdmin)


class OrderCancellationRequestAdmin(admin.ModelAdmin):
    # readonly_fields = ['cancel_status']
    exclude = ('user_notification',)

    readonly_fields = ('cancel_status',)

    class Meta:
        model = OrderCancellationRequest

admin.site.register(OrderCancellationRequest, OrderCancellationRequestAdmin)
