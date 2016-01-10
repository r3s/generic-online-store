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
        product_image_form = shop_forms.ProductImageForm()
        product_price_form = shop_forms.ProductPriceAndStockForm()
        return  render(request, "admin/shop/products_create.html",{
            'formbundle':[
            ("Product details",form),
            ("Product image",product_image_form),
            ("Price and stock",product_price_form)],
        })
    def post(self, request, *args, **kwargs):
        product_image_form = shop_forms.ProductImageForm(request.POST, request.FILES)
        form = shop_forms.ProductForm(request.POST)
        product_price_form = shop_forms.ProductPriceAndStockForm(request.POST)
        if form.is_valid() and product_image_form.is_valid() and product_price_form.is_valid():
            product = shop_models.Product()
            product.name = form.cleaned_data['name']
            product.serial_number = form.cleaned_data['serial_number']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.product_code = form.cleaned_data['product_code']
            product.track_stock = product_price_form.cleaned_data['track_stock']
            product.requires_shipping = product_price_form.cleaned_data['require_shipping']
            product.date_added = datetime.datetime.now()
            product.save()

            import ipdb
            for i in range(1,product_image_form.count):
                ipdb.set_trace()
                if request.FILES.has_key('image'+str(i)):
                    product_image = shop_models.ProductImages(
                        product = product,
                        caption = product_image_form.cleaned_data["caption"+str(i)] or "NC",
                        display_order = product_image_form.cleaned_data["display_order"+str(i)] or 5,
                        image = request.FILES['image'+str(i)]
                    )
                    product_image.save()

            vendor = shop_models.Vendors.objects.get(id=product_price_form.cleaned_data['vendor'])

            stock = shop_models.ProductStock()
            stock.vendor = vendor
            stock.product = product
            stock.quantity = product_price_form.cleaned_data['quantity_in_stock']
            stock.reorder_point = product_price_form.cleaned_data['reorder_point']
            stock.reorder_quantity = product_price_form.cleaned_data['reorder_quantity']
            stock.save()

            price = shop_models.ProductPrices()
            price.vendor = vendor
            price.product = product
            price.vendor_price =  product_price_form.cleaned_data['vendor_price']
            price.selling_price =  product_price_form.cleaned_data['selling_price']
            price.discount_price =  product_price_form.cleaned_data['discount_price']
            price.vendor_price =  product_price_form.cleaned_data['vendor_price']
            price.vendor_price =  product_price_form.cleaned_data['vendor_price']
            price.save()



            messages.success(request, 'Save successful..')
            return shortcuts.redirect("admin_shop_products")
        else:
            messages.error(request, 'Product not saved..')
        return  render(request, "admin/shop/products_create.html",{
            'formbundle':[
            ("Product details",form),
            ("Product image",product_image_form),
            ("Price and stock",product_price_form)],
        })

class CategoryAdmin(View):
    def get(self, request, *args, **kwargs):
        table = dict()
        table['headers'] = ["Title", "Slug", "Depth", "Parent","Actions"]
        table['fields'] = ["title", "slug", "depth", "parent", "admin/snippets/generic_table_actions.html"]
        category_list = shop_models.ProductCategories.objects.all()
        page_no = request.GET.get('page')
        page_size = 10
        table["data"] = helpers.paginate(category_list,page_no,page_size)

        return  render(request, "admin/shop/categories.html",{
        'table':table,
        })

class CategoriesCreate(View):
    def get(self, request, *args, **kwargs):
        form = shop_forms.ProductCategoryForm()
        return  render(request, "admin/shop/categories_create.html",{
            'formbundle':[
            ("Category details",form),]
        })
    def post(self, request, *args, **kwargs):
        form = shop_forms.ProductCategoryForm(request.POST)
        if form.is_valid():
            category_data = form.save(commit=False) #Modelform
            category_data.parent_slug =  category_data.parent.slug
            category_data.save()

            messages.success(request, 'Save successful..')
            return shortcuts.redirect("admin_shop_categories")
        else:
            messages.error(request, 'Product not saved..')
        return  render(request, "admin/shop/categories_create.html",{
            'formbundle':[
            ("Category details",form),]
        })
