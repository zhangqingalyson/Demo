from django.db import models

# Create your models here.
from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    create = models.DateTimeField(auto_now_add=True)

