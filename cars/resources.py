from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.validation import FormValidation, Validation

from cars.forms import *
from cars.models import *
from cars.validation import CarModelValidation


class ManufacturerResource(ModelResource):
    class Meta:
        queryset = Manufacturer.objects.all()
        authorization = Authorization()
        # validation = Validation()
        validation = FormValidation(form_class=ManufacturerForm)
        fields = ['name']
        # validation.is_valid()


class CarModelResource(ModelResource):
    manufacturer = fields.ForeignKey(ManufacturerResource, 'manufacturer', full=True)

    class Meta:
        queryset = CarModel.objects.all()
        authorization = Authorization()
        # validation = FormValidation(form_class=CarModelForm)
        # validation = CarModelValidation(form_class=CarModelForm)
        validation = CarModelValidation()
        fields = ['category', 'engine', 'name', 'passengers', 'manufacturer']


class CarResource(ModelResource):
    car_model = fields.ForeignKey(CarModelResource, 'car_model', full=True)

    class Meta:
        queryset = Car.objects.all()
        authorization = Authorization()
        fields = ['car_model', 'number_plate', 'year']
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'put', 'delete']
        validation = FormValidation(form_class=CarForm)
