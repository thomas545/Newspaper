from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.
# REST_FRAMEWORK

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


##########################

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model() , on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail' , args=[str(self.id)])



class Comment(models.Model):
    article = models.ForeignKey(Article , on_delete=models.CASCADE , related_name='comments')
    author = models.ForeignKey(get_user_model() , on_delete=models.CASCADE)
    comment = models.CharField(max_length=120)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')
