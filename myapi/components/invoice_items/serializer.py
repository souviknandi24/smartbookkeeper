from .serializer_unrelated import InvoiceItemSerializerUnrelated
from ..products.serializer_unrelated import ProductSerializerUnrelated
from ..invoices.serializer_unrelated import InvoiceSerializerUnrelated


class InvoiceItemSerializer(InvoiceItemSerializerUnrelated):
    included_serializers = {
        'product': ProductSerializerUnrelated,
        'invoice': InvoiceSerializerUnrelated,
    }

    class Meta(InvoiceItemSerializerUnrelated.Meta):
        fields = [*InvoiceItemSerializerUnrelated.Meta.fields,
                  'product', 'invoice']

    class JSONAPIMeta:
        select_related = ['product', 'invoice']
