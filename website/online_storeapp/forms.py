from django import forms
from .models import GoodsModel, OrderstModel

class NewProduct(forms.ModelForm):
    class Meta:
        model = GoodsModel
        fields = ['name_product','description_product','price_of_product','quantity_of_product', 'image_product']


class Buyer_Order_Date(forms.Form):
    num_id = forms.IntegerField()
    choice = forms.ChoiceField(choices=[('Неделя',7),('Месяц',30),('Год',365)])