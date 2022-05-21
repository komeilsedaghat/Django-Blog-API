from rest_framework import serializers
from .models import ArticleModel
from django.utils.text import slugify

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields= ('author','title','slug','content',)


class AddArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields= ('author','title','content',)
        

    def create(self, validated_data):
        article =  ArticleModel(**validated_data,slug=slugify(validated_data['title']))
        article.save()
        return article