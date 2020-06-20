from rest_framework import serializers
from .model import Session


class SessionSerializerUnrelated(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ['name',
                  'start_date',
                  'end_date']
