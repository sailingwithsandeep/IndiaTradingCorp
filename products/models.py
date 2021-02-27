from django.db import models
from django.utils.timezone import now
from django.utils.html import format_html

# Create your models here.


class Category(models.Model):
    categoryName = models.CharField(max_length=256, unique=True)
    categoryDescription = models.TextField(
        max_length=256, blank=True, null=True)
    categoryImage = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.categoryName

    def categoryImg(self):
        return format_html('<img href="{0}" src="{0}" width="150" height="150" />'.format(self.categoryImage.url))

    categoryImg.allow_tags = True
    categoryImg.short_description = 'Image'

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Subcategory(models.Model):
    subCategoryName = models.CharField(max_length=256, unique=True)
    subCategoryImage = models.ImageField(upload_to='subcategory/')

    def __str__(self):
        return self.subCategoryName

    def subCategoryImg(self):
        return format_html('<img href="{0}" src="{0}" width="150" height="150" />'.format(self.subCategoryImage.url))

    subCategoryImg.allow_tags = True
    subCategoryImg.short_description = 'Image'

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"


class Products(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, to_field='categoryName')
    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE, to_field='subCategoryName', null=True, blank=True)
    productName = models.CharField(max_length=256, unique=True)
    productDescription = models.CharField(max_length=256, null=True)
    productImage = models.ImageField(upload_to='products/')

    def productImg(self):
        return format_html('<img href="{0}" src="{0}" width="150" height="150" />'.format(self.productImage.url))

    productImg.allow_tags = True
    productImg.short_description = 'Image'

    def __str__(self):
        return self.productName

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Slider(models.Model):
    Name = models.CharField(max_length=255, blank=True)
    Description = models.CharField(max_length=255, blank=True)
    sliderImage = models.ImageField(upload_to='slider/', unique=True)

    def sliderImg(self):
        return format_html('<img href="{0}" src="{0}" width="150" height="150" />'.format(self.sliderImage.url))

    sliderImg.allow_tags = True
    sliderImg.short_description = 'Image'
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Slider"


class Email_Newsletter(models.Model):
    emailAddress = models.EmailField(max_length=256, unique=True)
    date = models.DateTimeField(default=now, editable=False)
    def __str__(self):
        return self.emailAddress
    class Meta:
        verbose_name = "Email_Newsletter"
        verbose_name_plural = "Email_Newsletter"
