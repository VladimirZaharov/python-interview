from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import MyAppModel

class MyModelView(ListView):
    model = MyAppModel
    template_name = 'index.html'
    queryset = MyAppModel.objects.all()