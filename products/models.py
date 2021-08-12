from django.db import models
# Create your models here.


class Product(models.Model):
    product_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=250, blank=False)
    description = models.CharField(max_length=400, blank=False)
    product_type = models.CharField(max_length=250, blank=False)
    product_brand = models.CharField(max_length=200, blank=False)
    photo = models.ImageField(upload_to='products')
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name
