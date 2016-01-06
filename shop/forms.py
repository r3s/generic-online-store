from django import forms
import models as shop_models

class ProductForm(forms.Form):
    category = forms.ChoiceField(choices=shop_models.ProductCategories.objects.all().values_list('id','title'))
    name = forms.CharField()
    product_code = forms.IntegerField()
    serial_number = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    # date_added = forms.DateField()
    track_stock = forms.BooleanField()
    require_shipping = forms.BooleanField()

class ProductImageForm(forms.Form):
    name = forms.CharField(max_length=128)
    display_order = forms.IntegerField()
    image = forms.ImageField()
