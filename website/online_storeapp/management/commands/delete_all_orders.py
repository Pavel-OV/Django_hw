from django.core.management.base import BaseCommand
from online_storeapp.models import OrderstModel

class Command(BaseCommand):
    help = "Удаление всех заказов"
    def handle(self, *args, **kwargs):

        products = OrderstModel.objects.all()

        if products:
            for product in products:
                self.stdout.write(str(product))
                product.delete()
        else:
            text: str = 'Продуктов нет в базе данных'
            self.stdout.write(text)
    



    # def handle(self, *args, **kwargs):
    #     OrderstModel.objects.all().delete()
    #     print("Все заказы удалены")
       
