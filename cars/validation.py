from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.validation import FormValidation

from cars.forms import CarModelForm


class CarModelValidation(FormValidation):
    def is_valid(self, bundle, request=None):
        if not bundle.data:
            return {'__all__': 'No data provided.'}
        errors = {}
        if bundle.request
        if bundle.data.get('title', '') == '':
            errors['title'] = 'Title cannot be empty'
        if bundle.data.get('content', '') == '':
            errors['content'] = 'Content cannot be empty'
        return errors

    manufacturer = fields.ForeignKey(ManufacturerResource, 'manufacturer', full=True)

    class Meta:
        validation = FormValidation(form_class=CarModelForm)