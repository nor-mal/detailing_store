from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy

from products.models import Product
# Create your models here.


class Customer(models.Model):
    customer_id = models.AutoField(unique=True, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + f' profile'


class Address(models.Model):
    id = models.AutoField(primary_key=True, unique=True, blank=True)
    address_name = models.CharField(max_length=60, blank=True)
    address_line_1 = models.CharField(max_length=120, null=True)
    address_line_2 = models.CharField(max_length=120, null=True)
    city = models.CharField(max_length=120, null=True)
    postcode = models.CharField(max_length=120, null=True)
    county = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    del_address = models.BooleanField(default=False)
    bill_address = models.BooleanField(default=False)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.address_name + f' --> ' + self.customer.user.username

    def get_absolute_url(self):
        return reverse_lazy('accounts:address_view', kwargs={'pk': self.pk})
