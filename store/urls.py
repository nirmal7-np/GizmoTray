from django.urls import path
from .views import (
    home,
    product_detail,
    add_to_cart,
    view_cart,
    about_view,
    contact_view,
    order_success,
    place_order,
    submit_feedback,  # ✅ import the feedback view
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('order-success/', order_success, name='order_success'),
    path('place-order/', place_order, name='place_order'),
    path('submit-feedback/', submit_feedback, name='submit_feedback'),
]
