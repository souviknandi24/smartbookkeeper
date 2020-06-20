from .serializer_unrelated import SessionSerializerUnrelated


class SessionSerializer(SessionSerializerUnrelated):
    included_serializers = {
    }

    class Meta(SessionSerializerUnrelated.Meta):
        fields = [*SessionSerializerUnrelated.Meta.fields]

    class JSONAPIMeta:
        select_related = []
