from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from products.models import Product

class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)