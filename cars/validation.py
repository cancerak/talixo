from tastypie.validation import Validation

from cars.models import CarModel, Manufacturer


class CarModelValidation(Validation):
    def is_valid(self, bundle, request=None):
        if not bundle.data:
            return {'__all__': 'No data provided.'}

        errors = {}

        unique = False
        # for key, value in bundle.data.items():
        #
        #     if value == :
        #         errors[key] = ['NOT ENOUGH AWESOME. NEEDS MORE.']
        items = bundle.data

        category = items.get('category')
        engine = items.get('engine')
        name = items.get('name')
        passengers = items.get('passengers')
        print(category)
        print(engine)

        duplicate = CarModel.objects.filter(category=category, engine=engine, name=name, passengers=passengers).first()
        if duplicate:
            print("duplicate: ")
            print(duplicate)
        else:
            print("no duplicate")

        # return errors
