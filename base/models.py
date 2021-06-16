from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.query import NamedValuesListIterable
from django.shortcuts import resolve_url

# Create your models here.

class Bob(models.Model):
    TITLE = (
        ('Godbob', 'Godbob'),
        ('Archbob', 'Archbob'),
        ('Masterbob', 'Masterbob'),
        ('Newbob', 'Newbob'), 
    )

    name = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True, choices=TITLE)
    contribution = models.IntegerField(max_length=200, null=True, default=0)


    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    CATEGORY = (
        ('Bob Moment', 'Bob Moment'),
        ('Tech', 'Tech'),
    )

    title = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(Bob, null=True, on_delete= models.SET_NULL)
    body = models.TextField(max_length=600, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self) -> str:
        return self.title