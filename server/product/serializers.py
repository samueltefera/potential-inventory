from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.

    Includes the `unit_title` field, which is a read-only field that represents the title of the unit associated with the product.
    """
    unit_title = serializers.CharField(source='unit.title', required=False)

    class Meta:
        model = Product
        fields = '__all__'
