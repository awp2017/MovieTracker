import pdb

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from movie_tracker.models import *
from django.shortcuts import render, redirect
from movie_tracker.forms import *


class Watchlist(View):
    def get(self, request, *args, **kwargs):
        request.user
        watched = UserMovie.objects.filter(user=request.user, status=UserMovie.WATCHED)
        not_watched = UserMovie.objects.filter(user=request.user, status=UserMovie.NOT_WATCHED)

        return render(request, "watchlist/index.html", { 'watched': watched, 'not_watched': not_watched })

    def post(self, request, *args, **kwargs):
        movie_id = request.GET.get('movie_id')
        movie_id = int(movie_id)
        user = request.user
        opt = request.POST.get('opt')
        if opt == 'add':
            add(user, movie_id)

        if opt == 'watch':
            watch_movie(user, movie_id)
        if opt == 'unwatch':
            unwatch_movie(user, movie_id)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add(user, movie_id):
    user_movie = UserMovie.objects.get_or_create(user=user, movie_id=movie_id)[0]
    user_movie.save()


def watch_movie(user, movie_id):
    user_movie = UserMovie.objects.get(user=user, movie_id=movie_id)
    user_movie.status = user_movie.WATCHED
    user_movie.save()


def unwatch_movie(user, movie_id):
    user_movie = UserMovie.objects.get(user=user, movie_id=movie_id)
    user_movie.status = user_movie.NOT_WATCHED
    user_movie.save()
