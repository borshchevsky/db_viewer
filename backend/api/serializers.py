from rest_framework import serializers

from api.models import DB


class DBSerializer(serializers.ModelSerializer):
    class Meta:
        model = DB
        fields = (
            'id',
            'type',
            'host',
            'port',
            'username',
            'password',
            'schema',
        )
