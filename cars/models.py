from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    CATEGORIES = (
        ('economy', 'Economy class'),
        ('business', 'Business class'),
        ('first', 'First class'),
    )  # assumption: categories won't be changed, no separate db table needed
    ENGINES = (
        ('normal', 'Combustion engine'),
        ('hybrid', 'Hybrid engine'),
        ('electric', 'Electric engine'),
    )
    category = models.CharField(max_length=8, choices=CATEGORIES)
    engine = models.CharField(max_length=8, choices=ENGINES)
    name = models.CharField(max_length=100)
    passengers = models.PositiveIntegerField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.manufacturer) + ' ' + self.name


class Car(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    number_plate = models.CharField(max_length=10, unique=True)
    year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year)])

    def __str__(self):
        return str(self.car_model) + ', number plate: ' + self.number_plate
