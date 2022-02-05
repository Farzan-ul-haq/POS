from django.db import models

# Create your models here.

class Order(models.Model):
    timestamp = models.DateTimeField()
    products = models.JSONField()

    def __str__(self):
        return f"{self.id} | {self.timestamp}"