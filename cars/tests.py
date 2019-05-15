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
#
#         # Scope out the data for correctness.
#         self.assertEqual(len(self.deserialize(resp)['objects']), 2)
#         # # Here, we're checking an entire structure for the expected data.
#         # self.assertEqual(self.deserialize(resp)['objects'][0], {
#         #     'pk': str(self.car_1.pk),
#         #     'title': 'First post',
#         #     'slug': 'first-post',
#         #     'created': '2012-05-01T19:13:42',
#         #     'resource_uri': '/api/v1/entry/{0}/'.format(self.car_1.pk)
#         # })

    # def test_get_detail_json(self):
    #     resp = self.api_client.get(self.detail_url, format='json')
    #     self.assertValidJSONResponse(resp)
    #
    #     # We use ``assertKeys`` here to just verify the keys, not all the data.
    #     self.assertKeys(self.deserialize(resp), ['created', 'slug', 'title', 'user'])
    #     self.assertEqual(self.deserialize(resp)['name'], 'First post')
    #
    # def test_post_list(self):
    #     # Check how many are there first.
    #     self.assertEqual(Car.objects.count(), 5)
    #     self.assertHttpCreated(self.api_client.post('/api/v1/entries/', format='json', data=self.post_data))
    #     # Verify a new one has been added.
    #     self.assertEqual(Car.objects.count(), 6)
    #
    # def test_put_detail(self):
    #     # Grab the current data & modify it slightly.
    #     original_data = self.deserialize(self.api_client.get(self.detail_url, format='json'))
    #     new_data = original_data.copy()
    #     new_data['title'] = 'Updated: First Post'
    #     new_data['created'] = '2012-05-01T20:06:12'
    #
    #     self.assertEqual(Car.objects.count(), 5)
    #     self.assertHttpAccepted(self.api_client.put(self.detail_url, format='json', data=new_data))
    #     # Make sure the count hasn't changed & we did an update.
    #     self.assertEqual(Car.objects.count(), 5)
    #     # Check for updated data.
    #     self.assertEqual(Car.objects.get(pk=25).title, 'Updated: First Post')
    #     self.assertEqual(Car.objects.get(pk=25).slug, 'first-post')
    #     self.assertEqual(Car.objects.get(pk=25).created, datetime.datetime(2012, 3, 1, 13, 6, 12))
    #
    # def test_delete_detail(self):
    #     self.assertEqual(Car.objects.count(), 5)
    #     self.assertHttpAccepted(self.api_client.delete(self.detail_url, format='json'))
    #     self.assertEqual(Car.objects.count(), 4)
