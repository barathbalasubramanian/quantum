from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Product(models.Model):
    username = models.CharField(max_length=15 )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        print(f"{self.name} - ${self.price}")
        return f"{self.name} - ${self.price}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    domain = models.CharField(max_length=100, blank=True)

