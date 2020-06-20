from .serializer_unrelated import SessionSerializerUnrelated
from ..invoices.serializer_unrelated import InvoiceSerializerUnrelated


class SessionSerializer(SessionSerializerUnrelated):
    included_serializers = {
        'invoices': InvoiceSerializerUnrelated,
    }

    class Meta(SessionSerializerUnrelated.Meta):
        fields = [*SessionSerializerUnrelated.Meta.fields, 'invoices']

    class JSONAPIMeta:
        select_related = ['invoices']
