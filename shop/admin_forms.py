from django import forms
import models as shop_models
from django.contrib.auth.models import User

class ProductForm(forms.Form):
    vendor = forms.ModelChoiceField(queryset=shop_models.Vendors.objects.all())
    category = forms.ModelChoiceField(queryset=shop_models.ProductCategories.objects.all())
    name = forms.CharField()
    product_code = forms.IntegerField()
    serial_number = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    # date_added = forms.DateField()

class ProductImageForm(forms.Form):
    multiple_form = True
    multiple_form_id = "product-images-form"
    count = 5
    field_types = ["caption", "display_order", "image"]

    caption1 = forms.CharField(required=False)
    display_order1 = forms.IntegerField(required=False)
    image1 = forms.ImageField(required=False)
    image1_pk = forms.CharField(widget=forms.HiddenInput,required=False,label='')

    caption2 = forms.CharField(required=False)
    display_order2 = forms.IntegerField(required=False)
    image2 = forms.ImageField(required=False)
    image2_pk = forms.CharField(widget=forms.HiddenInput,required=False,label='')

    caption3 = forms.CharField(required=False)
    display_order3 = forms.IntegerField(required=False)
    image3 = forms.ImageField(required=False)
    image3_pk = forms.CharField(widget=forms.HiddenInput,required=False,label='')

    caption4 = forms.CharField(required=False)
    display_order4 = forms.IntegerField(required=False)
    image4 = forms.ImageField(required=False)
    image4_pk = forms.CharField(widget=forms.HiddenInput,required=False,label='')

    caption5 = forms.CharField(required=False)
    display_order5 = forms.IntegerField(required=False)
    image5 = forms.ImageField(required=False)
    image5_pk = forms.CharField(widget=forms.HiddenInput,required=False,label='')


class ProductPriceAndStockForm(forms.Form):
    vendor_price = forms.FloatField()
    selling_price = forms.FloatField()
    discount_price = forms.FloatField()
    quantity_in_stock = forms.IntegerField()
    reorder_point = forms.IntegerField()
    reorder_quantity = forms.IntegerField()
    track_stock = forms.BooleanField(required=False)
    require_shipping = forms.BooleanField(required=False)

class ProductCategoryForm(forms.ModelForm):
    parent = forms.ModelChoiceField(queryset=shop_models.ProductCategories.objects.all())
    class Meta:
        model = shop_models.ProductCategories
        fields = ["title", "slug", "depth", "parent",]

class VendorForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    class Meta:
        model = shop_models.Vendors
        fields =  ["name", "code", "user"]

class AddressForm(forms.ModelForm):
    pass
    class Meta:
        model = shop_models.Address
        fields = ["title", "first_name", "last_name", "line1", "line2", "line3", "line4", "phone", "state", "postcode"]
