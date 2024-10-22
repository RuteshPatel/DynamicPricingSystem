"""
    discounts/models.py

    This module defines discount models for products. It includes different types of discounts,
    such as percentage-based and fixed amount discounts
"""

from django.db import models
from products.models import BaseModel


class ProductDiscount(BaseModel):
    """
    Represents a general product discount.

    Attributes:
        name (CharField): The name of the discount.

    Methods:
        apply_discount(price): Applies the discount to the given price.
    """
    name = models.CharField(max_length=100)

    def apply_discount(self, price):
        """
        Applies the discount to the given price.

        This method can be overridden by subclasses to implement specific discount logic.

        Args:
            price (Decimal): The original price of the product.

        Returns:
            Decimal: The price after applying the discount (no modification in base class).
        """
        return price


class PercentageDiscount(ProductDiscount):
    """
    Represents a discount based on a percentage reduction.

    Attributes:
        percentage (DecimalField): The percentage of the discount to apply.

    Methods:
        apply_discount(price): Applies the percentage discount to the given price.
    """
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def apply_discount(self, price):
        """
        Applies the percentage discount to the given price.

        Args:
            price (Decimal): The original price of the product.

        Returns:
            Decimal: The price after applying the percentage discount.
        """
        return price * (1 - self.percentage / 100)


class FixedAmountDiscount(ProductDiscount):
    """
    Represents a discount that deducts a fixed amount from the price.

    Attributes:
        amount (DecimalField): The fixed amount to subtract from the price.

    Methods:
        apply_discount(price): Applies the fixed amount discount to the given price.
    """
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def apply_discount(self, price):
        """
        Applies the fixed amount discount to the given price.

        Args:
            price (Decimal): The original price of the product.

        Returns:
            Decimal: The price after applying the fixed amount discount, ensuring
            it does not go below zero.
        """
        return max(0, price - self.amount)
