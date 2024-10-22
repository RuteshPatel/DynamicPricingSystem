"""
    products/views.py

    This module defines API views for managing product models. It includes views for listing and creating general products,
    seasonal products, and bulk products.
"""

from rest_framework import generics, status
from rest_framework.response import Response

from constants import CREATED_SUCCESSFULLY, SOMETHING_WENT_WRONG
from .constants import PRODUCT, BULK_PRODUCT, SEASONAL_PRODUCT
from .models import Product, SeasonalProduct, BulkProduct
from .serializers import ProductSerializer, SeasonalProductSerializer, BulkProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    """
    Handles listing of all products and creating new products.

    This view supports both GET and POST methods for product management.

    Attributes:
        queryset (QuerySet): A queryset of all Product instances.
        serializer_class (Serializer): The serializer class for validating and
        deserializing product data.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        """
        Creates a new product using the provided data.

        Args:
            request (Request): The HTTP request containing product data.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: A response containing the created product data or error details.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': CREATED_SUCCESSFULLY.replace("{module}", PRODUCT), 'data': serializer.data},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({'error': SOMETHING_WENT_WRONG, 'details': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


class SeasonalProductListCreateView(generics.ListCreateAPIView):
    """
    Handles listing of all seasonal products and creating new products.

    This view implements custom seasonal discount logic and returns appropriate
    success or error messages.

    Attributes:
        queryset (QuerySet): A queryset of all SeasonalProduct instances.
        serializer_class (Serializer): The serializer class for validating and
        deserializing seasonal product data.
    """
    queryset = SeasonalProduct.objects.all()
    serializer_class = SeasonalProductSerializer

    def create(self, request, *args, **kwargs):
        """
        Creates a new seasonal product using the provided data.

        Args:
            request (Request): The HTTP request containing seasonal product data.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: A response containing the created seasonal product data or error details.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': CREATED_SUCCESSFULLY.replace("{module}", SEASONAL_PRODUCT),
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': SOMETHING_WENT_WRONG, 'details': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


class BulkProductListCreateView(generics.ListCreateAPIView):
    """
    Manages the creation and retrieval of bulk products.

    This view supports listing existing bulk products and creating new ones.

    Attributes:
        queryset (QuerySet): A queryset of all BulkProduct instances.
        serializer_class (Serializer): The serializer class for validating and
        deserializing bulk product data.
    """
    queryset = BulkProduct.objects.all()
    serializer_class = BulkProductSerializer

    def create(self, request, *args, **kwargs):
        """
        Creates a new bulk product using the provided data.

        Args:
            request (Request): The HTTP request containing bulk product data.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: A response containing the created bulk product data or error details.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': CREATED_SUCCESSFULLY.replace("{module}", BULK_PRODUCT), 'data': serializer.data},
                status=status.HTTP_201_CREATED)
        else:
            return Response({'error': SOMETHING_WENT_WRONG, 'details': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
