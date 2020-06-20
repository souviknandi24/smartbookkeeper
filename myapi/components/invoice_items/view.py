from django.db.models import Prefetch
from rest_framework import viewsets
from .model import InvoiceItem
from .serializer import InvoiceItemSerializer
from ..products.model import Product
from ..invoices.model import Invoice


class InvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = InvoiceItem.objects.all().order_by('id')
    serializer_class = InvoiceItemSerializer
    select_for_includes = {
        'product': ['product__name'],
        'invoice': ['invoice__invoice_number'],
    }
    prefetch_for_includes = {
        '__all__': [],
        'all_products': [Prefetch('all_products', queryset=Product.objects.select_related('name'))],
        'all_invoices': [Prefetch('all_invoices', queryset=Invoice.objects.select_related('invoice_number'))],
    }
