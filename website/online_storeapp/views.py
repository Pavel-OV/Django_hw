
from datetime import timedelta, timezone
from django.shortcuts import redirect, render,  get_object_or_404
from django.http import HttpResponse
from online_storeapp.models import OrderstModel, ClientsModel, GoodsModel
from .forms import NewProduct, Buyer_Order_Date
from django.core.files.storage import FileSystemStorage

menu = []


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
    current_day = timezone.now()
    day_of_countdown = current_day - timedelta(days=count_day)
    list_filter_orders = []
    for order in orders:
        if day_of_countdown <= order.date_of_order:
            list_filter_orders.append(order)
    return render(request, 'online_storeapp/orders_by_days.html',
                  {'list_filter_orders': list_filter_orders, 'buyer': buyer, 'count_day': count_day, })


def new_product(request):
    if request.method == 'POST':
        form = NewProduct(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            num_id = product.pk
            form = NewProduct()
            return description_product(request, num_id)
        else:
            return render(request, 'online_storeapp/new_product.html', {'form': form})
    return render(request, 'online_storeapp/new_product.html', {'form': NewProduct()})


def description_product(request: HttpResponse, product_id):
    goods = GoodsModel.objects.all().filter(pk=product_id)
    name_product = GoodsModel.objects.get(pk=product_id)
    description_product = GoodsModel.objects.get(
        pk=product_id).description_product
    price_of_product = GoodsModel.objects.get(
        pk=product_id).price_of_product
    quantity_of_product = GoodsModel.objects.get(
        pk=product_id).quantity_of_product
    date_product_added = GoodsModel.objects.get(
        pk=product_id).date_product_added
    image_product = GoodsModel.objects.get(
        pk=product_id).image_product
    return render(request,
                  'online_storeapp/description_product.html',
                  {'name_product': name_product, 'description_product': description_product,
                   'price_of_product':price_of_product, 'quantity_of_product':quantity_of_product,
                    'date_product_added': date_product_added, 'image_product': image_product,
                    "goods":goods,                   

                   })


def buyer_date(request):
    if request.method == 'POST':
        form = Buyer_Order_Date(request.POST)
        if form.is_valid():
            choice = form.cleaned_data.get('Неделя')
            num_id = form.cleaned_data.get('altempts')
            # if choice == 'Неделя':
            #     return orders_by_days(request, num_id)
            # elif choice == 'Месяц':
            #     return orders_by_days(request, num_id)
            # elif choice == 'Год':
            #     return orders_by_days(request, num_id)
        else:
            return render(request, "online_storeapp/index.html", {'form': form})
    return render(request, "online_storeapp/index.html", {'form': Buyer_Order_Date()})