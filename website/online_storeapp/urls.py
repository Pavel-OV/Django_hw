from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('orders/<int:name_client>/', views.get_all_orders_client, name='orders'),
     path('order/<int:order_id>/', views.order_list, name='order'),
     path('buyer_date/', views.buyer_date, name='buyer_date'),
     path('new_product/', views.new_product, name='new_product'),
     path('get_all_orders/', views.get_all_orders_client, name='get_all_orders'),
     path('description_product/<int:product_id>', views.description_product, name='description_product'),
     path('get_goods_all/', views.get_goods_all, name='get_goods_all'),
     path('get_clients_all/',views. get_clients_all, name='get_clients_all'),
     path('get_orders_all/', views.get_orders_all, name='get_orders_all'),
     path("form_id/", views.search_num, name="form_id"),
    ]