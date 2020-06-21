from rest_framework import serializers
from .model import Vendor


class VendorSerializerUnrelated(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = ['name',
                  'contact_name',
                  'gstin',
                  'address_line_1',
                  'address_line_2',
                  'city',
                  'state',
                  'zipcode',
                  'phone_number',
                  'email',
                  'bank_account_number',
                  'bank_account_name',
                  'bank_name',
                  'bank_branch_name',
                  'bank_ifs_code',
                  'entity_type',
                  'created_at',
                  'updated_at'
                  ]
