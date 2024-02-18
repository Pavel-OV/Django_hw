from django import forms
from .models import GoodsModel

class NewProduct(forms.ModelForm):
    class Meta:
        model = GoodsModel
        fields = ['name_product','description_product','price_of_product','quantity_of_product', 'image_product']
