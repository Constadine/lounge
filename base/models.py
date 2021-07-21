from django.db import models
from django.contrib.auth.models import User

from django.db.models.fields.related import ForeignKey
from django.db.models.query import NamedValuesListIterable
from django.shortcuts import resolve_url
from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime import datetime
# Create your models here.

class Bob(models.Model):
    TITLE = (
        ('Godbob', 'Godbob'),
        ('Archbob', 'Archbob'),
        ('Masterbob', 'Masterbob'),
        ('Newbob', 'Newbob'), 
        ('Failbob', 'Failbob'),
        ('Lesbob', 'Lesbob'),
    )
    user = models.OneToOneField(User,related_name="profile", null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True, choices=TITLE)
    contribution = models.IntegerField(max_length=200, null=True, default=0)


    def __str__(self) -> str:
        return self.name or '-'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Bob.objects.create(user=instance, name=instance.username)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Tag(models.Model):

    name = models.CharField(max_length=200, null=True)
    
    def __str__(self) -> str:

        return self.name    
        
class Post(models.Model):
    # CATEGORY = (
    #     ('Bob Moment', 'Bob Moment'),
    #     ('Tech', 'Tech'),
    # )

    title = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(Bob, null=True, on_delete= models.SET_NULL)
    body = models.TextField(max_length=600, null=True)
    # category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)


    def __str__(self) -> str:
        return self.title

class Room(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.name
        
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=100000)
    room = models.CharField(max_length=100000)
