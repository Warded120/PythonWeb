from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm
from products.models import Product
from django.http import JsonResponse


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.role == 'admin':
                return redirect('home')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.role == 'admin':
                return redirect('home')
            return redirect('home')
        messages.error(request, "Невірний логін або пароль")
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def user_home(request):
    if not request.user.is_authenticated or request.user.role != 'user':
        return redirect('login')
    return render(request, 'accounts/user_home.html')

def admin_home(request):
    if not request.user.is_authenticated or request.user.role != 'admin':
        return redirect('login')
    return render(request, 'accounts/admin_home.html')

def home(request):
    return render(request, 'accounts/index.html')
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        quantity = float(request.POST.get('quantity', 1))

        cart = request.session.get('cart', {})

        if str(product_id) in cart:
            cart[str(product_id)]['quantity'] += quantity
        else:
            cart[str(product_id)] = {
                'name': product.name,
                'price': float(product.price),
                'quantity': quantity,
            }

        request.session['cart'] = cart

        return JsonResponse({
            'message': f"{product.name} додано до кошика!",
            'cart_count': len(cart)
        })
    
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('index')

def checkout_view(request):
    cart = request.session.get('cart', {})
    if request.method == 'POST':
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        if not address or not phone:
            messages.error(request, "Будь ласка, введіть адресу та телефон")
            return redirect('index')  

        request.session['cart'] = {}
        messages.success(request, "Замовлення оформлено! Ми зв’яжемося з вами")
        return redirect('index')  

    return render(request, 'accounts/checkout.html', {'cart': cart})

def update_cart(request, product_id, quantity):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        if quantity <= 0:
            del cart[str(product_id)]
        else:
            cart[str(product_id)]['quantity'] = quantity
        request.session['cart'] = cart
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'products/cart.html', {'cart': cart, 'total': total})
