from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Vendor(models.Model):
    name = models.CharField(null=False, max_length=300, unique=True)
    contact_name = models.CharField(blank=True, max_length=300)
    gstin = models.CharField(blank=True, max_length=20)
    address_line_1 = models.CharField(blank=True, max_length=300)
    address_line_2 = models.CharField(blank=True, max_length=300)
    city = models.CharField(blank=True, max_length=100)
    state = models.CharField(blank=True, max_length=100)
    zipcode = models.PositiveIntegerField(
        blank=True, validators=[MinValueValidator(100000), MaxValueValidator(999999)])
    phone_number = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=160)
    bank_account_number = models.PositiveIntegerField(blank=True)
    bank_account_name = models.CharField(blank=True, max_length=300)
    bank_name = models.CharField(blank=True, max_length=200)
    bank_branch_name = models.CharField(blank=True, max_length=200)
    bank_ifs_code = models.CharField(blank=True, max_length=20)
    entity_type = models.CharField(null=False, max_length=20, choices=[(
        'manufacturer', 'MANUFACTURER'), ('buyer', 'BUYER'), ('firm', 'FIRM')], default='buyer')

    def __str__(self):
        return self.name + ' | ' + self.gstin if self.gstin else self.name
