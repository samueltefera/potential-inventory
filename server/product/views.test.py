from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from product.models import Product
from product.serializers import ProductSerializer


# initialize the APIClient app
client = APIClient()


class GetAllProductsTest(APITestCase):
    """ Test module for GET all products API """

    def setUp(self):
        self.product1 = Product.objects.create(name='Product 1', price=10.00, description='Product 1 description')
        self.product2 = Product.objects.create(name='Product 2', price=20.00, description='Product 2 description')
        self.product3 = Product.objects.create(name='Product 3', price=30.00, description='Product 3 description')

    def test_get_all_products(self):
        # get API response
        response = client.get(reverse('product-list'))
        # get data from db
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleProductTest(APITestCase):
    """ Test module for GET single product API """

    def setUp(self):
        self.product1 = Product.objects.create(name='Product 1', price=10.00, description='Product 1 description')
        self.product2 = Product.objects.create(name='Product 2', price=20.00, description='Product 2 description')
        self.product3 = Product.objects.create(name='Product 3', price=30.00, description='Product 3 description')

    def test_get_valid_single_product(self):
        response = client.get(reverse('product-detail', kwargs={'pk': self.product2.pk}))
        product = Product.objects.get(pk=self.product2.pk)
        serializer = ProductSerializer(product)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_product(self):
        response = client.get(reverse('product-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewProductTest(APITestCase):
    """ Test module for creating a new product """

    def setUp(self):
        self.valid_payload = {
            'name': 'Product 4',
            'price': 40.00,
            'description': 'Product 4 description'
        }
        self.invalid_payload = {
            'name': '',
            'price': 40.00,
            'description': 'Product 4 description'
        }

    def test_create_valid_product(self):
        response = client.post(
            reverse('product-list'),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_product(self):
        response = client.post(
            reverse('product-list'),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleProductTest(APITestCase):
    """ Test module for updating an existing product record """

    def setUp(self):
        self.product1 = Product.objects.create(name='Product 1', price=10.00, description='Product 1 description')
        self.product2 = Product.objects.create(name='Product 2', price=20.00, description='Product 2 description')
        self.valid_payload = {
            'name': 'Product 2 updated',
            'price': 25.00,
            'description': 'Product 2 description updated'
        }
        self.invalid_payload = {
            'name': '',
            'price': 25.00,
            'description': 'Product 2 description updated'
        }

    def test_valid_update_product(self):
        response = client.put(
            reverse('product-detail', kwargs={'pk': self.product2.pk}),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_product(self):
        response = client.put(
            reverse('product-detail', kwargs={'pk': self.product2.pk}),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleProductTest(APITestCase):
    """ Test module for deleting an existing product record """

    def setUp(self):
        self.product1 = Product.objects.create(name='Product 1', price=10.00, description='Product 1 description')
        self.product2 = Product.objects.create(name='Product 2', price=20.00, description='Product 2 description')

    def test_valid_delete_product(self):
        response = client.delete(
            reverse('product-detail', kwargs={'pk': self.product2.pk}),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_product(self):
        response = client.delete(
            reverse('product-detail', kwargs={'pk': 30}),
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)