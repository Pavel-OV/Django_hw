from django.urls import path
from online_storeapp.views import index, get_all_orders, order_list, orders_by_days

urlpatterns = [
     path('', index, name='index'),
     path('orders/<int:name_client>/', get_all_orders, name='orders'),
     path('order/<int:order_id>/', order_list, name='order'),
     path('orders_by_days/<int:buyer_id>/<int:count_day>', orders_by_days, name='orders_by_days'),
    ]