from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Image(models.Models):
    """
    Image model creating table
    """
    image = models.ImageField(upload_to='media/', blank=True)
    image_name = models.CharField(max_length=200)
    caption = models.CharField(max_length=1000)
    likes = models.IntegerField(default=0)
    comment = models.CharField(max_length=10000)


