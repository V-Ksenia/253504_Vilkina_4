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
    climate = models.CharField(max_length=255)
    
    def __str__(self):
        return self.climate

class Country(models.Model):
    name = models.CharField(max_length=255)
    climate = models.ManyToManyField('Climate', related_name='countries')

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





#ADDITIONAL PAGES

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    published_date = models.DateTimeField(auto_now_add=True)


class CompanyInfo(models.Model):
    text = models.TextField()


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    published_date = models.DateTimeField(auto_now_add=True)

class Term(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    date_added = models.DateField(auto_now_add=True)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    #photo = models.ImageField(upload_to='images/')
    phone = models.CharField(max_length=20)
    email = models.EmailField()


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Review(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    text = models.TextField()
    date = models.DateField(auto_now_add=True)