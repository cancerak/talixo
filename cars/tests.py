import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from tastypie.test import ResourceTestCaseMixin
from cars.models import Car

# json = {
#     "car_model": {
#         "category": "economy",
#         "engine": "electric",
#         "manufacturer": {
#             "name": "xMazda"
#         },
#         "name": "Privia+-",
#         "passengers": 0
#     },
#     "number_plate": "KR 001",
#     "year": 2019
# }


# class CarResourceTest(ResourceTestCaseMixin, TestCase):
#
#     fixtures = ['test_cars.json']
#
#     def setUp(self):
#         super(CarResourceTest, self).setUp()
#
#         self.car_1 = Car.objects.get(number_plate='KR 001')
#
#         self.detail_url = '/cars_api/car/{0}/'.format(self.car_1.pk)
#
#         self.manufacturer = {
#             'name': 'manufacturer name'
#         }
#         self.car_model = {
#             'category': 'economy',
#             'engine': 'electric',
#             'manufacturer': self.manufacturer,
#             'name': 'model name',
#             'passengers': 5
#         }
#         self.post_data = {
#             'car_model': self.car_model,
#             'number_plate': 'KR 001',
#             'year': 2017
#         }
#
#     def test_get_list_json(self):
#         resp = self.api_client.get('/cars_api/car/', format='json')
#         self.assertValidJSONResponse(resp)
