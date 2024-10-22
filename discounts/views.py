"""
    discount/views.py

    This module defines API views for managing product discounts. It includes views for listing and
    creating generic discounts, percentage-based discounts, and fixed amount discounts.
"""

from rest_framework.response import Response
from rest_framework import status, generics

from constants import CREATED_SUCCESSFULLY, SOMETHING_WENT_WRONG
from .constants import DISCOUNT, PERCENTAGE_DISCOUNT, FIXED_AMOUNT_DISCOUNT
from .models import ProductDiscount, PercentageDiscount, FixedAmountDiscount
from .serializers import DiscountSerializer, PercentageDiscountSerializer, FixedAmountDiscountSerializer


class DiscountListCreateView(generics.ListCreateAPIView):
    """
    Handles listing and creating generic discounts.

    This view supports both GET and POST requests, allowing users to retrieve
    existing discounts or create new ones.

    Attributes:
        queryset (QuerySet): A queryset of all ProductDiscount instances.
        serializer_class (Serializer): The serializer class used for validating
        and deserializing discount data.
    """
    queryset = ProductDiscount.objects.all()
    serializer_class = DiscountSerializer

    def create(self, request, *args, **kwargs):
        """
        Creates a new discount using the provided data.

        Args:
            request (Request): The HTTP request containing discount data.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: A response containing the created discount data or error details.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': CREATED_SUCCESSFULLY.replace("{module}", DISCOUNT), 'data': serializer.data},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({'error': SOMETHING_WENT_WRONG, 'details': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


class PercentageDiscountListCreateView(generics.ListCreateAPIView):
    """
    Manages the creation and retrieval of percentage-based discounts.

    This view allows users to list existing percentage discounts or create new ones.

    Attributes:
        queryset (QuerySet): A queryset of all PercentageDiscount instances.
        serializer_class (Serializer): The serializer class for validating and
        deserializing percentage discount data.
    """
    queryset = PercentageDiscount.objects.all()
    serializer_class = PercentageDiscountSerializer

    def create(self, request, *args, **kwargs):
        """
        Creates a new percentage discount using the provided data.

        Args:
            request (Request): The HTTP request containing percentage discount data.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: A response containing the created percentage discount data or error details.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': CREATED_SUCCESSFULLY.replace("{module}", PERCENTAGE_DISCOUNT), 'data': serializer.data},
                status=status.HTTP_201_CREATED)
        else:
            return Response({'error': SOMETHING_WENT_WRONG, 'details': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


class FixedAmountDiscountListCreateView(generics.ListCreateAPIView):
    """
    Allows listing and creating fixed amount discounts.

    This view provides functionality to retrieve existing fixed amount discounts
    and to create new ones.

    Attributes:
        queryset (QuerySet): A queryset of all FixedAmountDiscount instances.
        serializer_class (Serializer): The serializer class for validating and
        deserializing fixed amount discount data.
    """
    queryset = FixedAmountDiscount.objects.all()
    serializer_class = FixedAmountDiscountSerializer

    def create(self, request, *args, **kwargs):
        """
        Creates a new fixed amount discount using the provided data.

        Args:
            request (Request): The HTTP request containing fixed amount discount data.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: A response containing the created fixed amount discount data or error details.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': CREATED_SUCCESSFULLY.replace("{module}", FIXED_AMOUNT_DISCOUNT), 'data': serializer.data},
                status=status.HTTP_201_CREATED)
        else:
            return Response({'error': SOMETHING_WENT_WRONG, 'details': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
