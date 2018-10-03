from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    """
    method to create profile
    """
    avatar = models.ImageField(upload_to='media/profile/', blank=True)
    Bio = models.CharField(max_length=2000)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    location = models.CharField(max_length=200)
    phone_number = models.IntegerField(default=0)
    email = models.CharField(max_length=500)

    def save_profile(self):
        """
        method to save profile
        :return:
        """
        self.save()

    def delete_profile(self):
        """
        method to delete profile
        :return:
        """
        self.delete()

    # @classmethod
    # def find_profile(cls, name):
    #     """
    #     method to find profiles by name
    #     :param name:
    #     :return:
    #     """
    #     name = cls.objects.filter()


class Likes(models.Model):
    """
    Like model for likes on images
    """
    profile = models.ForeignKey(Profile)
    Likes = models.IntegerField(default=0)


class Comments(models.Model):
    """
    comment model for comments
    """
    comment = models.TextField()
    profile = models.ForeignKey(Profile)


class Image(models.Model):
    """
    Image model creating table
    """
    image = models.ImageField(upload_to='media/', blank=True)
    image_name = models.CharField(max_length=200)
    caption = models.CharField(max_length=1000)
    profile = models.ForeignKey(Profile, null=True, blank=True)
    likes = models.ForeignKey(Likes)

    def save_image(self):
        """
        method to save images
        :return:
        """
        self.save()

    @classmethod
    def get_image(cls, image_id):
        """
        method to get image by id
        :return:
        """
        images = cls.objects.filter(id=image_id)
        return images

    def delete_image(self):
        """
        method to delete image
        :return:
        """
        self.delete()






