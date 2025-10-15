# products/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Review
from .forms import ReviewForm

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ReviewForm()

    return render(request, 'products/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form
    })
@login_required
def add_review(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        text = request.POST.get('text')
        rating = request.POST.get('rating')
        Review.objects.create(product=product, user=request.user, text=text, rating=rating)
        return redirect('product_detail', pk=product.pk)
    return render(request, 'products/add_review.html', {'product': product})
    
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
