from django.conf.urls import patterns, include, url
from shop import views as shop_views

urlpatterns = patterns('',
    url(r'^products/$', shop_views.ProductsList.as_view(), name='shop_products_list'),
    url(r'^products/(?P<product_id>\d+)/details/$', shop_views.ProductDetails.as_view(), name='shop_products_details'),
)
