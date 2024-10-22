"""
    orders/models.py

    This module defines the Order and OrderItem models  It includes functionality for calculating the total
    price of an order, including any applicable discounts.
"""

from django.db import models
from products.models import Product, BaseModel
from discounts.models import ProductDiscount


class Order(models.Model):
    """
    Represents a customer order containing multiple products.

    Attributes:
        products (ManyToManyField): A many-to-many relationship with Product,
            allowing multiple products to be included in an order.
        discount (ForeignKey): A reference to a ProductDiscount that can be
            applied to the order. Can be null or blank.
        total_price (DecimalField): The total price of the order, calculated
            based on the products and any applicable discounts.

    Methods:
        calculate_total(): Calculates the total price of the order, applying
            any discounts if available.
    """
    products = models.ManyToManyField(Product, through='OrderItem')
    discount = models.ForeignKey(ProductDiscount, null=True, blank=True, on_delete=models.SET_NULL)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def calculate_total(self):
        """
        Calculates the total price of the order.

        This method iterates through all OrderItems associated with the order,
        retrieves the price for each product (considering quantity and discounts),
        and sums the total.

        Returns:
            Decimal: The total price of the order, including any applicable discounts.
        """
        total = 0
        for item in self.orderitem_set.all():
            price = item.product.get_price(quantity=item.quantity)
            if self.discount:
                price = self.discount.apply_discount(price)
            total += price * item.quantity
        return total


class OrderItem(models.Model):
    """
    Represents a specific product within an order, including quantity.

    Attributes:
        order (ForeignKey): A reference to the Order this item belongs to.
        product (ForeignKey): A reference to the Product being ordered.
        quantity (PositiveIntegerField): The quantity of the product ordered.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
