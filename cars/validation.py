from tastypie.validation import Validation


class ManufacturerValidation(Validation):
    def is_valid(self, bundle, request=None):
        if not bundle.data:
            return {'__all__': 'No data provided.'}

        errors = {}

        unique = False
        # for key, value in bundle.data.items():
        #
        #     if value == :
        #         errors[key] = ['NOT ENOUGH AWESOME. NEEDS MORE.']
        bundle.data.items()

        return errors