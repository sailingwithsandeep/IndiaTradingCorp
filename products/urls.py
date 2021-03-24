from django.urls import path, include
from . import views
from django.conf.urls import url


app_name = 'products'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('products', views.ProductPage.as_view(), name='productpage'),
    path('about', views.AwardList.as_view(), name='about'),
    path('contact', views.ContactUsView.as_view(), name='contact'),
    path('saveemail', views.insertEmail, name='saveemail'),
    path('saveFeedback', views.saveFeedback, name='saveemail'),

]
