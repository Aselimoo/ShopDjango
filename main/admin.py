from django.contrib import admin
from .models import Product, Category, Profile
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'description', 'created_at']
    list_filter = ['category']
    search_fields = ['title', 'description']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['title']
    search_fields = ['title']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'birth_data', 'phone']
    list_filter = ['user']
    search_fields = ['user']
