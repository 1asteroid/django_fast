from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="")
    count = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name


class OrderStatus(models.TextChoices):
    PENDING = 'PENDING' 'pending'
    TRANSIT = 'TRANSIT' 'transit'
    DELIVERED = 'DELIVERED' 'delivered'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField(default=1)
    create_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=20, choices=OrderStatus, default=OrderStatus.PENDING)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return f"{self.product.name} {self.count}"


