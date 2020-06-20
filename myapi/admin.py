# Register your models here.
from django.contrib import admin
from .models import Vendor, Product, Session, Invoice, InvoiceItem

admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(Session)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
