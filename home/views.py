from django.shortcuts import render
from .models import ArticleModel
from rest_framework import generics
from .serializers import ArticleSerializer,AddArticleSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class ListArticleView(generics.ListAPIView):
    queryset = ArticleModel.objects.filter(status=True)
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)

class DetailArticleView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    queryset = ArticleModel.objects.filter(status=True)
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)

    
class AddArticleView(generics.CreateAPIView):
    serializer_class = AddArticleSerializer
    permission_classes = (IsAuthenticated,)
    

class UpdateArticleView(generics.UpdateAPIView):
    lookup_field = 'slug'
    queryset = ArticleModel.objects.filter(status=True)
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)
