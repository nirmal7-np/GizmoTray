from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin

from .models import Product, Cart, Feedback, Order, OrderItem, Category
from .custom_admin_site import custom_admin_site

# Register User and Group ONLY with custom_admin_site
custom_admin_site.register(User, UserAdmin)
custom_admin_site.register(Group, GroupAdmin)

@admin.register(Product, site=custom_admin_site)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')

@admin.register(Cart, site=custom_admin_site)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')

@admin.register(Feedback, site=custom_admin_site)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('emoji', 'email', 'submitted_at')
    list_filter = ('emoji', 'submitted_at')
    search_fields = ('email', 'comment')


@admin.register(Order, site=custom_admin_site)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username',)

