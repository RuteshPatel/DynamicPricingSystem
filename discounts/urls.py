from django.urls import path
from .views import DiscountListCreateView, PercentageDiscountListCreateView, FixedAmountDiscountListCreateView

urlpatterns = [
    path('discounts/', DiscountListCreateView.as_view(), name='discount-list-create'),
    path('discounts/percentage/', PercentageDiscountListCreateView.as_view(), name='percentage-discount-list-create'),
    path('discounts/fixed/', FixedAmountDiscountListCreateView.as_view(), name='fixed-discount-list-create'),
]
