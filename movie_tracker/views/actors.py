# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView
from movie_tracker.models import *
from django.core.paginator import Paginator


class Index(ListView):
    model = Actor
    template_name = 'actors/index.html'
    context_object_name = 'actors'
    paginate_by = 10
