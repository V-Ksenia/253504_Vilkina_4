import re
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ValidationError


class User(AbstractUser):
    STATUS_CHOICES = (
        ("staff", "staff"),
        ("client", "client"),
    )
    status = models.CharField(choices=STATUS_CHOICES, default="client", max_length=6)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name
    
    def save(self, *args, **kwargs):
        phone_pattern = re.compile(r'\+375(25|29|33)\d{7}')
        if not re.fullmatch(phone_pattern, str(self.phone_number)):
            raise ValidationError("This field accepts mail id of google only")
        super().save(*args, **kwargs)
    

class Climate(models.Model):
    CLIMATE_CHOICES = (
        ("TR", "tropical"),
        ("AL", "Alpine"),
        ("OC", "Oceanic"),
        ("CN", "Continental"),
    ) 
    climate = models.CharField(choices=CLIMATE_CHOICES, default="Continental", max_length=13)
    country = models.ManyToManyField('Country', related_name='climates')
    
    def __str__(self):
        return self.climate

class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    STAR_CHOICES = (
        (1, "Terrible"),
        (2, "Poor"),
        (3, "Average"),
        (4, "Very Good"),
        (5, "Excellent"),
    )
    stars = models.CharField(choices=STAR_CHOICES, default="Average", max_length=255)
    price_per_night = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Tour(models.Model):
    name = models.CharField(max_length=255)
    DURATION_CHOICES = {
        1: "One week",
        2: "Two weeks",
        4: "Four weeks",
    }
    duration = models.IntegerField(choices=DURATION_CHOICES)

    departure_date = models.DateField()

    hotel = models.ForeignKey(Hotel, related_name="tours", on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name="tours", on_delete=models.CASCADE)

    price = models.PositiveIntegerField()

    # def get_price(self):
    #     self.price = self.hotel.price_per_night * int(self.duration * 7)
    #     return self.price
    # @property
    # def price(self):
    #     return self.hotel.price_per_night * int(self.duration)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.AutoField(primary_key=True)
    tour = models.ForeignKey(Tour, related_name='tours', on_delete=models.CASCADE)