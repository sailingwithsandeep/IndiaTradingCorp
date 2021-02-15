from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmailForm
from .models import *
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.


class HomePage(TemplateView):
    pass
   # template_name = "index.html"
