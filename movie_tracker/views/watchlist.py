import pdb

from django.urls import reverse
from django.views.generic import View
from movie_tracker.models import *
from django.shortcuts import render, redirect
from movie_tracker.forms import *


class Watchlist(View):
    def get(self, request, *args, **kwargs):
        watched = UserMovie.objects.filter(user=request.user, status=UserMovie.WATCHED)
        not_watched = UserMovie.objects.filter(user=request.user, status=UserMovie.NOT_WATCHED)

        return render(request, "watchlist/index.html", {'watched': watched, 'not_watched': not_watched})

    def post(self, request, *args, **kwargs):
        movie_id = request.GET.get('movie_id')
        movie_id = int(movie_id)

        user_movie = UserMovie(user=request.user, movie_id=movie_id)
        user_movie.save()
        return redirect('movies_index')

    def delete(self, request, *args, **kwargs):
        id = request.GET.get('id')
        UserMovie.get(pk=id)
        UserMovie.delete()
        return redirect('movies_index')

    def put(self, request, *args, **kwargs):
        id = request.PUT.get('id')
        status = request.PUT.get('status')

        UserMovie.get(pk=id)
        UserMovie.status = status
        UserMovie.save()