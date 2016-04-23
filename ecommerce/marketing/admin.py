from django.contrib import admin

# Register your models here.
from .models import MarketingMessage, Slider, CategorySlider, AllCategorySlider


class MarketingMessageAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "start_date", "end_date", "active"]

    class Meta:
        model = MarketingMessage

admin.site.register(MarketingMessage, MarketingMessageAdmin)


class SliderAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "order", "start_date", "end_date", "active"]
    list_editable = ["order", "start_date", "end_date"]

    class Meta:
        model = Slider

admin.site.register(Slider, SliderAdmin)

admin.site.register(CategorySlider)

admin.site.register(AllCategorySlider)