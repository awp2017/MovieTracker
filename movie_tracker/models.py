# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length = 200)


class Keyword(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length = 200)
    release_date = models.DateField(null = True)
    runtime = models.IntegerField()
    genres = models.CharField(max_length = 2000)
    budget = models.IntegerField()
    overview = models.CharField(max_length = 2000)
    tagline = models.CharField(max_length = 2000)
    actors = models.ManyToManyField(Actor, blank = True)
    keywords = models.ManyToManyField(Keyword, blank = True)

    def __str__(self):
        return self.title


class Watched(models.Model):
    watched = models.BooleanField(default = False)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
