from rest_framework import serializers
from .models import Article, LANGUAGE_CHOICES, STYLE_CHOICES


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'body', 'date',
                  'author', )
