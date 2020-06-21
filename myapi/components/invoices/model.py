from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ..vendors.model import Vendor
from ..sessions.model import Session


class Invoice(models.Model):
    invoice_number = models.CharField(null=False, max_length=100)
    invoice_date = models.DateField(null=False)
    invoice_amount = models.DecimalField(null=False, max_digits=14, decimal_places=2, validators=[
        MinValueValidator(0)], default=0)
    invoice_cgst_amount = models.DecimalField(null=False, max_digits=14, decimal_places=2, validators=[
        MinValueValidator(0)], default=0)
    invoice_sgst_amount = models.DecimalField(null=False, max_digits=14, decimal_places=2, validators=[
        MinValueValidator(0)], default=0)
    invoice_igst_amount = models.DecimalField(null=False, max_digits=14, decimal_places=2, validators=[
        MinValueValidator(0)], default=0)
    invoice_utgst_amount = models.DecimalField(null=False, max_digits=14, decimal_places=2, validators=[
        MinValueValidator(0)], default=0)
    delivery_note = models.TextField(blank=True)
    terms_of_payment = models.TextField(blank=True)
    supplier_ref = models.CharField(null=False, blank=True, max_length=100)
    other_ref = models.CharField(null=False, blank=True, max_length=100)
    buyer_order_number = models.CharField(
        null=False, blank=True, max_length=100)
    buyer_order_date = models.DateField(null=True, blank=True)
    despatch_document_number = models.CharField(
        null=False, blank=True, max_length=100)
    delivery_note = models.TextField(blank=True)
    terms_of_delivery = models.TextField(blank=True)
    seller = models.ForeignKey(Vendor, related_name='sold_invoices',
                               null=True, blank=True, default=None, on_delete=models.SET_NULL)
    buyer = models.ForeignKey(Vendor, related_name='bought_invoices',
                              null=True, blank=True, default=None, on_delete=models.SET_NULL)
    session = models.ForeignKey(Session, related_name='invoices',
                                null=True, blank=True, default=None, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}/{} {}'.format(self.invoice_number, self.session, self.buyer)
