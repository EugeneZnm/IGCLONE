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

    def save_image(self):
        """
        method to save images
        :return:
        """
        self.save()

    def get_image(self):
        """
        method to get image by id
        :return:
        """
        self.get_image()

    def delete_image(self):
        """
        method to delete image
        :return:
        """
        self.delete()
