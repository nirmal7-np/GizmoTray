from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('home')

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'store/cart.html', {'cart_items': cart_items})

def place_order(request):
    if request.method == "POST":
        Cart.objects.filter(user=request.user).delete()
        messages.success(request, "✅ Your order has been placed successfully!")
        return redirect('order_success')
    return redirect('view_cart')

# 🔧 Add this function to fix the NoReverseMatch issue
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

def about_view(request):
    return render(request, 'store/about.html')

def contact_view(request):
    return render(request, 'store/contact.html')

def order_success(request):
    return render(request, 'store/order_success.html')

def place_order(request):
    # ... your order logic
    messages.success(request, "Your order was placed successfully!")
    return redirect('order_success')


