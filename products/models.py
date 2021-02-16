from django.db import models
from django.utils.timezone import now
from django.utils.html import format_html

# Create your models here.


class Category(models.Model):
    categoryName = models.CharField(max_length=256, unique=True)
    categoryImage = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.categoryName

    def categoryImg(self):
        return format_html('<img href="{0}" src="{0}" width="150" height="150" />'.format(self.categoryImage.url))

    categoryImg.allow_tags = True
    categoryImg.short_description = 'Image'


class Subcategory(models.Model):
    subCategoryName = models.CharField(max_length=256, unique=True)
    subCategoryImage = models.ImageField(upload_to='subcategory/')

    def __str__(self):
        return self.subCategoryName

    def subCategoryImg(self):
        return format_html('<img href="{0}" src="{0}" width="150" height="150" />'.format(self.subCategoryImage.url))

    subCategoryImg.allow_tags = True
    subCategoryImg.short_description = 'Image'


class Products(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, to_field='categoryName')
    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE, to_field='subCategoryName')
    productName = models.CharField(max_length=256, unique=True)
    productImage = models.ImageField(upload_to='products/')

    def productImg(self):
        return format_html('<img href="{0}" src="{0}" width="150" height="150" />'.format(self.productImage.url))

    productImg.allow_tags = True
    productImg.short_description = 'Image'

    def __str__(self):
        return self.productName


class Slider(models.Model):
    pass
    # 3 image dynamic slider on homepage page


class Email_Newsletter(models.Model):
    emailAddress = models.EmailField(max_length=256, unique=True)
    date = models.DateTimeField(default=now, editable=False)
