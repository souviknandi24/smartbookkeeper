from .serializer_unrelated import InvoiceSerializerUnrelated
from ..vendors.serializer_unrelated import VendorSerializerUnrelated
from ..sessions.serializer_unrelated import SessionSerializerUnrelated
from ..invoice_items.serializer_unrelated import InvoiceItemSerializerUnrelated


class InvoiceSerializer(InvoiceSerializerUnrelated):
    included_serializers = {
        'seller': VendorSerializerUnrelated,
        'buyer': VendorSerializerUnrelated,
        'session': SessionSerializerUnrelated,
        'invoice_items': InvoiceItemSerializerUnrelated
    }

    class Meta(InvoiceSerializerUnrelated.Meta):
        fields = [*InvoiceSerializerUnrelated.Meta.fields,
                  'seller', 'buyer', 'session', 'invoice_items']

    class JSONAPIMeta:
        select_related = ['seller', 'buyer', 'session', 'invoice_items']
