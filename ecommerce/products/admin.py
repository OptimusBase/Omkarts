"""Admin Configuration."""
from django.contrib import admin
from .models import Category, SubCategoryParent, SubCategoryChild, Product, ProductImage, Variation, Brand, Variation, BrandConfiguration
from product_description.models import PdpSpecification, PdpDescription, PdpFeatured, PdpKeyFeature, PdpPhysicalFeature
# Register your models here.


class VariationInline(admin.StackedInline):
    model = Variation
    extra = 0


class PdpSpecificationInline(admin.StackedInline):
    model = PdpSpecification
    extra = 0


class PdpDescriptionInline(admin.StackedInline):
    model = PdpDescription
    extra = 0


class PdpKeyFeatureInline(admin.StackedInline):
    model = PdpKeyFeature
    extra = 0


class PdpPhysicalFeatureInline(admin.StackedInline):
    model = PdpPhysicalFeature
    extra = 0


class PdpFeaturedInline(admin.StackedInline):
    model = PdpFeatured
    extra = 0


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    readonly = ['updated', 'timestamp']
    prepopulated_fields = {"slug": ("category_name",)}

    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)


class SubCategoryParentAdmin(admin.ModelAdmin):
    readonly = ['updated', 'timestamp']
    prepopulated_fields = {"slug": ("sub_cat_parent_name",)}

    class Meta:
        model = SubCategoryParent

admin.site.register(SubCategoryParent, SubCategoryParentAdmin)


class SubCategoryChildAdmin(admin.ModelAdmin):
    readonly = ['updated', 'timestamp']
    prepopulated_fields = {"slug": ("sub_cat_child_name",)}

    class Meta:
        model = SubCategoryChild

admin.site.register(SubCategoryChild, SubCategoryChildAdmin)


class ProductAdmin(admin.ModelAdmin):
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
        model = Product
admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'variation', ]
    # inlines = [
    #     ProductImageInline,
    # ]

    class Meta:
        model = Variation

admin.site.register(ProductImage, ProductImageAdmin)


class VariationAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'product']
    search_fields = ['product__title']
    list_filter = ['product']
    inlines = [
        ProductImageInline, PdpSpecificationInline, PdpDescriptionInline, PdpPhysicalFeatureInline, PdpKeyFeatureInline, PdpFeaturedInline
    ]

    class Meta:
        model = Variation

admin.site.register(Variation, VariationAdmin)

# admin.site.register(BrandConfiguration)


class BrandConfigurationInline(admin.StackedInline):
    model = BrandConfiguration
    extra = 0


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("brand_name",)}
    inlines = [
        BrandConfigurationInline,
    ]

    class Meta:
        model = Brand

admin.site.register(Brand, BrandAdmin)
