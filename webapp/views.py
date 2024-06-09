from django.shortcuts import render

from django.views import View
from .models import Product, Order, Category


class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        context = {"products": products}
        return render(request, "product.html", context)
