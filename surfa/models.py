from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"publish")
)

class Post_Projects(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    url = models.URLField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d')
    
    
    def __str__(self):
        return self.title
