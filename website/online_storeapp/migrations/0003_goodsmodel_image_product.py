# Generated by Django 5.0.1 on 2024-02-18 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_storeapp', '0002_alter_orderstmodel_total_amount_of_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsmodel',
            name='image_product',
            field=models.ImageField(default='No image', upload_to='images/'),
        ),
    ]
