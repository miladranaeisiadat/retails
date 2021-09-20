import json

from django.test import TestCase, Client
from rest_framework import status

from api.models import Store, Product

# initialize the APIClient app
client = Client()


class StoreTest(TestCase):
    """ Test module for POST single STORE API """

    def setUp(self):
        self.valid_payload = {
            'name': 's1',
            'address': 'moscow',
        }
        self.invalid_payload = {
            'name': 's2',
            'address': 'iran',
            'city': 'mashhad',
        }

    def test_create_valid_store(self):
        response = client.post(
            '/stores/',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_store(self):
        response = client.post(
            '/store/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ProductsTest(TestCase):
    """ Test module for POST single Products API """

    def setUp(self):
        self.valid_payload = {
            'name': 'p1',
            'price': 1000,
        }
        self.invalid_payload = {
            'name': 'p1',
            'address': 'iran',
            'price': -10,
        }

    def test_create_valid_products(self):
        response = client.post(
            '/products/',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_products(self):
        response = client.post(
            '/products/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class AddStoreTest(TestCase):
    """ Test module for add single product with quantity"""

    def setUp(self):
        self.pr = Store.objects.create(
            name='s1')
        self.pr = Product.objects.create(
            name='p1', price=1000)
        self.valid_payload = {
            'product_id': self.pr.pk,
            'count': 10,
        }
        self.invalid_payload = {
            'product_id': 20,
            'price': 1000,
            'city': 'mashhad'
        }

    def test_create_valid_add_product(self):
        pr_id = self.valid_payload.get('product_id')
        response = client.post(
            f'/stores/{pr_id}/add/',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invalid_add_product(self):
        pr_id = self.invalid_payload.get('product_id')
        response = client.post(
            f'/stores/{pr_id}/add/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class buyStoreTest(TestCase):
    """ Test module for buy single product with quantity"""

    def setUp(self):
        self.sr = Store.objects.create(
            name='s1')
        self.pr = Product.objects.create(
            name='p1', price=1000)

        self.valid_payload_add = {
            'product_id': self.pr.pk,
            'count': 10,  # required quantity
        }
        pr_id = self.valid_payload_add.get('product_id')
        self.valid_payload = {
            'product_id': self.pr.pk,
            'count': 5,
        }
        self.invalid_payload = {
            'product_id': 20,  # this product not available in stock
            'count': 1000,
        }
        client.post(
            f'/stores/{pr_id}/add/',
            data=json.dumps(self.valid_payload_add),
            content_type='application/json'
        )

    def test_create_valid_buy_product(self):
        pr_id = self.valid_payload.get('product_id')
        response = client.post(
            f'/stores/{pr_id}/buy/',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invalid_buy_product(self):
        pr_id = self.invalid_payload.get('product_id')
        response = client.post(
            f'/stores/{pr_id}/buy/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
