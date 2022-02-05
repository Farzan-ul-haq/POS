from django.db import models

from category.models import Category

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        null=True
    )
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title
