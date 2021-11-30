# Generated by Django 3.2.9 on 2021-11-30 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_myappmodel_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='Unknown', max_length=64)),
                ('unit', models.ManyToManyField(related_name='cat', to='myapp.MyAppModel')),
            ],
        ),
    ]
