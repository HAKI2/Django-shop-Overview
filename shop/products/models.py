from pathlib import Path
from django.db import models
from django.urls import reverse

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('products:products_cat', kwargs={"category": self.category})

class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    image = models.ImageField(upload_to='product/img/products')

    def __str__(self):
        return f'{self.category}, {self.name}, {self.price}'

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={"pr_id": self.pk})