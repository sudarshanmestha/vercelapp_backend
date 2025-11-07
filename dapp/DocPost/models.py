from django.db import models

# Create your models here.

class DocPosts(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.title