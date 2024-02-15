from django.core.management.base import BaseCommand
from online_storeapp.models import ClientsModel


class Command(BaseCommand):
    help = 'Просмотр всех клиентов'
    def handle(self, *args, **kwargs):

        clients = ClientsModel.objects.all()
        if clients:
            for client in clients:
                self.stdout.write(str(client))

        else:
            text: str = 'Клиентов в базе данных нет'
            self.stdout.write(text)
