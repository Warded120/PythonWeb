from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user_home/', views.user_home, name='user_home'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:product_id>/<int:quantity>/', views.update_cart, name='update_cart'),
     path('checkout/', views.checkout_view, name='checkout'),
]
