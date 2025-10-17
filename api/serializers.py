
from rest_framework import serializers


class MovieSerializer(serializers.Serializer):
    name=serializers.CharField()
    descriptions=serializers.CharField()
