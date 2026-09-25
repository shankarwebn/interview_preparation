from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Account(AbstractUser):
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)


    def __str__(self):
        return self.username
    

class Post(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='posts')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
