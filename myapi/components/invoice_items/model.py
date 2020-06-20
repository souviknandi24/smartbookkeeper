from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ..products.model import Product
from ..invoices.model import Invoice


class InvoiceItem(models.Model):
    name = models.CharField(null=False, max_length=100)
    quantity = models.PositiveIntegerField(
        null=False, validators=[MinValueValidator(1)], default=1)
    rate = models.DecimalField(null=False, max_digits=14, decimal_places=2,
                               validators=[MinValueValidator(0)], default=0)
    hsn_sac = models.CharField(null=False, max_length=100)
    gst_percentage = models.PositiveIntegerField(
        null=False, validators=[MinValueValidator(0)], default=0)
    amount = models.DecimalField(null=False, max_digits=14, decimal_places=2, validators=[
        MinValueValidator(0)], default=0)
    measuring_unit = models.CharField(
        null=False, max_length=20, default='units')
    description = models.TextField(blank=True)
    model_serial_number = models.TextField(blank=True)
    product = models.ForeignKey(Product, related_name='invoice_items',
                                null=True, blank=True, default=None, on_delete=models.SET_NULL)
    invoice = models.ForeignKey(Invoice, related_name='invoice_items',
                                null=True, blank=True, default=None, on_delete=models.SET_NULL)

    def __str__(self):
        return '{} '.format(self.product)
