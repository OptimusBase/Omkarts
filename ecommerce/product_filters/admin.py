"""Admin configs."""
from django.contrib import admin

from product_filters.models import ProductFilter, ProductFilterAttributes
from import_export.admin import ImportExportMixin

# Register your models here.


class ProductFilterAttributesInline(admin.StackedInline):
    model = ProductFilterAttributes
    extra = 0


class ProductFilterAdmin(ImportExportMixin, admin.ModelAdmin):
    inlines = [
        ProductFilterAttributesInline,
    ]

    class Meta:
        model = ProductFilter

admin.site.register(ProductFilter, ProductFilterAdmin)


class ProductFilterAttributesAdmin(ImportExportMixin, admin.ModelAdmin):
    class Meta:
        model = ProductFilterAttributes

admin.site.register(ProductFilterAttributes, ProductFilterAttributesAdmin)
