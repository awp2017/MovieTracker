# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pdb

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from movie_tracker.models import *
from django.core.paginator import Paginator


class Index(ListView):
    model = Actor
    template_name = 'actors/index.html'
    context_object_name = 'actors'
    paginate_by = 10

    def get_queryset(self):
        name = self.request.GET.get('actor','')

        return self.model.objects.filter(name__contains=name)


class Show(DetailView):
    model = Actor
    template_name = 'actors/show.html'
    context_object_name = 'actor'
