from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.validation import FormValidation

from cars.forms import *
from cars.models import *


class ManufacturerResource(ModelResource):
    class Meta:
        queryset = Manufacturer.objects.all()
        authorization = Authorization()
        fields = ['name']
        validation = FormValidation(form_class=ManufacturerForm)
        # validation.is_valid()


class CarModelResource(ModelResource):
    manufacturer = fields.ForeignKey(ManufacturerResource, 'manufacturer', full=True)

    class Meta:
        queryset = CarModel.objects.all()
        authorization = Authorization()
        fields = ['category', 'engine', 'name', 'passengers', 'manufacturer']
        validation = FormValidation(form_class=CarModelForm)


class CarResource(ModelResource):
    car_model = fields.ForeignKey(CarModelResource, 'car_model', full=True)

    class Meta:
        queryset = Car.objects.all()
        authorization = Authorization()
        fields = ['car_model', 'number_plate', 'year']
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'put', 'delete']
        validation = FormValidation(form_class=CarForm)
