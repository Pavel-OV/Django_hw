from django.core.management.base import BaseCommand
from online_storeapp.models import GoodsModel


class Command(BaseCommand):
    help = "Удалить  группу товаров по ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='id товара')
        parser.add_argument('pk_end', type=int, help='id товара')  # pk - id

    def handle(self, *args, **kwargs):
        pk_start = kwargs.get('pk')
        pk_end = kwargs.get('pk_end')
        for pk in range(pk_start, pk_end+1):
            product = GoodsModel.objects.filter(pk=pk).first()
            if product is not None:
                product.delete()
                self.stdout.write(f'Товар удалён по номеру {pk}')
