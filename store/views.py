from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Product, Cart, Order, OrderItem, Category, Feedback
from .forms import FeedbackForm

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    feedback_form = FeedbackForm()
    return render(request, 'store/home.html', {
        'products': products,
        'categories': categories,
        'feedback_form': feedback_form
    })

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

@login_required
def place_order(request):
    if request.method == "POST":
        cart_items = Cart.objects.filter(user=request.user)
        if not cart_items:
            messages.error(request, "🛒 Your cart is empty!")
            return redirect('view_cart')

        order = Order.objects.create(user=request.user)
        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
        cart_items.delete()
        messages.success(request, "✅ Your order has been placed successfully!")
        return redirect('order_success')
    return redirect('view_cart')

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

def about_view(request):
    return render(request, 'store/about.html')

def contact_view(request):
    return render(request, 'store/contact.html')

def order_success(request):
    return render(request, 'store/order_success.html')

def submit_feedback(request):
    if request.method == 'POST':
        emoji = request.POST.get('emoji')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        Feedback.objects.create(emoji=emoji, email=email, comment=comment)
    return redirect(request.META.get('HTTP_REFERER', '/'))

@staff_member_required
def custom_admin_dashboard(request):
    context = {
        'product_count': Product.objects.count(),
        'order_count': Order.objects.count(),
        'user_count': User.objects.count(),
        'feedback_count': Feedback.objects.count(),
    }
    return render(request, 'admin/custom_dashboard.html', context)