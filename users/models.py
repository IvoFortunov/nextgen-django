from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import pre_save
import os
from django.core.validators import FileExtensionValidator
import datetime


from django.dispatch import receiver
from django.forms import ImageField

class Profile(models.Model):
    HAND_CHOICES=(('L', 'Лява'),('R', 'Дясна'))
    BACKHAND_CHOICES=(('S', 'С една ръка'), ('D', 'С две ръце'))
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank= True)
    name = models.CharField(max_length=200, null=True, blank= True)
    email = models.EmailField(max_length=500, null=True, blank= True)
    linked_email = models.EmailField(max_length=500, null=True, blank= True)
    username = models.CharField(max_length=200, null=True, blank= True)
    location = models.CharField(max_length=200, null=True, blank= True)
    intro = models.CharField(max_length=200, null=True, blank= True)
    bio = models.TextField(null=True, blank= True)
    profile_image = models.ImageField(null=True, blank= True, upload_to='profiles', default="profiles/user-default.png")
    date_of_birth = models.DateField(null=True, blank= True)
    is_coach = models.BooleanField(default=False)
    hand = models.CharField(max_length=10, choices = HAND_CHOICES, default = "R")
    backhand = models.CharField(max_length=10, choices = BACKHAND_CHOICES, default = "D")
    social_facebook = models.CharField(max_length=200, null=True, blank= True)
    social_instagram = models.CharField(max_length=200, null=True, blank= True)
    
     
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    class Meta:
        ordering = ['name']

    def __str__(self)->str:
        return str(self.name)
    
class Presentation(models.Model):
    player = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True, blank=True)
    video = models.FileField(null=True, upload_to='profiles/videos',
            validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    class Meta:
        ordering = ['player__name']

    def __str__(self)->str:
        return str(self.player.name)

class Messages(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="recipient")
    subject = models.CharField(max_length=200, null=True)
    body = models.TextField(null=True)
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    class Meta:
        ordering = ['is_read', '-created']

    def __str__(self)->str:
        return self.subject
    
class PlayerOTW(models.Model):
    YEARS = [(i,i) for i in range(2023,2033)]
    WEEKS = [(i,i) for i in range(1,58)]
    currentYear = datetime.datetime.now().year
    currentWeek = datetime.datetime.now().isocalendar()[1]
    player = models.ForeignKey(Profile,null=True, on_delete=models.SET_NULL)
    year = models.IntegerField(choices = YEARS, default=currentYear)
    week = models.IntegerField(choices = WEEKS, default=currentWeek)

    class Meta:
        ordering = ['-year', '-week']
        unique_together = ('week', 'year')

    def __str__(self)->str:
        return str(self.player.name + ', Седмица: ' + str(self.week) + ', Година: ' + str(self.year))

    



    




    

