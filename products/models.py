from django.db import models

# Create your models here.


class Category(models.Model):
    categoryName = models.CharField(max_length=256, unique=True)
    categoryImage = models.ImageField(upload_to='images/category')

    def __str__(self):
        return self.categoryName


class Subcategory(models.Model):
    subCategoryName = models.CharField(max_length=256, unique=True)
    subCategoryImage = models.ImageField(upload_to='images/subcategory')

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, to_field='categoryName')
    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE, to_field='subCategoryName')
    productName = models.CharField(max_length=256, unique=True)
    productImage = models.ImageField(upload_to='images/products')

    def __str__(self):
        return self.productName


class Slider(models.Model):
    pass
    # 3 image dynamic slider on homepage page


class Email_Newsletter(models.Model):
    emailAddress = models.EmailField(max_length=256,)
