# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.urls import reverse


def search(request):
    if request.GET.get('actor'):
        return redirect(reverse('actors_index') + '?actor={0}'.format(request.GET.get('actor')))

    if request.GET.get('movie'):
        return redirect(reverse('movies_index') + '?movie={0}'.format(request.GET.get('movie')))

    if request.GET.get('keyword'):
        return redirect(reverse('movies_index') + '?keyword={0}'.format(request.GET.get('keyword')))
