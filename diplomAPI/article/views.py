from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.

from .models import Coordinations, User
from .serializers import ArticleSerializer

class ArticleView(ListCreateAPIView):
    queryset = Coordinations.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        #user = get_object_or_404(User, id=self.request.data.get('id'))
        return serializer.save()

class SingleArticleView(RetrieveUpdateDestroyAPIView):
    queryset = Coordinations.objects.all()
    serializer_class = ArticleSerializer
