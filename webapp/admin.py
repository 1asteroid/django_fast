from django.contrib import admin
from .models import Product, Category, Order


admin.site.register([Category, Product, Order])
