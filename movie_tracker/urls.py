from django.conf.urls import url

import views.actors as actors
import views.movies as movies

import views.test as test

urlpatterns = [
    url(r'^movies/$', movies.Index.as_view(), name='movies_index'),
    url(r'^movies/(?P<pk>[0-9]+)/$', movies.MovieDetailView.as_view(), name='movies_show'),
    url(r'^movies/(?P<pk>[0-9]+)/comments$', movies.CommentsIndex.as_view(), name='movie_comments'),
    url(r'^movies/(?P<pk_movie>[0-9]+)/actors/$', actors.Index.as_view(), name='movie_actors'),
    url(r'^actors/$', actors.Index.as_view(), name='actors_index'),
    url(r'^actors/(?P<pk>[0-9]+)/$', actors.Show.as_view(), name='actors_show'),
    url(r'^watched/$', actors.Index.as_view(),name='movies_watched'),
    url(r'^test/$', test.Test.as_view(), name='test'),
]

