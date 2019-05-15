from django.contrib import admin

# Register your models here.
from cars.models import *


admin.site.register(Manufacturer)
admin.site.register(CarModel)
admin.site.register(Car)
