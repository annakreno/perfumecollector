from django.db import models
from django.urls import reverse

# Create your models here.
class Perfume(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    description = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'perfume_id': self.id})

# class Review(models.Model):


