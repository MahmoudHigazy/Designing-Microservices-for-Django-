from django.db import models
from django.contrib.auth.models import User

class Pizzeria(models.Model):
    owner = models.ForeignKey(User, on_delete=models.
    CASCADE)
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=40)

class Pizza(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    thumbnail_url = models.URLField(null=True, blank=True)
    approved = models.BooleanField(default=False)
    creator = models.ForeignKey(Pizzeria, on_delete=models.
    CASCADE)
    TYPES = [
        ('Meat', 'Meat'),
        ('Vegetarian', 'Vegetarian'),
        ('Vegan', 'Vegan'),
    ]
    types = models.CharField(
        max_length=12, choices=TYPES, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.
    CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)