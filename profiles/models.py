from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

"""Users will have their own 'profile page' which they can edit """

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=False)
    image = models.ImageField(
        upload_to='images/', default='../default_ifhb1q')
    bio = models.TextField(max_length=500, blank=True)
    location = models.TextField(max_length=255, blank=True)
    currently_reading = models.TextField(max_length=350, blank=True)
    favourite_coffee = models.TextField(max_length=350, blank=True)
    pets_name = models.TextField(max_length=350, blank=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
