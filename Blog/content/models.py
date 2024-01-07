from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
User = get_user_model()

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='author_image')
    date_create = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.username
class Article(models.Model):
    article_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    category = models.CharField(max_length=100)
    titre = models.CharField(max_length=100)
    article_img = models.ImageField(upload_to='article_image', default='blank-profile-picture.png')
    body = models.TextField()
    date_create = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.titre


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


    
    

