from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    pass
    
PRICE_RANGE = (
                ("low", "إقتصادي"),
                ("medium", "متوسط"),
                ("high", "مرتفع")
)
    
class Restaurant(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(default="")
    rating = models.IntegerField(default=1)
    address = models.CharField(max_length=64, default="unknown")
    cuisine = models.CharField(max_length=64, default="unknown")
    phone = models.CharField(max_length=16, default="+xxx-xxx-xxx-xxx")
    email = models.CharField(max_length=64, default="noreply@example.com")
    map = models.ImageField(upload_to='main/static/img/restaurants/maps/', default=None)
    price = models.CharField(
                max_length = 20,
                choices = PRICE_RANGE,
                default = 'medium'
            )
    wifi = models.BooleanField(default=False)
    delivary = models.BooleanField(default=False)
    outdoor = models.BooleanField(default=False)
    kids = models.BooleanField(default=False)
    discounts = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    music = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
        
    
class Image(models.Model):
    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to='main/static/img/restaurants/')
    restaurant = models.ForeignKey(Restaurant, default=None,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

        
class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, default="UNKNOWN")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    gr_code = models.ImageField(upload_to="main/static/img/bookings/", default=None)
    date = models.CharField(max_length=64, default="UNKNOWN")
    
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