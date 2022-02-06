import json
from django.db import models

# Create your models here.

class Order(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    products = models.CharField(max_length=5000)

    def __str__(self):
        return f"{self.id} | {self.timestamp}"

    def order_detail(self):
        order_data = json.loads(self.products)
        order_data.pop('total_price')
        return order_data
    
    def total_price(self):
        order_data = json.loads(self.products)
        return order_data.pop('total_price')