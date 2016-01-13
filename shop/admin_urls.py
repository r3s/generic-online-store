from django.conf.urls import patterns, include, url
from shop import admin_views as shop_admin

urlpatterns = patterns('',
    # url(r'^', profile_view.UserAuthentication.as_view(), name='login'),
    url(r'^products/$', shop_admin.ProductsAdmin.as_view(), name='admin_shop_products'),
    url(r'^categories/$', shop_admin.CategoryAdmin.as_view(), name='admin_shop_categories'),
    url(r'^products/create/$', shop_admin.ProductsCreate.as_view(), name='admin_shop_products_create'),
    url(r'^products/(?P<product_id>\d+)/edit/$', shop_admin.ProductsEdit.as_view(), name='admin_shop_products_edit'),
    url(r'^products/(?P<product_id>\d+)/delete/$', shop_admin.ProductsDelete.as_view(), name='admin_shop_products_delete'),
    url(r'^categories/create/$', shop_admin.CategoriesCreate.as_view(), name='admin_shop_categories_create'),
    url(r'^categories/(?P<category_id>\d+)/edit/$', shop_admin.CategoriesEdit.as_view(), name='admin_shop_categories_edit'),
    url(r'^categories/(?P<category_id>\d+)/delete/$', shop_admin.CategoriesDelete.as_view(), name='admin_shop_categories_delete'),
    # url(r'^(?P<id>\d+)/calls/$', 'competitions.views.my_calls', name='my_calls'),
)
