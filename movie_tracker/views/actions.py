# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pdb

from django.shortcuts import redirect
from django.urls import reverse


def search(request):
    option = request.GET.get('option')
    value = request.GET.get('search', '')

    if option == 'actor':
        return redirect(reverse('actors_index') + '?actor={0}'.format(value))
    elif option == 'movie':
        return redirect(reverse('movies_index') + '?movie={0}'.format(value))
    elif option == 'keyword':
        return redirect(reverse('movies_index') + '?keyword={0}'.format(value))
