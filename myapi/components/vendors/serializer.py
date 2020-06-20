from .serializer_unrelated import VendorSerializerUnrelated
from ..invoices.serializer_unrelated import InvoiceSerializerUnrelated
from ..products.serializer_unrelated import ProductSerializerUnrelated


class VendorSerializer(VendorSerializerUnrelated):
    included_serializers = {
        'products': ProductSerializerUnrelated,
        'sold_invoices': InvoiceSerializerUnrelated,
        'bought_invoices': InvoiceSerializerUnrelated,
    }

    class Meta(VendorSerializerUnrelated.Meta):
        fields = [*VendorSerializerUnrelated.Meta.fields,
                  'products', 'sold_invoices', 'bought_invoices']

    class JSONAPIMeta:
        select_related = ['products', 'sold_invoices', 'bought_invoices']
