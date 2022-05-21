from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class ArticleModel(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='author')
    title = models.CharField(max_length=220)
    slug  = models.SlugField(max_length=220)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.content}"