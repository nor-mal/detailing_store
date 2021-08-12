from django.contrib import admin
from .models import Customer, Address

# Register your models here.
admin.site.register(Customer)
admin.site.register(Address)
# admin.site.unregister(auth.models.User)
# admin.site.unregister(auth.models.Group)
