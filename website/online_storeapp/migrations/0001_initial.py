# Generated by Django 5.0.1 on 2024-02-09 08:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_client', models.CharField(max_length=150, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('phone', models.CharField(max_length=10, verbose_name='Телефон')),
                ('customer_address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('date_of_registration', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=200, verbose_name='Название')),
                ('description_product', models.TextField(verbose_name='Описание')),
                ('price_of_product', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена')),
                ('quantity_of_product', models.PositiveIntegerField(verbose_name='Количество')),
                ('date_product_added', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
            ],
        ),
        migrations.CreateModel(
            name='OrderstModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount_of_order', models.DecimalField(decimal_places=2, default=0, max_digits=2, verbose_name='Итоговая цена')),
                ('date_of_order', models.DateTimeField(auto_now_add=True, verbose_name='Дата оформления заказа')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_storeapp.clientsmodel', verbose_name='Клиент')),
                ('goods', models.ManyToManyField(to='online_storeapp.goodsmodel', verbose_name='Продукт')),
            ],
        ),
    ]