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
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.first_name
    

class Climate(models.Model):
    climate = models.CharField(max_length=255)
    
    def __str__(self):
        return self.climate

class Country(models.Model):
    name = models.CharField(max_length=255)
    climate = models.ManyToManyField(Climate, related_name='countries')

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
    country = models.ForeignKey(Country, related_name="hotels", on_delete=models.CASCADE)

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
    trips = models.PositiveSmallIntegerField()

    hotel = models.ForeignKey(Hotel, related_name="tours", on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name="tours", on_delete=models.CASCADE)

    price = models.PositiveIntegerField()

    def get_price(self):
        self.price = self.hotel.price_per_night * int(self.duration * 7)
        self.save()
        return self.price
    
    def __str__(self):
        return self.name
    

class Order(models.Model): 
    number = models.AutoField(primary_key=True)    
    amount = models.PositiveSmallIntegerField(default=1)
    price = models.FloatField()
    departure_date = models.DateField()

    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, related_name='tours', on_delete=models.CASCADE)

    def use_discount(self, promocode):
        if UsedDiscounts.objects.filter(promocode_id=promocode, user_id=self.user).exists():
            return
        self.price *= (100 - promocode.discount) / 100
        self.save()

        UsedDiscounts.objects.create(promocode=promocode, user=self.user)


class Promocode(models.Model):
    code = models.CharField(max_length=10)
    discount = models.PositiveSmallIntegerField()


class UsedDiscounts(models.Model):
    promocode = models.ForeignKey(Promocode, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)




#ADDITIONAL PAGES

class Article(models.Model):
    title = models.TextField(max_length=120)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class CompanyInfo(models.Model):
    text = models.TextField()
    logo = models.ImageField(upload_to='images/')


class News(models.Model):
    title = models.TextField(max_length=120)
    content = models.TextField()
    #image = models.ImageField(upload_to='images/')

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    date = models.DateField(auto_now_add=True)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    #photo = models.ImageField(upload_to='images/')
    phone = models.CharField(max_length=15)
    email = models.EmailField()


class Vacancy(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()


class Review(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    text = models.TextField()
    date = models.DateField(auto_now_add=True)