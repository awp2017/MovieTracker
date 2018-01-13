from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^movies/', MoviesIndex.as_view(), name='movies_index'),
    url(r'^/movies/(?P<pk>[0-9]+)/$', MoviesIndex.as_view(), name='movies_show'),
    url(r'^/movies/(?P<pk>[0-9]+)/comments$', MoviesIndex.as_view(), name='movie_comments'),
    url(r'^/movies/(?P<pk_movie>[0-9]+)/actors/$', MoviesIndex.as_view(), name='movie_actors'),
    url(r'^/actors/', MoviesIndex.as_view(), name='actors_index'),
    url(r'^/actors/(?P<pk>[0-9]+)/$', MoviesIndex.as_view(), name='actors_show'),
    url(r'^/watched$', MoviesIndex.as_view(),name='movies_watched'),
]

