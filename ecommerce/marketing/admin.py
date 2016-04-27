from django.contrib import admin

# Register your models here.
from .models import MarketingMessage, Slider, CategorySlider, AllCategorySlider
from import_export.admin import ImportExportMixin


class MarketingMessageAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ["__unicode__", "start_date", "end_date", "active"]

    class Meta:
        model = MarketingMessage

admin.site.register(MarketingMessage, MarketingMessageAdmin)


class SliderAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ["__unicode__", "order", "start_date", "end_date", "active"]
    list_editable = ["order", "start_date", "end_date"]

    class Meta:
        model = Slider

admin.site.register(Slider, SliderAdmin)


class CategorySliderAdmin(ImportExportMixin, admin.ModelAdmin):

    class Meta:
        model = CategorySlider

admin.site.register(CategorySlider, CategorySliderAdmin)


class AllCategorySliderAdmin(ImportExportMixin, admin.ModelAdmin):

    class Meta:
        model = AllCategorySlider

admin.site.register(AllCategorySlider, AllCategorySliderAdmin)