from django.core.management.base import BaseCommand
from online_storeapp.models import GoodsModel, ClientsModel, OrderstModel
import random
from django.utils import timezone
from decimal import Decimal


class Command(BaseCommand):
    help = "Создание тестовых заказов с нескольеами товарами в заказе"
    # подготовлен для дальнейшего развития проекта, пока не задействован

    def handle(self, *args, **kwargs):
        buyers = ClientsModel.objects.all()
        goods = GoodsModel.objects.all()
        for i in range(1, 150):
            buyer = random.choice(buyers)
            order = OrderstModel.objects.create(buyer=buyer)
            total_amout = Decimal(0)
            count_goods = random.randint(1, 5)
            for _ in range(count_goods):
                name_product = random.choice(goods)
                order.goods.add(name_product)
                total_amout += name_product.price_of_product
            order.total_amount_of_order = total_amout
            order.date_of_order = timezone.now()
            order.save()
        print('Создание заказов  выплнено')
