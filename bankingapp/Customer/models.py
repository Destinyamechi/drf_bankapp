from django.db import models
from Admin.models import CustomUser

# Create your models here. 
class customerAccountProfile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,null =True, blank = True)
    bvn = models.IntegerField(default=00000000000,null =True, blank = True)

    def __str__(self):
        return f'{self.user}'