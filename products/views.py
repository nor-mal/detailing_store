# from django.views.generic import ListView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from products.models import Product
#
# # Create your views here.
# from shopping_basket.models import Order
#
#
# class ProductListView(LoginRequiredMixin, ListView):
#     model = Product
#     template_name = 'products/product_page.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         products = Product.objects.all()
#         filtered_orders = Order.objects.filter(owner=self.request.user.customer, is_ordered=False)
#         current_order_products = []
#         if filtered_orders.exists():
#             user_order = filtered_orders[0]
#             user_order_items = user_order.items.all()
#             current_order_products = [product.product for product in user_order_items]
#
#         product = filtered_orders[0].items.all()
#         total_price = sum([item.product.price for item in product])
#
#         context = {
#             # 'products': products,
#             # 'current_order_products': current_order_products,
#             'total_price': total_price,
#         }
#         return context
