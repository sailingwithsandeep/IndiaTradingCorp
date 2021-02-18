from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Category)
class Category_admin(admin.ModelAdmin):
    list_display = ['categoryName', 'categoryImg']


@admin.register(Subcategory)
class Subcategory_admin(admin.ModelAdmin):
    list_display = ['subCategoryName', 'subCategoryImg']


@admin.register(Products)
class Product_admin(admin.ModelAdmin):
    list_display = ['productName', 'productImg']


@admin.register(Slider)
class sliderImage_admin(admin.ModelAdmin):
    list_display = ['Name', 'Description', 'sliderImage', 'sliderImg']


@admin.register(Email_Newsletter)
class Email_Newsletter(admin.ModelAdmin):
    list_display = ['emailAddress', 'date']
