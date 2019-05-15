from django.urls import path, include
from tastypie.api import Api

from cars.resources import *


cars_api = Api(api_name='cars_api')
cars_api.register(CarResource())

urlpatterns = [
    path('', include(cars_api.urls)),
]

# less flexible alternative
# car_resource = CarResource()
#
# urlpatterns = [
#      path('', include(car_resource.urls)),
# ]
