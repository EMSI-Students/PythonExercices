from django.db import models
from users.models import User

class Product(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=25)
    description = models.TextField()
    brand = models.CharField(max_length=25)
    date_production = models.DateField()
    image = models.FileField(upload_to='static/products')

    def __str__(self):
        return f"{self.name} ({self.id})"
