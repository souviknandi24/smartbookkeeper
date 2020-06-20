from .serializer_unrelated import ProductSerializerUnrelated
from ..vendors.serializer_unrelated import VendorSerializerUnrelated
from ..invoice_items.serializer_unrelated import InvoiceItemSerializerUnrelated


class ProductSerializer(ProductSerializerUnrelated):
    included_serializers = {
        'manufacturer': VendorSerializerUnrelated,
        'invoice_items': InvoiceItemSerializerUnrelated
    }

    class Meta(ProductSerializerUnrelated.Meta):
        fields = [*ProductSerializerUnrelated.Meta.fields,
                  'manufacturer', 'invoice_items']

    class JSONAPIMeta:
        select_related = ['manufacturer', 'invoice_items']
