"""
    discount/serializers.py

    This module defines serializers for discount models. It includes serializers for base product discounts,
    percentage discounts, and fixed amount discounts.
"""

from rest_framework import serializers
from .models import ProductDiscount, PercentageDiscount, FixedAmountDiscount


class DiscountSerializer(serializers.ModelSerializer):
    """
    Serializes the ProductDiscount model, providing fields for basic discount information.

    Attributes:
        id (IntegerField): The unique identifier for the discount.
        name (CharField): The name of the discount.
    """

    class Meta:
        model = ProductDiscount
        fields = ['id', 'name']


class PercentageDiscountSerializer(DiscountSerializer):
    """
    Serializes the PercentageDiscount model, including additional percentage information.

    Attributes:
        percentage (DecimalField): The percentage value of the discount.
    """

    class Meta(DiscountSerializer.Meta):
        model = PercentageDiscount
        fields = DiscountSerializer.Meta.fields + ['percentage']


class FixedAmountDiscountSerializer(DiscountSerializer):
    """
    Serializes the FixedAmountDiscount model, incorporating the fixed discount amount.

    Attributes:
        amount (DecimalField): The fixed amount to deduct from the price.
    """

    class Meta(DiscountSerializer.Meta):
        model = FixedAmountDiscount
        fields = DiscountSerializer.Meta.fields + ['amount']
