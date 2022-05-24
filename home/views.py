from django.shortcuts import render
from .models import ArticleModel
from rest_framework import generics
from .serializers import ArticleSerializer,AddArticleSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle


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
    throttle_classes = (UserRateThrottle,)
    serializer_class = AddArticleSerializer
    permission_classes = (IsAuthenticated,)
    

class UpdateArticleView(generics.UpdateAPIView):
    throttle_classes = (UserRateThrottle,)
    lookup_field = 'slug'
    queryset = ArticleModel.objects.filter(status=True)
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)

class DeleteArticleView(generics.DestroyAPIView):
    throttle_classes = (UserRateThrottle,)
    throttle_classes = (UserRateThrottle,)
    lookup_field = 'slug'
    queryset = ArticleModel.objects.filter(status=True)
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)


