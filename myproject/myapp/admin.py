from django.contrib import admin

from .models import MyAppModel, CategoriesModel

admin.site.register(MyAppModel)
admin.site.register(CategoriesModel)