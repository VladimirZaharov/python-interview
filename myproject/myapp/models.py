from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager

# Create your models here.
class MyAppModel(models.Model):
    name = models.CharField(max_length=64, default='Unknown')
    recieve_date = models.DateField(auto_now_add=True)
    price = models.IntegerField(default=0)
    unit = models.CharField(max_length=15)
    producer = models.CharField(max_length=64)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    objects = CurrentSiteManager('site')

    def __str__(self):
        return self.name


class CategoriesModel(models.Model):
    category = models.CharField(max_length=64, default='Unknown')
    product = models.ManyToManyField(MyAppModel, related_name='product')
    objects = models.Manager()

    def __str__(self):
        return self.category
