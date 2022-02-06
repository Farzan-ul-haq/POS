from django.db import models

# Create your models here.

class Order(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    products = models.CharField(max_length=5000)

    def __str__(self):
        return f"{self.id} | {self.timestamp}"