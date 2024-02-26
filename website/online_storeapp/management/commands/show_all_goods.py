from django.core.management.base import BaseCommand
from online_storeapp.models import GoodsModel

class Command(BaseCommand):
    help = "Просмотр всех товаров"

    def handle(self, *args, **kwargs):
        
        goods = GoodsModel.objects.all()
        if goods:
            for product in goods:
                self.stdout.write(str(product))
           
        else:
            text: str = 'Товаров в базе данных нет'
            self.stdout.write(text)
       
