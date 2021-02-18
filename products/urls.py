from django.urls import path, include
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
]
