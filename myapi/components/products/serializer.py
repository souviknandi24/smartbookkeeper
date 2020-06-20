from .serializer_unrelated import ProductSerializerUnrelated
from ..vendors.serializer_unrelated import VendorSerializerUnrelated


class ProductSerializer(ProductSerializerUnrelated):
    included_serializers = {
        'manufacturer': VendorSerializerUnrelated
    }

    class Meta(ProductSerializerUnrelated.Meta):
        fields = [*ProductSerializerUnrelated.Meta.fields, 'manufacturer']

    class JSONAPIMeta:
        select_related = ['manufacturer']
