from django.db import models

from accounts.models import Customer
from products.models import Product
# Create your models here.


class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.product.name

    def update_quantity(self, quantity):
        self.quantity = self.quantity + quantity
        self.save()


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    total_paid = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    payment_id = models.CharField(max_length=200, null=True)
    payment_email = models.EmailField(null=True)

    def get_basket_items(self):
        return self.items.all()

    def get_basket_sum(self):
        return sum([item.product.price for item in self.items.all()])

    def get_basket_vat(self):
        return (self.get_basket_sum()*20)/100

    def get_basket_total(self):
        return self.get_basket_sum() + self.get_basket_vat()

    def __str__(self):
        return '{0}-{1}'.format(self.ref_code, self.owner.user)
