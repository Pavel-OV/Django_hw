
from datetime import timedelta, timezone
import datetime
from django.shortcuts import redirect, render,  get_object_or_404
from django.http import HttpResponse
from online_storeapp.models import OrderstModel, ClientsModel, GoodsModel
from .forms import NewProduct, Buyer_Order_Date, NumId, Id_Num


def index(request):
    return render(request, "online_storeapp/index.html")


def get_all_orders_client(request: HttpResponse, name_client):
    orders = OrderstModel.objects.filter(buyer_id=name_client)
    return render(request, 'online_storeapp/orders.html', {'orders': orders, 'buyer_id': name_client})


def get_order(request: HttpResponse, order):
    order = OrderstModel.objects.filter(id=order)
    return render(request, 'online_storeapp/orders.html', {'orders': order, 'buyer_id': order})


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


def orders_by_days(request, id_client: int, days: int):
    goods_set = []
    day_of_countdown = datetime.datetime.now() - timedelta(days=days)
    client = ClientsModel.objects.filter(pk=id_client).first()
    orders = OrderstModel.objects.filter(
        buyer=client, date_of_order__gte=day_of_countdown)
    for order in orders:
        products = order.goods.all()
        for product in products:
            if product not in goods_set:
                goods_set.append(product)
    return render(request, 'online_storeapp/orders_by_days.html',
                  {'client': client, 'goods_set': goods_set, 'days': days})


def buyer_date(request):
    if request.method == 'POST':
        form = Buyer_Order_Date(request.POST)
        if form.is_valid():
            days = form.cleaned_data['days']
            id_client = form.cleaned_data['num_id']
            return orders_by_days(request, id_client, days)
        else:
            return render(request, 'online_storeapp/buyer_date.html', {'form': form})
    return render(request, 'online_storeapp/buyer_date.html', {'form': Buyer_Order_Date()})


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
                   'price_of_product': price_of_product, 'quantity_of_product': quantity_of_product,
                   'date_product_added': date_product_added, 'image_product': image_product,
                   "goods": goods,

                   })


def get_goods_all(request):
    all_goods = GoodsModel.objects.all()
    return render(request, 'online_storeapp/get_goods_all.html', {'all_goods': all_goods})


def get_orders_all(request):
    orders = OrderstModel.objects.all()
    return render(request, 'online_storeapp/get_orders_all.html', {'orders': orders})


def get_clients_all(request):
    clients_all = ClientsModel.objects.all()
    return render(request, 'online_storeapp/get_clients_all.html', {'clients_all': clients_all})


def search_num(request):
    if request.method == 'POST':
        form = Id_Num(request.POST)
        if form.is_valid():
            choice = form.cleaned_data.get('choice')
            num_id = form.cleaned_data.get('num_id')
            if choice == 'Client':
                return get_all_orders_client(request, num_id)
            elif choice == 'Order':
                return order_list(request, num_id)
            # elif choice == 'Goods':
            #     return gen_number(request, num_id)
        else:
            return render(request, "online_storeapp/form_id.html", {'form': form})
    return render(request, "online_storeapp/form_id.html", {'form': Id_Num()})
