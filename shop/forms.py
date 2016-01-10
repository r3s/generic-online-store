from django import forms
import models as shop_models

class ProductForm(forms.Form):
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

    caption2 = forms.CharField(required=False)
    display_order2 = forms.IntegerField(required=False)
    image2 = forms.ImageField(required=False)

    caption3 = forms.CharField(required=False)
    display_order3 = forms.IntegerField(required=False)
    image3 = forms.ImageField(required=False)

    caption4 = forms.CharField(required=False)
    display_order4 = forms.IntegerField(required=False)
    image4 = forms.ImageField(required=False)

    caption5 = forms.CharField(required=False)
    display_order5 = forms.IntegerField(required=False)
    image5 = forms.ImageField(required=False)


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
