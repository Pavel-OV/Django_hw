from django.urls import path
from online_storeapp.views import index, get_all_orders, order_list

urlpatterns = [
     path('', index, name='index'),
     path('orders/<int:name_client>/', get_all_orders, name='orders'),
     path('order/<int:order_id>/', order_list, name='order'),
    ]