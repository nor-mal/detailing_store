from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from accounts.models import Customer


@receiver(post_save, sender=User)
def customer_creation(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
