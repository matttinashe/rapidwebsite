from django.db import models


# Create your models here.
class Highlight(models.Model):
    picture_post = models.CharField(max_length=64)
    picture_background = models.ImageField()
    date_published = models.DateTimeField()
