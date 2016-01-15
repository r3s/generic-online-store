from django import http, shortcuts
from django.conf import settings
from django.views.generic import View
from django.contrib import messages

from utils import helpers
import models as shop_models
# import forms as shop_forms
import datetime
import logging
import ipdb

# globals
if not settings.DEBUG:
    logger = logging.getLogger("django.request")
else:
    logger = logging.getLogger("gs_file")

class ProductsList(View):
    def get(self, request, *args, **kwargs):
        products = shop_models.Product.objects.all()
        if request.GET.get('cat'):
            try:
                products = products.filter(category=int(request.GET.get('cat')))
            except:
                pass
        categories = shop_models.ProductCategories.objects.all()
        page_no = request.GET.get('page')
        page_size = 10
        queryset = helpers.paginate(products,page_no,page_size)
        return  shortcuts.render(request, "shop/product_list.html",{
        'queryset':queryset,
        'categories':categories,
        })
