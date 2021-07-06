from WEBSITE.models import Cart
from django.contrib import admin
from .models import Category
from .models import Product
from .models import Cart

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)