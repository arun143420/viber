from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Album(models.Model):
    artist = models.CharField(max_length=50)
    album_title = models.CharField(max_length=120)
    genre = models.CharField(max_length=10)
    album_logo = models.FileField()
    is_fovorite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})  #for creating new

    def __str__(self):
        return self.album_title + '-' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, default="no_album")
    file_type = models.CharField(max_length=15)
    song_title = models.CharField(max_length=250)
    song_file = models.FileField(default="no_song")

    def get_absolute_url(self):
        return reverse('music:song-added-view', kwargs={'pk': self.pk})

    def __str__(self):
        return self.song_title


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10,blank=True)
    address = models.CharField(max_length=30,blank=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
