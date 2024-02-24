from django.urls import path
from online_storeapp.views import buyer_date, get_goods_all, get_orders_all,index, get_all_orders, order_list, new_product, get_all_orders,description_product, get_clients_all


urlpatterns = [
     path('', index, name='index'),
     path('orders/<int:name_client>/', get_all_orders, name='orders'),
     path('order/<int:order_id>/', order_list, name='order'),
     path('buyer_date/', buyer_date, name='buyer_date'),
     path('new_product/', new_product, name='new_product'),
     path('get_all_orders/', get_all_orders, name='get_all_orders'),
     path('description_product/<int:product_id>', description_product, name='description_product'),
     path('get_goods_all/', get_goods_all, name='get_goods_all'),
     path('get_clients_all/', get_clients_all, name='get_clients_all'),
     path('get_orders_all/', get_orders_all, name='get_orders_all'),
    ]