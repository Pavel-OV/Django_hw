
from datetime import timedelta, timezone
from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse
from online_storeapp.models import OrderstModel, ClientsModel


def index(request):
    return render(request, "online_storeapp/index.html")


def get_all_orders(request: HttpResponse, name_client):
    orders = OrderstModel.objects.filter(buyer_id=name_client)
    return render(request, 'online_storeapp/orders.html', {'orders': orders, 'buyer_id': name_client})


def order_list(request: HttpResponse, order_id):
    order = get_object_or_404(OrderstModel, pk=order_id)
    order_id = OrderstModel.objects.get(pk=order_id).pk
    date_order = OrderstModel.objects.get(pk=order_id).date_of_order
    buyer = OrderstModel.objects.get(pk=order_id).buyer.name_client
    price_total_order = OrderstModel.objects.get(
        pk=order_id).total_amount_of_order
    products = OrderstModel.objects.get(pk=order_id).goods.all()
    return render(
        request, 'online_storeapp/order.html', {'order': order, 'order_id': order_id,
                                                'date_order': date_order, 'products': products,
                                                'buyer': buyer, 'price_total_order': price_total_order, })


def orders_by_days(request: HttpResponse, buyer_id, count_day):
    buyer = get_object_or_404(ClientsModel, pk=buyer_id)
    orders = OrderstModel.objects.filter(buyer=buyer)
    current_day =  timezone.now()
    day_of_countdown = current_day - timedelta(days=count_day)
    list_filter_orders = []
    for order in orders:
        if day_of_countdown <= order.date_of_order:
            list_filter_orders.append(order)
    return render(request, 'online_storeapp/orders_by_days.html',
                  {'list_filter_orders': list_filter_orders, 'buyer': buyer, 'count_day': count_day, })
