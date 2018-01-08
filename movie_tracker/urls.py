from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^movies/', MoviesIndex.as_view(), name='movies_index')
]
