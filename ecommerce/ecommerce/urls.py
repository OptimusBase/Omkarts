"""Url Configurations."""
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^$', 'products.views.home', name='home'),
    url(r'^s/$', 'products.views.search', name='search'),
    url(r'^products/$', 'products.views.all', name='products'),
    url(r'^category/(?P<slug>[\w-]+)/$', 'products.views.category_page', name='category_page'),
    url(r'^all_categories/$', 'products.views.all_categories', name='all_categories'),
    
    url(r'^category/filter/(?P<category>[\w-]+)/(?P<spec_type_id>[\w-]+)/(?P<spec_value_id>[\w-]+)/$', 'products.views.category_page_filter_products', name='category_page_filter_products'),
    
    url(r'^products/(?P<slug>[\w-]+)/(?P<id>\d+)/$', 'products.views.single', name='single_product'),
    url(r'^cart/(?P<id>\d+)/$', 'carts.views.remove_from_cart', name='remove_from_cart'),
    url(r'^cart/(?P<slug>[\w-]+)/$', 'carts.views.add_to_cart', name='add_to_cart'),
    url(r'^cart/$', 'carts.views.view', name='cart'),
    url(r'^checkout/$', 'orders.views.checkout', name='checkout'),
    url(r'^orders/$', 'orders.views.orders', name='user_orders'),

    url(r'^ajax/dismiss_marketing_message/$', 'marketing.views.dismiss_marketing_message', name='dismiss_marketing_message'),
    url(r'^ajax/email_signup/$', 'marketing.views.email_signup', name='ajax_email_signup'),
    url(r'^ajax/add_user_address/$', 'accounts.views.add_user_address', name='ajax_add_user_address'),
    url(r'^ajax/update_default_address/$', 'accounts.views.update_default_address', name='update_default_address'),
    url(r'^ajax/add_wish_list/$', 'accounts.views.add_wish_list', name='add_wish_list'),
    url(r'^ajax/remove_from_wishlist/(?P<slug>[\w-]+)/(?P<id>\d+)/$', 'accounts.views.remove_from_wishlist', name='remove_from_wishlist'),
    url(r'^ajax/user_account_info_update$', 'accounts.views.user_account_info_update', name='user_account_info_update'),
    url(r'^ajax/user_personal_info_update$', 'accounts.views.user_personal_info_update', name='user_personal_info_update'),
    url(r'^ajax/get_product_variation_price$', 'products.views.get_product_variation_price', name='get_product_variation_price'),

    # url(r'^blog/', include('blog.urls')),
    # (?p<all_items>,*)
    # (?P<id>\d+)
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/logout/$', 'accounts.views.logout_view', name='auth_logout'),
    url(r'^accounts/login/$', 'accounts.views.login_view', name='auth_login'),
    url(r'^accounts/register/$', 'accounts.views.registration_view', name='auth_register'),
    url(r'^accounts/address/add/$', 'accounts.views.add_user_address', name='add_user_address'),
    url(r'^accounts/activate/(?P<activation_key>\w+)/$', 'accounts.views.activation_view', name='activation_view'),
    url(r'^accounts/address/$', 'accounts.views.view_user_address', name='view_user_address'),
    url(r'^accounts/wistlist/$', 'accounts.views.view_wist_list', name='view_wist_list'),
    url(r'^accounts/account_settings$', 'accounts.views.account_settings', name='account_settings'),
    # url(r'^accounts/', include('allauth.urls')),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
