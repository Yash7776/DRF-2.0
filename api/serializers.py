
from rest_framework import serializers
from . models import Movie

class MovieSerializer(serializers.Serializer):
    name=serializers.CharField()
    descriptions=serializers.CharField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.descriptions=validated_data.get('descriptions',instance.descriptions)
        instance.save()
        return instance
    
