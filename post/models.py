from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=4096)
    thumb_url = models.CharField(max_length=8092)
    content = models.TextField(max_length=4096)
    
    