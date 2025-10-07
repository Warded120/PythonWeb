from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.http import JsonResponse

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

