from rest_framework import serializers
from .model import InvoiceItem


class InvoiceItemSerializerUnrelated(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ['name',
                  'description',
                  'rate',
                  'hsn_sac',
                  'gst_percentage',
                  'quantity',
                  'amount',
                  'measuring_unit',
                  'model_serial_number',
                  'created_at',
                  'updated_at'
                  ]
