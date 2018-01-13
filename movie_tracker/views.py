# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView
from movie_tracker.models import *


# Create your views here.

class MoviesIndex(ListView):
    model = Movie
    template_name = 'movies-index.html'
    context_object_name = 'movies'
