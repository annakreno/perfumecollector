from django.db import models
from django.urls import reverse
from django.utils.timezone import now


RATINGS = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))

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

class Review(models.Model):
    date = models.DateField(
        default=now()
    )
    content = models.TextField(max_length=1000)
    rating = models.IntegerField(choices=RATINGS, default=RATINGS[4])
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE)



