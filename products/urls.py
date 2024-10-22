from django.urls import path
from .views import ProductListCreateView, SeasonalProductListCreateView, BulkProductListCreateView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/seasonal/', SeasonalProductListCreateView.as_view(), name='seasonal-product-list-create'),
    path('products/bulk/', BulkProductListCreateView.as_view(), name='bulk-product-list-create'),
]
