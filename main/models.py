from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    pass
    
PROVINCES = (
    ("Constantine", "قسنطينة"),
    ("El Khroub", "الخروب"),
    ("Ain Smara", "عين سمارة"),
    ("Ouled Rahmoun", "أولاد رحمون"),
    ("Ain Abid", "عين عبيد"),
    ("Ibn Badis", "ابن باديس"),
    ("Zighoud Youcef", "زيغود يوسف"),
    ("Beni Hamidane", "بني حميدان"),
    ("Hamma Bouziane", "حامة بوزيان"),
    ("Didouche Mourad", "ديدوش مراد"),
    ("Ibn Ziad", "ابن زياد"),
    ("Messaoud Boudjeriou", "مسعود بوجريو")
)

CUISINES = (
    ("continental", "Continental"),
    ("asiatique", "Asiatique"),
    ("arabe", "Arabe"),
    ("algérienne traditionnelle", "Algérienne traditionnelle"),
)


class Restaurant(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(default="")
    rating = models.IntegerField(default=1)
    address = models.CharField(max_length=64, default="unknown")
    cuisine = models.CharField(
                max_length = 30,
                choices = CUISINES,
                default = 'Continental'
            )
    phone = models.CharField(max_length=16, default="+xxx-xxx-xxx-xxx")
    email = models.CharField(max_length=64, default="noreply@example.com")
    province = models.CharField(
                max_length = 30,
                choices = PROVINCES,
                default = 'Constantine'
            )
    wifi = models.BooleanField(default=False)
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
    
    
    
class Plate(models.Model):
    name = models.CharField(max_length=64, default="")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price = models.IntegerField(default=100)
    image = models.ImageField(upload_to="main/static/img/plates/", default=None)
    
    def __str__(self):
        return self.name
        
class Comment(models.Model):
    content = models.CharField(max_length=128, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username