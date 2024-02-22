from django.contrib import admin
from .models import ClientsModel,GoodsModel,OrderstModel


@admin.register(ClientsModel)
class ClientsModelAdmin(admin.ModelAdmin):
    list_display = ['name_client', 'phone',]
    readonly_fields = ['date_of_registration',]
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name_client'],
            },
        ),
        (
            'Полная информация о клиенте',
            {
                'classes': ['collapse'],
                'description': 'Информация о клиенте',
                'fields': ['date_of_registration','email','customer_address'],
            },
        ),

        (
            'Контакты',
            {
                'description': 'Контакты клиента',
                'fields': ['phone', ],
            }
        ),
    ]

@admin.register(GoodsModel)
class GoodsModelAdmin(admin.ModelAdmin):
    list_display = ['id','name_product', 'price_of_product','quantity_of_product','date_product_added',]


@admin.register(OrderstModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['buyer','total_amount_of_order','date_of_order','id',]
    readonly_fields = ['buyer' ,'goods']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['buyer'],
            },
        ),
        (
            'Заказы',
            {
                'classes': ['goods'],
                'description': 'Текст статьи',
                'fields': ['goods',],
            },
        ),
        (
            'Катигория и дата публикации и изменений',
            {
                'fields': ['total_amount_of_order',]

            }
        ),
        (
            'Число просмотров и статус статьи',
            {
                'description': 'Число просмотров и статус статьи',
                'fields': ['date_of_order'],
            }
        ),
    ]


