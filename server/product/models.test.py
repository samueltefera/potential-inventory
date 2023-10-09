from django.test import TestCase
from common.models import Unit
from supplier.models import Supplier
from .models import Product


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.unit = Unit.objects.create(name='kg')
        cls.supplier = Supplier.objects.create(name='Supplier 1')

    def setUp(self):
        # Set up objects specific to this test method
        self.product = Product.objects.create(
            name='Product 1',
            brand='Brand 1',
            unit=self.unit,
            supplier=self.supplier,
        )

    def test_name_label(self):
        field_label = self.product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_brand_label(self):
        field_label = self.product._meta.get_field('brand').verbose_name
        self.assertEqual(field_label, 'brand')

    def test_unit_label(self):
        field_label = self.product._meta.get_field('unit').verbose_name
        self.assertEqual(field_label, 'unit')

    def test_supplier_label(self):
        field_label = self.product._meta.get_field('supplier').verbose_name
        self.assertEqual(field_label, 'supplier')

    def test_name_max_length(self):
        max_length = self.product._meta.get_field('name').max_length
        self.assertEqual(max_length, 63)

    def test_brand_max_length(self):
        max_length = self.product._meta.get_field('brand').max_length
        self.assertEqual(max_length, 50)

    def test_object_name_is_name(self):
        expected_object_name = self.product.name
        self.assertEqual(expected_object_name, str(self.product))