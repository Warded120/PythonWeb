# products/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Review
from .forms import ReviewForm

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()
    return render(request, 'products/detail.html', {'product': product, 'reviews': reviews})

@login_required
def add_review(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        text = request.POST.get('text')
        rating = request.POST.get('rating')
        Review.objects.create(product=product, user=request.user, text=text, rating=rating)
        return redirect('product_list')

    
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
