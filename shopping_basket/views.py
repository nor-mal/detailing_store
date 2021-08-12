import datetime
import json
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from paypalcheckoutsdk.orders import OrdersGetRequest
from shopping_basket.paypal import PayPalClient

from accounts.models import Customer
from products.models import Product
from shopping_basket.extras import generate_order_id
from shopping_basket.models import OrderItem, Order


# Create your views here.


def get_customer_pending_order(request):
    # get order for the correct customer
    customer = get_object_or_404(Customer, user=request.user)
    order = Order.objects.filter(owner=customer, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0


@login_required
def add_to_basket(request, **kwargs):
    # get the customer profile
    user_profile = get_object_or_404(Customer, user=request.user.customer.customer_id)
    # filter products by ID
    product = Product.objects.filter(product_id=kwargs.get("item_id", "")).first()

    # create OrderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(product=product)

    # create Order assosiated with the customer
    customer_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    customer_order.items.add(order_item)
    if status:
        # generate a ref code:
        customer_order.ref_code = generate_order_id()
        customer_order.save()
    # show confirmation messages and redirect to the same page
    messages.info(request, 'Item added to basket')
    return redirect(reverse('home_page'))


@login_required()
def delete_from_basket(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)

    # recalculation of the basket total after the item was deleted
    product = Product.objects.filter(name=item_to_delete[0])
    prod_price = product.values_list('price')[0][0]  # grabbing product price
    total_price = request.session['total_price']
    basket_total = Decimal(total_price) - (prod_price + ((prod_price * 20) / 100))

    if item_to_delete.exists():
        item_to_delete[0].delete()
        request.session['total_price'] = str(basket_total)
        messages.info(request, 'Item has been deleted')

    return redirect(reverse('shopping_basket:order_summary'))


@login_required()
def order_summary(request, **kwargs):
    existing_order = get_customer_pending_order(request)

    if existing_order != 0:
        order_id = existing_order.id

        # empty and not paid order delete
        if not existing_order.items.all() and existing_order.paid is False:
            order_delete = Order.objects.filter(ref_code=existing_order.ref_code)
            order_delete.delete()
    else:
        order_id = None

    total_price = request.session['total_price']

    context = {
        'order': existing_order,
        'id': order_id,
        'total_price': total_price,
    }
    return render(request, 'shopping_basket/order_summary.html', context)


# View of all orders done by currently logged Customer
@login_required()
def orders_view(request, **kwargs):
    orders = Order.objects.filter(owner=request.user.customer)
    total_price = request.session['total_price']
    return render(request, 'shopping_basket/orders.html', {'orders': orders, 'total_price': total_price})


@login_required()
def order_details(request, ref_code, **kwargs):
    total_price = request.session['total_price']

    order = Order.objects.filter(ref_code=ref_code, owner=request.user.customer)

    return render(request, 'shopping_basket/order_details.html', {'order': order, 'total_price': total_price})


@login_required()
def checkout(request, **kwargs):
    existing_order = get_customer_pending_order(request)

    total_price = request.session['total_price']

    context = {
        'order': existing_order,
        'total_price': total_price,
    }
    return render(request, 'shopping_basket/checkout.html', context)


@login_required()
def process_payment(request):
    existing_order = get_customer_pending_order(request)

    PPClient = PayPalClient()

    body = json.loads(request.body)
    data = body['orderID']

    requestorder = OrdersGetRequest(data)
    response = PPClient.client.execute(requestorder)

    if response.status_code == 200:
        existing_order.is_ordered = True
        existing_order.paid = True
        existing_order.date_ordered = datetime.datetime.now()
        existing_order.payment_id = response.result.id
        existing_order.payment_email = response.result.payer.email_address
        existing_order.total_paid = response.result.purchase_units[0].amount.value
        existing_order.save()

    request.session['total_price'] = str(0)

    return JsonResponse("Payment completed!", safe=False)


@login_required()
def payment_successful(request):
    total_price = request.session['total_price']

    orders = Order.objects.filter(owner=request.user.customer)
    messages.info(request, 'Your order is completed. Thank you')

    return render(request, 'shopping_basket/orders.html', {'total_price': total_price, 'orders': orders})
