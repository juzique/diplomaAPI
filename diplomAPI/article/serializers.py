from rest_framework import serializers

from .models import Coordinations

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinations
        fields = ['id','username','lon','lat','acc','date']

    def create(self, validated_data):
        return Coordinations.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id',instance.id)
        instance.username = validated_data.get('username', instance.username)
        instance.lon = validated_data.get('lon', instance.lon)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.acc = validated_data.get('acc', instance.acc)
        instance.date = validated_data.get('date', instance.date)


