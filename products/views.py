from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmailForm, ContactForm
from .models import *
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib import messages
from django import forms
from django.contrib import messages
import os
# Create your views here.


class HomePage(TemplateView):

    template_name = "index.html"
    context_object_name = 'slider', 'categories', 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slider'] = Slider.objects.all().order_by('id')
        context['categories'] = Category.objects.all().order_by('id')
        context['products'] = Products.objects.all().order_by('id')

        return context


class ProductPage(ListView):
    model = Products
    template_name = "products/product.html"
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductPage, self).get_context_data(**kwargs)
        context['products'] = Products.objects.all().order_by('id')
        context['categories'] = Category.objects.all().order_by('id')
        return context


class AwardList(ListView):
    model = Awards
    template_name = "products/about.html"
    context_object_name = 'award'

    def get_context_data(self, *args, **kwargs):
        context = super(AwardList, self).get_context_data(**kwargs)
        context['award'] = Awards.objects.all().order_by('id')
        return context


class ContactUsView(CreateView):
    model = ContactUs
    template_name = "products/contact.html"
    form_class = ContactForm
    success_url = "/contact"

    def get_success_url(self, *args):
        messages.success(
            self.request, ("Thanks for contacting with us!"))

def saveFeedback(request):
    str_name = request.POST.get('name')
    str_email = request.POST.get('email')
    str_message = request.POST.get('message')
    try:
        validate_email(str_email)

        if request.method == 'POST':
            print("post")
            if str_email and str_name and str_message:
                print('all feild')
                feedback = ContactUs(name=str_name,contactEmail=str_email,message=str_message)
                feedback.save()
                messages.error(request, "Thanks for contacting with us!")

                # return to previous page
                next = request.POST.get('next', '/')
                return HttpResponseRedirect(next)   
            else:
                print("missing")   
                messages.error(request, "Please enter all feilds!")

                 # return to previous page
                next = request.POST.get('next', '/')
                return HttpResponseRedirect(next)
    # if invalid email
    except ValidationError as e:
        messages.error(request, "Invalid email address!")
        # return to previous page
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

def insertEmail(request):
    str_email = request.POST.get('email')
    try:
        validate_email(str_email)
        if request.method == 'POST':
            if str_email:
                email = Email_Newsletter.objects.get(emailAddress=str_email)
                if email:
                    messages.error(request, "Email already exists!")
                # return to previous page
                next = request.POST.get('next', '/')
                return HttpResponseRedirect(next)    # if email already exists
    except Email_Newsletter.DoesNotExist:
        email = Email_Newsletter(emailAddress=str_email)
        # print(request.POST.get('email'))
        email.save()
        messages.error(request, "Email Address saved!")
        # return to previous page
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
    # if invalid email
    except ValidationError as e:
        messages.error(request, "Invalid email address!")
        # return to previous page
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

    
def errorPage(request, *args, **kwargs):
    return render(request, '404.html', status=404)
