from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="photos/")
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=CASCADE, related_name="categories")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Cart (models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE ,related_name="user")
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sessions

class CartDetail (models.Model):
    cart = models.ForeignKey(Cart, on_delete=CASCADE ,related_name="cart")
    product = models.ForeignKey(Product, on_delete=CASCADE ,related_name="product")
    quantity = models.IntegerField()
    price = models.FloatField(default=0)
    total = models.FloatField(default=0)
    def __str__(self):
        return self.product
