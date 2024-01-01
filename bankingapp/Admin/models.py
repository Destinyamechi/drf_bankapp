from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    age = models.CharField(max_length=50,null =True, blank = True)
    gender = models.CharField(max_length=50,null =True, blank = True)
    address = models.CharField(max_length=50,null =True, blank = True)
    state_of_origin = models.CharField(max_length=50,null =True, blank = True)
    nationality = models.CharField(max_length=50,null =True, blank = True)
    phone_number = models.CharField(max_length=50,null =True, blank = True)
    
    