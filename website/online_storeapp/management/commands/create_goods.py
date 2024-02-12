from django.core.management.base import BaseCommand
from online_storeapp.models import GoodsModel, ClientsModel
from random import randint
from django.utils import lorem_ipsum

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for i in range(0,8):
            product = GoodsModel(
                 name_product =f'Товар {i}',
                 description_product =lorem_ipsum.paragraphs(4),
                 price_of_product = randint(1000, 1000000),
                 quantity_of_product = randint(0,15)
                )
            product.save()
        print('Создание товаров выплнено')
