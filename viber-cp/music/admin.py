from django.contrib import admin
from.models import Profile

# Register your models here.
from .models import Album, Song, Profile
admin.site.register(Album)
admin.site.register(Song)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','phone','address']

    admin.site.register(Profile)
