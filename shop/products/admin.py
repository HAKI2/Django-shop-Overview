from django.contrib import admin
from .models import Category, Product


class OrderProduct(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'image']
    list_filter = ['category']


admin.site.register(Product, OrderProduct)
admin.site.register(Category)