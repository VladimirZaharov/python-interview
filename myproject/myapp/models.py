from django.db import models

# Create your models here.
class MyAppModel(models.Model):
    name = models.CharField(max_length=64, default='Unknown')
    recieve_date = models.DateField(auto_now_add=True)
    price = models.IntegerField(default=0)
    unit = models.CharField(max_length=15)
    producer = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class CategoriesModel(models.Model):
    category = models.CharField(max_length=64, default='Unknown')
    product = models.ManyToManyField(MyAppModel, related_name='cat')
    some_model = models.CharField(max_length=64, default='Unknown')

    def __str__(self):
        return self.category
