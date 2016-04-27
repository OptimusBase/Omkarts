from django.contrib import admin
from product_description.models import *
from import_export.admin import ImportExportMixin

# Register your models here.


class PdpSpecificationTypeAdmin(ImportExportMixin, admin.ModelAdmin):

    class Meta:
        model = PdpSpecificationType

admin.site.register(PdpSpecificationType, PdpSpecificationTypeAdmin)


class PdpSpecificationAdmin(ImportExportMixin, admin.ModelAdmin):

    class Meta:
        model = PdpSpecification

admin.site.register(PdpSpecification, PdpSpecificationAdmin)


class PdpDescriptionAdmin(ImportExportMixin, admin.ModelAdmin):

    class Meta:
        model = PdpDescription

admin.site.register(PdpDescription, PdpDescriptionAdmin)


class PdpKeyFeatureAdmin(ImportExportMixin, admin.ModelAdmin):

    class Meta:
        model = PdpKeyFeature

admin.site.register(PdpKeyFeature, PdpKeyFeatureAdmin)


class PdpPhysicalFeatureAdmin(ImportExportMixin, admin.ModelAdmin):

    class Meta:
        model = PdpPhysicalFeature

admin.site.register(PdpPhysicalFeature, PdpPhysicalFeatureAdmin)


class PdpFeaturedAdmin(ImportExportMixin, admin.ModelAdmin):

    class Meta:
        model = PdpFeatured

admin.site.register(PdpFeatured, PdpFeaturedAdmin)




















