from django.core.management.base import BaseCommand
from online_storeapp.models import ClientsModel


class Command(BaseCommand):
    help = 'Просмотр клиента по ID (PK)'

    def add_arguments(self, parser):
        parser.add_argument('name_client', type=int, help='клиент по ID')


    def handle (self, *args, **kwargs):
        id_client:int = kwargs['name_client']
        name = ClientsModel.objects.filter(pk=id_client)          # поиск строки по id
        if name:
            text= name
        else:
            text = 'Клиента с таким ID нет в базе данных'
        # self.stdout.write(text)
        print(*text)
        
        # self.stdout.write(f'{name}')
