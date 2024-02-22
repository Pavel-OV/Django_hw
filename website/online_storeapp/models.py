from django.db import models
from django.urls import reverse


class ClientsModel(models.Model):
    name_client = models.CharField(max_length=150,  verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    phone = models.CharField(max_length=10, verbose_name='Телефон')
    customer_address = models.CharField(max_length=200, verbose_name='Адрес')
    date_of_registration = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата регистрации')

    def __str__(self):
        return self.name_client


class GoodsModel(models.Model):
    name_product = models.CharField(max_length=200, verbose_name='Название')
    description_product = models.TextField(verbose_name='Описание')
    price_of_product = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='Цена')
    quantity_of_product = models.PositiveIntegerField(
        verbose_name='Количество')
    date_product_added = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата добавления')
    image_product = models.ImageField(
        upload_to="images/", default='No image', blank=True, null=True)

    def get_absolute_url(self):
        return reverse("order_list", kwargs={'order_id': self.pk})

    def __str__(self):
        return self.name_product


class OrderstModel(models.Model):
    buyer = models.ForeignKey(
        ClientsModel, on_delete=models.CASCADE, verbose_name='Клиент')
    goods = models.ManyToManyField(GoodsModel, verbose_name='Продукт')
    total_amount_of_order = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name='Итоговая цена')
    date_of_order = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата оформления заказа')

    def __str__(self):
        return   self.buyer.name_client
           
