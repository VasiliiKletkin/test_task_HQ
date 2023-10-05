from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Product(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_products')
    users = models.ManyToManyField(User, related_name='bought_products', blank=True)
    
    def __str__(self):
        return self.title