from django.core.management.base import BaseCommand
from online_storeapp.models import ClientsModel


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for i in range(0, 9):
            client = ClientsModel(
                name_client=f'Покупатель {i}',
                email=f'email{i}@mail.ru',
                phone=f'99{i}8{i}54{i}2{i}',
                customer_address=f'Город{i}, улица{i}, дом{i}'
            )
            client.save()
        print('Создание клиентов выплнено')
