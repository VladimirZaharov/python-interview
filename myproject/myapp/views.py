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
    queryset = CategoriesModel.objects.select_related('cat').prefetch_related('электроника')

class WearView(ListView):
    model = CategoriesModel
    template_name = 'wear.html'
    queryset = CategoriesModel.objects.select_related('cat').prefetch_related('одежда')
