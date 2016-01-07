from django import forms
import models as shop_models

class ProductForm(forms.Form):
    category = forms.ModelChoiceField(queryset=shop_models.ProductCategories.objects.all())
    name = forms.CharField()
    product_code = forms.IntegerField()
    serial_number = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    # date_added = forms.DateField()

class ProductImageForm(forms.ModelForm):
    # name = forms.CharField(max_length=128)
    # display_order = forms.IntegerField()
    # image = forms.ImageField()
    pass
    class Meta:
        model = shop_models.ProductImages
        fields = ['caption','display_order','image']


class ProductPriceAndStockForm(forms.Form):
    vendor = forms.ChoiceField(choices=shop_models.Vendors.objects.all().values_list('id','name'))
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
