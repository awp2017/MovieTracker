# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from movie_tracker.models import *
from django.core.paginator import Paginator


class Index(ListView):
    model = Movie
    template_name = 'movies/index.html'
    context_object_name = 'movies'
    paginate_by = 10

    def get_queryset(self):
        title = self.request.GET.get('movie', '')
        keyword = self.request.GET.get('keyword', '')

        return self.model.objects.filter(title__contains=title, keywords__name__contains=keyword)


class MovieDetailView(DetailView):
    template_name = 'movies/show.html'
    model = Movie
    context_object_name = 'movie'
