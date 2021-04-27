from rest_framework import serializers

from .models import Coordination

class ArticleSerializer(serializers.Serializer):
    lon = serializers.DecimalField(max_digits=10, decimal_places=3)
    lat = serializers.DecimalField(max_digits=10, decimal_places=3)
    acc = serializers.DecimalField(max_digits=10, decimal_places=3)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return Coordination.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.lon = validated_data.get('lon', instance.lon)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.acc = validated_data.get('acc', instance.acc)
        instance.date = validated_data.get('date', instance.date)

        instance.save()
        return instance
