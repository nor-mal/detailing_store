from django.urls import path
from .views import (
    add_to_basket,
    delete_from_basket,
    order_summary,
    checkout,
    process_payment,
    payment_successful,
    orders_view,
    order_details,
)

app_name = 'shopping_basket'

urlpatterns = [
    path('add_to_basket/<item_id>/', add_to_basket, name='add_to_basket'),
    path('order_summary/', order_summary, name='order_summary'),
    path('item/delete/<item_id>/', delete_from_basket, name='delete_item'),
    path('checkout/<id>/', checkout, name='checkout'),
    path('all_orders/', orders_view, name='orders_view'),
    path('order_details/<ref_code>/', order_details, name='order_details'),
    path('payment_processing/', process_payment, name='process_payment'),
    path('payment-successful/', payment_successful, name='payment_successful'),
]
