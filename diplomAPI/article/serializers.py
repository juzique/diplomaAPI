from rest_framework import serializers

from .models import Coordinations

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinations
        fields = ['id','username','lon','lat','acc','date']

