from django.urls import path, include
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('products', views.ProductPage.as_view(), name='productpage'),
    path('saveemail', views.insertEmail, name='saveemail'),
]
