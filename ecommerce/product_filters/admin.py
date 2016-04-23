"""Admin configs."""
from django.contrib import admin

from product_filters.models import ProductFilter, ProductFilterAttributes

# Register your models here.


class ProductFilterAttributesInline(admin.StackedInline):
    model = ProductFilterAttributes
    extra = 0


class ProductFilterAdmin(admin.ModelAdmin):
    inlines = [
        ProductFilterAttributesInline,
    ]

    class Meta:
        model = ProductFilter

admin.site.register(ProductFilter, ProductFilterAdmin)
admin.site.register(ProductFilterAttributes)
