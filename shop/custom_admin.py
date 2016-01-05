from django.shortcuts import render
from django import http
import logging
from django.conf import settings
from django.views.generic import View
import forms as shop_forms
import models as shop_models
from django import shortcuts
from django.contrib import messages
import datetime
from utils import helpers

# globals
if not settings.DEBUG:
    logger = logging.getLogger("django.request")
else:
    logger = logging.getLogger("gs_file")

class ProductsAdmin(View):
    def get(self, request, *args, **kwargs):
        table = dict()
        table['headers'] = ["Name", "Product Code", "Serial number", "Date", "Actions"]
        table['fields'] = ["name", "product_code", "serial_number", "date_added", "admin/snippets/generic_table_actions.html"]

        product_list = shop_models.Product.objects.all()
        page_no = request.GET.get('page')
        page_size = 10
        table["data"] = helpers.paginate(product_list,page_no,page_size)

        return  render(request, "admin/shop/products.html",{
        'table':table,
        })

class ProductsCreate(View):
    def get(self, request, *args, **kwargs):
        form = shop_forms.ProductForm()
        return  render(request, "admin/shop/products_create.html",{
            'form':form,
        })
    def post(self, request, *args, **kwargs):
        form = shop_forms.ProductForm(request.POST)
        if form.is_valid():
            product = shop_models.Product()
            product.name = form.cleaned_data['name']
            product.serial_number = form.cleaned_data['serial_number']
            product.description = form.cleaned_data['description']
            product.category = shop_models.ProductCategories.objects.get(id=form.cleaned_data['category'])
            product.product_code = form.cleaned_data['product_code']
            product.track_stock = form.cleaned_data['track_stock']
            product.requires_shipping = form.cleaned_data['require_shipping']
            product.date_added = datetime.datetime.now()
            product.save()
            messages.success(request, 'Save successful..')
            return shortcuts.redirect("admin_shop_products")
        else:
            messages.error(request, 'Product not saved..')
        return  render(request, "admin/shop/products_create.html",{
            'form':form,
        })
# http://www.jquery-steps.com/Examples
