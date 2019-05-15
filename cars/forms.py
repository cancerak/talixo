from django.forms import ModelForm

from cars.models import *


class ManufacturerForm(ModelForm):

    # def __init__(self):
    #     super().__init__()
    #     self.name = None

    def clean(self):
        cleaned_data = self.cleaned_data

        # self.name = cleaned_data.get('name')
        # del cleaned_data['name']
        # print('nejm')
        # print(name)
        return cleaned_data

    class Meta:
        model = Manufacturer
        fields = ['name']


class CarModelForm(ModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data

        category = cleaned_data.get('category')
        engine = cleaned_data.get('engine')
        name = cleaned_data.get('name')
        passengers = cleaned_data.get('passengers')
        manufacturer = cleaned_data.get('manufacturer')
        # manufacturer = ManufacturerForm.cleaned_data.get('name')

        print("tutaj")
        print("manu")
        print(manufacturer)
        cleaned_data['category'] = 'first'
        print(category)

        f = CarModel.objects.filter(
            category=category, engine=engine, name=name, passengers=passengers,  # manufacturer_id=manufacturer.pk
        )
        print(f.count())
        if f.count() > 0:
            print('yee')
            pk = f.first().pk
            # del cleaned_data['category']
            # del cleaned_data['engine']
            # del cleaned_data['name']
            # del cleaned_data['passengers']
            # del cleaned_data['manufacturer']
            # raise forms.ValidationError("Account and is_master combination already exists.")

        print('nope')
        return cleaned_data

    class Meta:
        model = CarModel
        fields = ['category', 'engine', 'name', 'passengers']


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['number_plate', 'year']
