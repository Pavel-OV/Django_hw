from django.core.management.base import BaseCommand
from online_storeapp.models import GoodsModel


class Command(BaseCommand):
    help = "Удаление всех продуктов"

    def handle(self, *args, **kwargs):
        products = GoodsModel.objects.all()
        if products:
            for product in products:
                self.stdout.write(str(product))
                product.delete()
        else:
            text: str = 'Продуктов нет в базе данных'
            self.stdout.write(text)
