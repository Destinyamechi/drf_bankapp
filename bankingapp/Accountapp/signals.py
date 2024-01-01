from django.db.models.signals import post_save
from Customer.models import customerAccountProfile
from django.dispatch import receiver
from .models import accountDetails
import random

@receiver(post_save, sender = customerAccountProfile)
def create_profile(sender,instance, created, **kwargs):

    if created:
        user = instance.user
        accountDetails.objects.create(
            account_owner = instance,
            account_name = f"{user.first_name}{user.last_name}",
            account_number = random.randint(1000000000, 9999999999),
            account_balance = random.randint(1, 9999999)
            )

@receiver(post_save,sender=customerAccountProfile)
def profile_save(sender, instance,**kwargs ):
        instance.accountdetails.save()
