from django.core.management.base import BaseCommand
from online_storeapp.models import ClientsModel


class Command(BaseCommand):
    help = "Удаление всех клиентов"

    def handle(self, *args, **kwargs):

        clients = ClientsModel.objects.all()

        if clients:
            for client in clients:
                self.stdout.write(str(client))
                client.delete()
        else:
            text: str = 'Клиентов нет в базе данных'
            self.stdout.write(text)