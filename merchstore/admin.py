from django.contrib import admin
from .models import ProductType, Product


class ProductInline(admin.TabularInline):
    model = Product


class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    inlines = [ProductInline,]


class ProductAdmin(admin.ModelAdmin):
    model = Product
