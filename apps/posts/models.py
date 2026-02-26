from django.db import models
# from uuid import uuid4 

# Create your models here.
class PostModel(models.Model):
    # id = models.UUIDField(uuid4)
    title = models.CharField(max_length=255)
    content = models.TextField()