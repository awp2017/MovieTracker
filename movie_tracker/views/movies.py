# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from movie_tracker.models import *
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator


class Index(ListView):
    model = Movie
    template_name = 'movies/index.html'
    context_object_name = 'movies'
    paginate_by = 10

    def get_queryset(self):
        title = self.request.GET.get('movie', '')
        keyword = self.request.GET.get('keyword', '')

        return self.model.objects.filter(title__icontains=title, keywords__name__icontains=keyword).distinct()


class MovieDetailView(DetailView):
    template_name = 'movies/show.html'
    model = Movie
    context_object_name = 'movie'

class CommentsIndex(View):
    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        comments = Comment.objects.filter(movie=pk)
        return render(
            request,
            'movies/comments.html',
            context={'comments': comments,
                     'movie': movie}
        )

    def post(self, request, pk):
        movie_instance = Movie.objects.get(id=pk)
        user_instance = User.objects.get(id=request.user.id)
        comment = Comment(movie=movie_instance, user=user_instance, text=request.POST.get('comment',''))
        comment.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
