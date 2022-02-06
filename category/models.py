from django.db import models

import product

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def get_products(self):
        return product.models.Product.objects.filter(category__id=self.id)
