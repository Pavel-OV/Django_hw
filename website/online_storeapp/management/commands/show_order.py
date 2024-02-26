from django.core.management.base import BaseCommand
from online_storeapp.models import OrderstModel


class Command(BaseCommand):
    help = 'Просмотр заказа по ID (PK)'

    def add_arguments(self, parser):
        parser.add_argument('id_order', type=int)

    def handle(self, *args, **kwargs):
        id_order = kwargs['id_order']
        order = OrderstModel.objects.get(pk=id_order)
        order.save()
        print(order)
        