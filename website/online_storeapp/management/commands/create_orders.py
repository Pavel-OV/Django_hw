from django.core.management.base import BaseCommand
from online_storeapp.models import GoodsModel, ClientsModel, OrderstModel
import random
from django.utils import timezone
from decimal import Decimal


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        buyers = ClientsModel.objects.all()
        goods = GoodsModel.objects.all()
        for i in range(1, 150):
            buyer = random.choice(buyers)
            order = OrderstModel.objects.create(buyer=buyer)
           
            
            name_product = random.choice(goods)
            order.goods.add(name_product)
               
            order.total_amount_of_order = name_product.price_of_product
            order.date_of_order = timezone.now()
            order.save()
        print('Создание заказов  выплнено')
