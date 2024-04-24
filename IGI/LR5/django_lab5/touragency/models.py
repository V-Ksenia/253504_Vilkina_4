from django.db import models

class User(models.Model):
    pass


class Climate(models.Model):
    CLIMATE_CHOICES = (
        ("TR", "tropical"),
        ("AL", "Alpine"),
        ("OC", "Oceanic"),
        ("CN", "Continental"),
    ) 
    climate = models.CharField(choices=CLIMATE_CHOICES, default="Continental", max_length=255)
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
    DURATION_CHOICES = (
        (1, "One week"),
        (2, "Two weeks"),
        (4, "Four weeks"),
    )
    duration = models.CharField(choices=DURATION_CHOICES, max_length=255)

    departure_date = models.DateField()

    hotel = models.ForeignKey(Hotel, related_name="tours", on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name="tours", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.AutoField(primary_key=True)
    tour = models.ForeignKey(Tour, related_name='tours', on_delete=models.CASCADE)