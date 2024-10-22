"""
    order/views.py

    This module defines API views for managing orders.It includes a view for creating new orders.
"""

from rest_framework import generics, status
from rest_framework.response import Response

from constants import CREATED_SUCCESSFULLY, SOMETHING_WENT_WRONG
from .constants import ORDER
from .models import Order
from .serializers import OrderSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    """
    Handles the creation of new orders.

    This view supports POST requests to create new orders in the system.

    Attributes:
        queryset (QuerySet): A queryset of all Order instances.
        serializer_class (Serializer): The serializer class used for validating and
        deserializing order data.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        """
        Creates a new order using the provided data.

        Args:
            request (Request): The HTTP request containing order data.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: A response containing the created order data or error details.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {'message': CREATED_SUCCESSFULLY.replace("{module}", ORDER), 'data': serializer.data},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response({'error': SOMETHING_WENT_WRONG, 'details': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
