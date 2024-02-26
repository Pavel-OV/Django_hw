from django.core.management.base import BaseCommand
from online_storeapp.models import GoodsModel, ClientsModel
from random import randint
from django.utils import lorem_ipsum

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for i in range(1,1000):
            product = GoodsModel(
                 name_product =f'Товар {i}',
                 description_product =lorem_ipsum.paragraphs(2),
                 price_of_product = randint(1000, 100000),
                 quantity_of_product = randint(1,20)
                )
            product.save()
        print('Создание товаров выплнено')
