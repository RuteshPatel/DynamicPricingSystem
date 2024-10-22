"""
    products/serializers.py

    This module defines serializers for product models. It includes serializers for basic products,
    seasonal products, and bulk products.
"""

from rest_framework import serializers
from .models import Product, SeasonalProduct, BulkProduct


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializes the basic Product model, handling name and base price.

    Attributes:
        id (IntegerField): The unique identifier for the product.
        name (CharField): The name of the product.
        base_price (DecimalField): The base price of the product.
    """

    class Meta:
        model = Product
        fields = ['id', 'name', 'price']  # Adjusted to match the model field name


class SeasonalProductSerializer(ProductSerializer):
    """
    Serializes the SeasonalProduct model, adding seasonal discount information.

    Attributes:
        seasonal_discount (DecimalField): The discount percentage applicable
        during the product's seasonal availability.
    """

    class Meta(ProductSerializer.Meta):
        model = SeasonalProduct
        fields = ProductSerializer.Meta.fields + ['seasonal_discount']


class BulkProductSerializer(ProductSerializer):
    """
    Serializes the BulkProduct model, incorporating bulk-specific fields.

    Attributes:
        bulk_threshold (IntegerField): The minimum quantity required to qualify
        for a bulk discount.
        bulk_discount (DecimalField): The discount percentage applied when
        the bulk threshold is met.
    """

    class Meta(ProductSerializer.Meta):
        model = BulkProduct
        fields = ProductSerializer.Meta.fields + ['bulk_threshold', 'bulk_discount']
