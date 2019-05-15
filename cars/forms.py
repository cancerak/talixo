from django.forms import ModelForm

from cars.models import *


class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name']


class CarModelForm(ModelForm):
    class Meta:
        model = CarModel
        fields = ['category', 'engine', 'name', 'passengers']


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['number_plate', 'year']
