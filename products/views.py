from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Review
from django.http import JsonResponse

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        if request.user.is_authenticated:
            text = request.POST.get('text')
            rating = request.POST.get('rating', 5)
            Review.objects.create(product=product, user=request.user, text=text, rating=rating)
            return redirect('product_detail', pk=pk)
    return render(request, 'products/detail.html', {'product': product})