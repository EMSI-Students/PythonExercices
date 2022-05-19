from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=25)
    brand = models.CharField(max_length=25)
    year = models.IntegerField()
