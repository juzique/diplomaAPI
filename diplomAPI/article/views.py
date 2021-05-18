from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
# Create your views here.

from .models import Coordinations
from .serializers import ArticleSerializer

class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        articles = Coordinations.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    def post(self, request):
        #pk = kwargs.get('pk')
        article = request.data.get('article')
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(article_saved.data)})

    def put(self, request, pk):
        saved_article = get_object_or_404(Coordinations.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Article '{}' updated successfully".format(pk)
        })

    def delete(self, request, pk):
        # Get object with this pk
        article = get_object_or_404(Coordinations.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Article with id `{}` has been deleted.".format(pk)
        }, status=204)