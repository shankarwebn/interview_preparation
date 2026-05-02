# shop/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.username   # ✅ fix


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"