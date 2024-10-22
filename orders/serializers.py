"""
    order/serializers.py

    This module defines serializers for order and order item models. It includes serializers for handling
    order details and associated items.
"""

from rest_framework import serializers

from discounts.models import ProductDiscount
from discounts.serializers import DiscountSerializer
from products.serializers import ProductSerializer
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    """
    Serializes the OrderItem model, representing individual items within an order.

    Attributes:
        product (ForeignKey): The product associated with the order item.
        quantity (PositiveIntegerField): The quantity of the product ordered.
    """

    class Meta:
        model = OrderItem
        fields = ["product", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializes the Order model, managing discount information and associated products.

    This serializer handles the creation of an order, including its associated items and discounts.
    It also customizes the representation of the order when retrieved.

    Attributes:
        products (OrderItemSerializer): A list of order items containing product
        and quantity information, write-only for creating orders.

    Methods:
        create(validated_data): Creates a new order and its associated order items.
        to_representation(instance): Customizes the serialized output to include order ID,
        total price, order items, and discount details.
    """
    products = OrderItemSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = ["discount", "products"]

    def create(self, validated_data):
        """
        Creates a new order and its associated order items.

        Args:
            validated_data (dict): The validated data for the order, including
            discount and product information.

        Returns:
            Order: The created order instance with its total price calculated.
        """
        order_items_data = validated_data.pop("products")
        order = Order.objects.create(**validated_data)

        order_items = [OrderItem(order=order, **item) for item in order_items_data]
        OrderItem.objects.bulk_create(order_items)
        order.total_price = order.calculate_total()
        order.save()
        return order

    def to_representation(self, instance):
        """
        Customizes the serialized output of the order instance.

        Args:
            instance (Order): The order instance to be serialized.

        Returns:
            dict: A dictionary representation of the order, including order ID,
            total price, order items, and discount details.
        """
        data = super().to_representation(instance)
        data["order_id"] = instance.id
        data["total_price"] = instance.total_price
        order_items_details = OrderItem.objects.filter(order=instance.id)
        data["order_items"] = OrderItemSerializer(order_items_details, many=True).data
        order_discount = ProductDiscount.objects.filter(id=instance.discount.id).values("name").first()
        data["discount"] = DiscountSerializer(order_discount).data
        return data

