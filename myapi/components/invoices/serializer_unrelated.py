from rest_framework import serializers
from .model import Invoice


class InvoiceSerializerUnrelated(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = ['invoice_number',
                  'invoice_date',
                  'invoice_amount',
                  'invoice_cgst_amount',
                  'invoice_sgst_amount',
                  'invoice_igst_amount',
                  'invoice_utgst_amount',
                  'delivery_note',
                  'terms_of_payment',
                  'supplier_ref',
                  'other_ref',
                  'buyer_order_number',
                  'buyer_order_date',
                  'despatch_document_number',
                  'delivery_note',
                  'terms_of_delivery']
