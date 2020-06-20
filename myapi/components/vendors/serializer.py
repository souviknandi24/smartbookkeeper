from .serializer_unrelated import VendorSerializerUnrelated
from ..products.serializer import ProductSerializerUnrelated


class VendorSerializer(VendorSerializerUnrelated):
    included_serializers = {
        'products': ProductSerializerUnrelated,
    }

    class Meta(VendorSerializerUnrelated.Meta):
        fields = [*VendorSerializerUnrelated.Meta.fields, 'products']

    class JSONAPIMeta:
        select_related = ['products']
