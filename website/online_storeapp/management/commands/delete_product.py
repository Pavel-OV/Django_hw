from django.core.management.base import BaseCommand
from online_storeapp.models import GoodsModel


class Command(BaseCommand):
    help = "Удалить товар по ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='id товара')  # pk - id

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = GoodsModel.objects.filter(
            pk=pk).first()  # поиск строки по id
        if product is not None:
            product.delete()  # удаление найденной строки

        self.stdout.write(f'Товар удалён по номеру {pk}')
