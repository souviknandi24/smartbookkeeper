# views.py
from rest_framework_json_api import views
from .components.vendors.view import VendorViewSet
from .components.products.view import ProductViewSet
from .components.sessions.view import SessionViewSet
from .components.invoices.view import InvoiceViewSet
from .components.invoice_items.view import InvoiceItemViewSet
