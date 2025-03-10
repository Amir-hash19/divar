from django.db import models
from datetime import datetime
   
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    time_added = models.DateTimeField(auto_now_add=True)

   


    


