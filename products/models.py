"""
    products/models.py

    This module contains the definitions of product models. It includes a base model for shared attributes,
    as well as specific models for regular, seasonal, and bulk products.
"""

from django.db import models


class BaseModel(models.Model):
    """
    Abstract base model that provides timestamp fields for created and updated times.

    Attributes:
        created_at (DateTimeField): The timestamp of when the record was created.
        updated_at (DateTimeField): The timestamp of when the record was last updated.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(BaseModel):
    """
    Represents a standard product with a name and price.

    Attributes:
        name (CharField): The name of the product.
        price (DecimalField): The price of the product.

    Methods:
        get_price(*args, **kwargs): Returns the price of the product.
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_price(self, *args, **kwargs):
        """
        Returns the price of the product.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Decimal: The price of the product.
        """
        return self.price


class SeasonalProduct(Product):
    """
    Represents a product that has a seasonal discount.

    Attributes:
        seasonal_discount (DecimalField): The discount percentage applied to the product.

    Methods:
        get_price(): Returns the price after applying the seasonal discount.
    """
    seasonal_discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def get_price(self):
        """
        Returns the price of the product after applying the seasonal discount.

        Returns:
            Decimal: The price of the product with seasonal discount applied.
        """
        return self.price * (1 - self.seasonal_discount / 100)


class BulkProduct(Product):
    """
    Represents a product that offers a bulk discount based on quantity.

    Attributes:
        bulk_threshold (IntegerField): The minimum quantity to qualify for a bulk discount.
        bulk_discount (DecimalField): The discount percentage applied when the bulk threshold is met.

    Methods:
        get_price(quantity): Returns the price after applying the bulk discount if applicable.
    """
    bulk_threshold = models.IntegerField(default=10)
    bulk_discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def get_price(self, quantity):
        """
        Returns the price of the product after applying the bulk discount based on quantity.

        Args:
            quantity (int): The quantity of the product being purchased.

        Returns:
            Decimal: The price of the product with the bulk discount applied, if applicable.
        """
        if quantity >= self.bulk_threshold:
            return self.price * (1 - self.bulk_discount / 100)
        return self.price
