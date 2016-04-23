from django.contrib import admin

# Register your models here.
from .models import UserStripe, EmailConfirmed, EmailMarketingSignUp, UserAddress, UserDefaultAddress, WishList, UserInformation, RecentViews


class UserAddressAdmin(admin.ModelAdmin):
    class Meta:
        model = UserAddress

admin.site.register(UserAddress, UserAddressAdmin)

admin.site.register(UserStripe)

admin.site.register(EmailConfirmed)

admin.site.register(UserDefaultAddress)


class EmailMarketingSignUpAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'timestamp']

    class Meta:
        model = EmailMarketingSignUp


admin.site.register(EmailMarketingSignUp, EmailMarketingSignUpAdmin)

admin.site.register(WishList)


class UserInformationAdmin(admin.ModelAdmin):
    fields = ['name', 'gender', 'country', 'birthdate']

    class Meta:
        model = UserInformation

admin.site.register(UserInformation, UserInformationAdmin)

admin.site.register(RecentViews)