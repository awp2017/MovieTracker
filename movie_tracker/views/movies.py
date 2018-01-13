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
    paginate_by = 12

    def get_queryset(self):
        title = self.request.GET.get('movie', '')
        keyword = self.request.GET.get('keyword', '')

        return self.model.objects.filter(title__icontains=title, keywords__name__icontains=keyword).distinct()


class MovieDetailView(View):
    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        if request.user.is_authenticated:
            watched = Movie.objects.get(pk=pk).usermovie_set.filter(user=request.user).exists()
        else: 
            watched = None
        comments = Comment.objects.filter(movie=pk).order_by('-date')
        return render(
            request,
            'movies/show.html',
            context={ 'comments': comments,
                      'movie': movie,
                      'watched': watched }
        )

    def post(self, request, pk):
        movie_instance = Movie.objects.get(id=pk)
        user_instance = User.objects.get(id=request.user.id)
        comment = Comment(movie=movie_instance, user=user_instance, text=request.POST.get('comment', ''))
        comment.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
