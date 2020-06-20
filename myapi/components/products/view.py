from django.db.models import Prefetch
from rest_framework import viewsets
from .model import Product
from .serializer import ProductSerializer
from ..vendors.model import Vendor


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    select_for_includes = {
        'manufacturer': ['manufacturer__name'],
        'sold_items': ['sold_items__rate']
    }
    prefetch_for_includes = {
        '__all__': [],
        'all_manufacturers': [Prefetch('all_manufacturers', queryset=Vendor.objects.select_related('name'))],
        'all_sold_items': [Prefetch('all_sold_items', queryset=Vendor.objects.select_related('rate'))],
    }
