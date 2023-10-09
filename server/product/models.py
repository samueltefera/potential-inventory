from django.db import models
from common.models import TimeStamp, Unit
from supplier.models import Supplier


class Product(TimeStamp):
    """
    A model representing a product in the inventory.

    Attributes:
    - name (str): The name of the product.
    - brand (str): The brand of the product.
    - unit (Unit): The unit of measurement for the product.
    - supplier (Supplier): The supplier of the product.

    Methods:
    - __str__(): Returns the name of the product as a string.
    """
    name = models.CharField(max_length=63)
    brand = models.CharField(max_length=50)
    unit = models.ForeignKey(to=Unit, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(to=Supplier, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


