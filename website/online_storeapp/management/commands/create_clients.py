from django.core.management.base import BaseCommand
from online_storeapp.models import ClientsModel
from random import randint


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for i in range(1, 250):
            client = ClientsModel(
                name_client=f'Покупатель {i}',
                email=f'email{i}@mail.ru',
                phone=f'9{randint(100000000, 999999999)}',
                customer_address=f'Город{i}, улица{i}, дом{i}'
            )
            client.save()
        print('Создание клиентов выплнено')
