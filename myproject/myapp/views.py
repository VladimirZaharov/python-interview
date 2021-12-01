from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import MyAppModel, CategoriesModel

class MyModelView(ListView):
    model = CategoriesModel
    template_name = 'index.html'
    queryset = CategoriesModel.objects.all()

class ElectronicView(ListView):
    model = CategoriesModel
    template_name = 'electronic.html'
    queryset = CategoriesModel.objects.prefetch_related('product').all()

class WearView(ListView):
    model = CategoriesModel
    template_name = 'wear.html'
    queryset = CategoriesModel.objects.prefetch_related('product').all()
