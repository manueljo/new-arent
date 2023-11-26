from django.db import models
from geoposition.fields import GeopositionField
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100,null=True)
    residential_address = models.CharField(max_length=100,null=True)
    lga = models.CharField(max_length=20, null=True, blank=True)
    passport = models.ImageField(null=True,upload_to='profile_pics',default='default.png')
    mobile_number = models.CharField(null=True,max_length=15)
    nin_number = models.CharField(null=True,max_length=15)
    verified = models.BooleanField(default=False)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'


class Areas(models.Model):
    name = models.CharField(max_length=50)
    location = GeopositionField()
    
    def __str__(self):
        return self.name

APARTMENT_TYPE = [
        ('SELF CONTAIN', 'self_contain'),
        ('SINGLE ROOM', 'single_room'),
        ('TWO ROOMS FLAT', 'two_rooms_flat'),
        ('THREE ROOMS FLAT', 'three_rooms_flat')
    ]
    
class Apartment(models.Model):
    name = models.CharField(max_length=50)
    area = models.ForeignKey(Areas, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    location = GeopositionField()
    apartment_type = models.CharField(max_length=20,choices=APARTMENT_TYPE,default='LEASE',null=True)
    description = models.TextField()
    first_image = models.ImageField(null=True)
    second_image = models.ImageField(null=True)
    third_image = models.ImageField(null=True)
    fourth_image = models.ImageField(null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name