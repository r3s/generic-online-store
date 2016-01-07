from django.conf.urls import patterns, include, url
from shop import custom_admin as shop_admin

urlpatterns = patterns('',
    # url(r'^', profile_view.UserAuthentication.as_view(), name='login'),
    url(r'^products/$', shop_admin.ProductsAdmin.as_view(), name='admin_shop_products'),
    url(r'^categories/$', shop_admin.CategoryAdmin.as_view(), name='admin_shop_categories'),
    url(r'^products/create/$', shop_admin.ProductsCreate.as_view(), name='admin_shop_products_create'),
    url(r'^categories/create/$', shop_admin.CategoriesCreate.as_view(), name='admin_shop_categories_create'),
    # url(r'^(?P<id>\d+)/calls/$', 'competitions.views.my_calls', name='my_calls'),
)
