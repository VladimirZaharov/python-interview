from django.urls import path

from .views import MyModelView, ElectronicView, WearView

app_name= 'myapp'

urlpatterns = [
    path('', MyModelView.as_view(), name='index'),
    path('electronic/', ElectronicView.as_view(), name='electronic'),
    path('wear/', WearView.as_view(), name='wear')
]