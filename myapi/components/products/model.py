from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ..vendors.model import Vendor


class Product(models.Model):
    name = models.CharField(null=False, max_length=100)
    measuring_unit = models.CharField(
        null=False, max_length=20, default='units')
    description = models.TextField(blank=True)
    basic_rate = models.DecimalField(
        max_digits=14, decimal_places=2, blank=True, validators=[MinValueValidator(0)])
    hsn_sac = models.CharField(blank=True, max_length=100)
    gst_percentage = models.PositiveIntegerField(
        blank=True, validators=[MinValueValidator(0), MaxValueValidator(100)])
    manufacturer = models.ForeignKey(
        Vendor, related_name='products', null=True, blank=True, default=None, on_delete=models.SET_NULL)

    def __str__(self):
        return '{} ({})'.format(self.name, self.manufacturer) if self.manufacturer else self.name
