from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone_numer = models.CharField(max_length=11)
    is_author = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)