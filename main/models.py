from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    pass

class Restaurant(models.Model):
    name = models.CharField(max_length=64)
    rating = models.IntegerField(default=1)
    address = models.CharField(max_length=64)
    cuisine = models.CharField(max_length=64)
    image = models.ImageField(upload_to='static/img')
    
    def __str__(self):
        return self.name
        
        
        
class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Bookings'
    