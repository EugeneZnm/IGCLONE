from django.db import models
from django.contrib.auth.models import User
# allows for saving and updating profile
from django.db.models.signals import post_save

# import receiver to receive information form signals
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    """
    method to create profile
    """
    avatar = models.ImageField(upload_to='media/', null=True)
    Bio = models.CharField(max_length=2000)
    # deletion of profile and user when deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    location = models.CharField(max_length=200)
    phone_number = models.IntegerField(default=0)
    email = models.CharField(max_length=500)

    def __str__(self):
        return self.user.username


# sender is source of signal
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    method to create profile
    :return:
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    method to save profile
    :return:
    """
    instance.profile.save()


class Likes(models.Model):
    """
    Like model for likes on images
    """

    Likes = models.IntegerField(default=0)


class Comments(models.Model):
    """
    comment model for comments
    """
    comment = models.TextField()


class Image(models.Model):
    """
    Image model creating table
    """
    image = models.ImageField(upload_to='media', blank=True)
    image_name = models.CharField(max_length=200)
    caption = models.CharField(max_length=1000)
    profile = models.ForeignKey(Profile, null=True)
    likes = models.ForeignKey(Likes, null=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE , default=True)

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


class Follower(models.Model):

    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True)

    @classmethod
    def make_follower(cls, current_user, new_follower):
        follower, created = cls.objects.get_or_create(
            # check whether follower object has current user as owner of friends list
            current_user=current_user
        )

        follower.users.add(new_follower)

    @classmethod
    def remove_follower(cls, current_user, new_follower):
        follower, created = cls.objects.get_or_create(
            # check whether follower object has current user as owner of friends list
            current_user=current_user
        )

        follower.users.remove(new_follower)


