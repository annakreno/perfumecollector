from django.db import models

# Create your models here.
class Perfume(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    description = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name

