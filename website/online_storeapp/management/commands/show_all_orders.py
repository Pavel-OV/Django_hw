from django.core.management.base import BaseCommand
from online_storeapp.models import OrderstModel

class Command(BaseCommand):
    help = "Просмотр всех заказов"

    def handle(self, *args, **kwargs):
        
        orders = OrderstModel.objects.all()
        if orders:
            for order in orders:
                self.stdout.write(str(order))
           
        else:
            text: str = 'Заказов нет в базе данных'
            self.stdout.write(text)
       
