from django.db.models import Prefetch
from rest_framework import viewsets
from .model import Invoice
from .serializer import InvoiceSerializer
from ..vendors.model import Vendor
from ..sessions.model import Session
from ..invoice_items.model import InvoiceItem


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all().order_by('id')
    serializer_class = InvoiceSerializer
    select_for_includes = {
        'seller': ['seller__name'],
        'buyer': ['buyer__name'],
        'session': ['session__name'],
        'invoice_items': ['invoice_items__product']
    }
    prefetch_for_includes = {
        '__all__': [],
        'all_sellers': [Prefetch('all_sellers', queryset=Vendor.objects.select_related('name'))],
        'all_buyers': [Prefetch('all_buyers', queryset=Vendor.objects.select_related('name'))],
        'all_sessions': [Prefetch('all_sessions', queryset=Session.objects.select_related('name'))],
        'all_invoice_items': [Prefetch('all_invoice_items', queryset=InvoiceItem.objects.select_related('product'))],
    }
