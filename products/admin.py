from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Products)
class Product_admin(admin.ModelAdmin):
    pass


@admin.register(Category)
class Category_admin(admin.ModelAdmin):
    pass


@admin.register(Subcategory)
class Subcategory_admin(admin.ModelAdmin):
    pass
