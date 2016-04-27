"""Admin Configuration."""
from django.contrib import admin
from .models import Category, SubCategoryParent, SubCategoryChild, Product, ProductImage, Variation, Brand, Variation, BrandConfiguration
from product_description.models import PdpSpecification, PdpDescription, PdpFeatured, PdpKeyFeature, PdpPhysicalFeature
from import_export.admin import ImportExportMixin
# Register your models here.


class VariationInline(admin.StackedInline):
    """VariationInline."""

    model = Variation
    extra = 0


class PdpSpecificationInline(admin.StackedInline):
    """PdpSpecificationInline."""

    model = PdpSpecification
    extra = 0


class PdpDescriptionInline(admin.StackedInline):
    """PdpSpecificationInline."""

    model = PdpDescription
    extra = 0


class PdpKeyFeatureInline(admin.StackedInline):
    """PdpKeyFeatureInline."""

    model = PdpKeyFeature
    extra = 0


class PdpPhysicalFeatureInline(admin.StackedInline):
    """PdpPhysicalFeatureInline."""

    model = PdpPhysicalFeature
    extra = 0


class PdpFeaturedInline(admin.StackedInline):
    """PdpFeaturedInline."""

    model = PdpFeatured
    extra = 0


class ProductImageInline(admin.StackedInline):
    """ProductImageInline."""

    model = ProductImage
    extra = 0


class CategoryAdmin(ImportExportMixin, admin.ModelAdmin):
    """CategoryAdmin."""

    readonly = ['updated', 'timestamp']
    prepopulated_fields = {"slug": ("category_name",)}

    class Meta:
        """Meta."""

        model = Category

admin.site.register(Category, CategoryAdmin)


class SubCategoryChildInline(admin.StackedInline):
    """ProductImageInline."""

    model = SubCategoryChild
    extra = 0


class SubCategoryParentAdmin(ImportExportMixin, admin.ModelAdmin):
    """SubCategoryParentAdmin."""

    readonly = ['updated', 'timestamp']
    prepopulated_fields = {"slug": ("sub_cat_parent_name",)}
    # inlines = [
    #     SubCategoryChildInline,
    # ]

    class Meta:
        """Meta."""

        model = SubCategoryParent

admin.site.register(SubCategoryParent, SubCategoryParentAdmin)


class SubCategoryChildAdmin(ImportExportMixin, admin.ModelAdmin):
    """SubCategoryChildAdmin."""
    list_display = ['sub_category_parent', 'sub_cat_child_name']
    readonly = ['updated', 'timestamp']
    prepopulated_fields = {"slug": ("sub_cat_child_name",)}

    class Meta:
        """Meta."""

        model = SubCategoryChild

admin.site.register(SubCategoryChild, SubCategoryChildAdmin)


class ProductAdmin(ImportExportMixin, admin.ModelAdmin):
    """Products Admin."""

    # fields = ('category', 'sub_category_parent', 'sub_category_child', 'brand', 'title', 'image', 'slug', 'active',)
    date_hierarchy = 'timestamp'
    search_fields = ['title', 'description']
    list_display = ['title', 'active', 'updated']
    list_editable = ['active']
    list_filter = ['active', ]
    readonly = ['updated', 'timestamp']
    prepopulated_fields = {"slug": ("title",)}

    inlines = [
        VariationInline,
    ]

    class Meta:
        """Meta."""

        model = Product
admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(ImportExportMixin, admin.ModelAdmin):
    """ProductImageAdmin."""

    list_display = ['id', 'variation', ]
    # inlines = [
    #     ProductImageInline,
    # ]

    class Meta:
        """Meta."""

        model = Variation

admin.site.register(ProductImage, ProductImageAdmin)


class VariationAdmin(ImportExportMixin, admin.ModelAdmin):
    """VariationAdmin."""

    list_display = ['__unicode__', 'product']
    search_fields = ['product__title']
    list_filter = ['product']
    inlines = [
        ProductImageInline, PdpSpecificationInline, PdpDescriptionInline, PdpPhysicalFeatureInline, PdpKeyFeatureInline, PdpFeaturedInline
    ]

    class Meta:
        """Meta."""

        model = Variation

admin.site.register(Variation, VariationAdmin)

# admin.site.register(BrandConfiguration)


class BrandConfigurationInline(admin.StackedInline):
    """BrandConfigurationInline."""

    model = BrandConfiguration
    extra = 0


class BrandAdmin(ImportExportMixin, admin.ModelAdmin):
    """BrandAdmin."""

    prepopulated_fields = {"slug": ("brand_name",)}
    inlines = [
        BrandConfigurationInline,
    ]

    class Meta:
        """Meta."""

        model = Brand

admin.site.register(Brand, BrandAdmin)


class BrandConfigurationAdmin(ImportExportMixin, admin.ModelAdmin):
    class Meta:
        model = BrandConfiguration

admin.site.register(BrandConfiguration, BrandConfigurationAdmin)

