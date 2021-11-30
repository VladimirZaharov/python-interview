from django.urls import path

from .views import MyModelView, ElectronicView, WearView

app_name= 'myapp'

urlpatterns = [
    path('', MyModelView.as_view(), name='index'),
    path('', ElectronicView.as_view(), name='electronic'),
    path('', WearView.as_view(), name='wear')
]