
from datetime import timedelta, timezone
from django.shortcuts import redirect, render,  get_object_or_404
from django.http import HttpResponse
from online_storeapp.models import OrderstModel, ClientsModel, GoodsModel
from .forms import NewProduct, Buyer_Order_Date
from django.core.files.storage import FileSystemStorage


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


def new_product(request):
    if request.method == 'POST':
        form = NewProduct(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            num_id = product.pk
            # {'orders': orders, 'buyer_id': name_client}
            return render(request, 'online_storeapp/description_product.html', {'product': product, 'product_id': num_id})
        else:
            return render(request, 'online_storeapp/new_product.html', {'form': form})
    return render(request, 'online_storeapp/new_product.html', {'form': NewProduct()})


def description_product(request: HttpResponse, product_id):
    # product = GoodsModel.objects.all().filter(pk=product_id)
    # context_dict = {'product':product}
    # return render(request, 'online_storeapp/description_product.html', context_dict)
    goods = GoodsModel.objects.all().filter(pk=product_id)
    name_product = GoodsModel.objects.get(pk=product_id)
    # product = GoodsModel.objects.get(pk=num_id).pk
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
                   "goods": goods, 'product_id': product_id
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
