from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    pass
    
    
class Image(models.Model):
    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to='main/static/img/restaurants/')
    def __str__(self):
        return self.title

class Restaurant(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    rating = models.IntegerField(default=1)
    address = models.CharField(max_length=64)
    cuisine = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=64)
    images = models.ManyToManyField(Image, related_name='images')
    def __str__(self):
        return self.name
        
        
        
class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    gr_code = models.ImageField(upload_to="main/static/img/bookings/", default=None)
    class Meta:
        verbose_name_plural = 'Bookings'
    
    
# class RestaurantStaff(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)

    # def __str__(self):
        # return self.user.username

# class Client(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    # def __str__(self):
        # return self.user.username
    
    
# class Plates(models.Model):
    # name = models.CharField(max_length=100)
    # cuisine = models.CharField(max_length=64)
    # description = models.TextField()
    # price = models.DecimalField(max_digits=8, decimal_places=2)
    # image = models.ImageField(upload_to='main/static/img/plates/')
    # restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    # class Meta:
        # verbose_name_plural = 'Plates'