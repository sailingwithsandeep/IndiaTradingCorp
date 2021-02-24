from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmailForm
from .models import *
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib import messages
from django import forms
import os
# Create your views here.


class HomePage(TemplateView):

    template_name = "index.html"
    context_object_name = 'slider'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slider'] = Slider.objects.all().order_by('id')
        return context

class ProductPage(TemplateView):

    template_name = "product.html"
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Products.objects.all().order_by('id')
        return context

def insertEmail(request):
    str_email = request.POST.get('email')
    try:
        validate_email(str_email)
        if request.method == 'POST':
            if str_email:
                email  = Email_Newsletter.objects.get(emailAddress = str_email)
                if email:
                    messages.error(request, "Email already exists!")  
                # return to previous page
                next = request.POST.get('next', '/')
                return HttpResponseRedirect(next)    # if email already exists
    except Email_Newsletter.DoesNotExist:
        email=Email_Newsletter(emailAddress = str_email)
        # print(request.POST.get('email'))
        email.save()       
        # return to previous page
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
    # if invalid email
    except ValidationError as e:
        messages.error(request, "Invalid email address!")
        # return to previous page
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
    
        
    