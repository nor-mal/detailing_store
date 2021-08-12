from django.views.generic import TemplateView
from django.shortcuts import render

from products.models import Product
from shopping_basket.models import Order


class HomePageView(TemplateView):
    model = Product
    template_name = 'products/product_page.html'

    def get_context_data(self, **kwargs):
        prod_type = self.request.GET.get('prod_type')
        prod_brand = self.request.GET.get('prod_brand')

        # sidenav Product views filter logic based on the above input
        if prod_type is not None:
            products = Product.objects.filter(product_type=prod_type).order_by('name')
        elif prod_brand is not None:
            products = Product.objects.filter(product_brand=prod_brand)

        else:
            products = Product.objects.all().order_by('name')

        total_price = 0

        if self.request.user.is_authenticated:
            # Finding total price for the Orders made by the currently logged Customer so that it can be
            # shown in the top navbar
            filtered_orders = Order.objects.filter(owner=self.request.user.customer, is_ordered=False)
            if filtered_orders.exists():
                product = filtered_orders[0].items.all()
                total = sum([item.product.price for item in product])
                total_price = str(total + (total*20)/100)

        # retrieving product_type's to display them as the unique set in the side navbar
        product_types = set([item.product_type for item in products])

        # retrieving product_brand's to display them as the unique set in the side navbar
        product_brands = set([item.product_brand for item in products])

        context = {
            'products': products,
            'product_types': product_types,
            'product_brands': product_brands,
            'total_price': total_price,
        }

        self.request.session['total_price'] = total_price
        return context


def about_us_view(request):
    total_price = request.session['total_price']
    return render(request, 'about_us.html', {'total_price': total_price})


def contact_us_view(request):
    total_price = request.session['total_price']
    return render(request, 'contact_us.html', {'total_price': total_price})
