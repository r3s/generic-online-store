from django.conf.urls import patterns, include, url
from shop import admin_views as shop_admin

urlpatterns = patterns('',
    url(r'^products/$', shop_admin.ProductsAdmin.as_view(), name='admin_shop_products'),
    url(r'^categories/$', shop_admin.CategoryAdmin.as_view(), name='admin_shop_categories'),
    url(r'^vendors/$', shop_admin.VendorAdmin.as_view(), name='admin_shop_vendors'),

    url(r'^products/create/$', shop_admin.ProductsCreate.as_view(), name='admin_shop_products_create'),
    url(r'^products/(?P<product_id>\d+)/edit/$', shop_admin.ProductsEdit.as_view(), name='admin_shop_products_edit'),
    url(r'^products/(?P<product_id>\d+)/delete/$', shop_admin.ProductsDelete.as_view(), name='admin_shop_products_delete'),

    url(r'^categories/create/$', shop_admin.CategoriesCreate.as_view(), name='admin_shop_categories_create'),
    url(r'^categories/(?P<category_id>\d+)/edit/$', shop_admin.CategoriesEdit.as_view(), name='admin_shop_categories_edit'),
    url(r'^categories/(?P<category_id>\d+)/delete/$', shop_admin.CategoriesDelete.as_view(), name='admin_shop_categories_delete'),

    url(r'^vendors/create/$', shop_admin.VendorsCreate.as_view(), name='admin_shop_vendors_create'),
    url(r'^vendors/(?P<vendor_id>\d+)/edit/$', shop_admin.VendorsEdit.as_view(), name='admin_shop_vendors_edit'),
    url(r'^vendors/(?P<vendor_id>\d+)/delete/$', shop_admin.VendorsDelete.as_view(), name='admin_shop_vendors_delete'),

)
