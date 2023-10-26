from django.db import models


# Create your models here.

# do not create user yourself, use django.contrib.auth.models.User
# Dr. should teach us later, no edit for now
class Account(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.username
