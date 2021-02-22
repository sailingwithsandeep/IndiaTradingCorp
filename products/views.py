from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmailForm
from .models import *
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.


class HomePage(TemplateView):

    template_name = "index.html"
    context_object_name = 'slider'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slider'] = Slider.objects.all().order_by('id')
        return context
