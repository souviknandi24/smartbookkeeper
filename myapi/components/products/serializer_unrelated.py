from rest_framework import serializers
from .model import Product


class ProductSerializerUnrelated(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name',
                  'description',
                  'basic_rate',
                  'hsn_sac',
                  'gst_percentage',
                  'measuring_unit']
