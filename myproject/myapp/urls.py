from django.urls import path

from .views import MyModelView


urlpatterns = [
    path('', MyModelView.as_view())
]