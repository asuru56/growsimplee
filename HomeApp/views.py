from django.shortcuts import render
from account.models import register_model
from tmdbv3api import TMDb, Movie
import pandas as pd
from django.contrib.staticfiles.storage import staticfiles_storage
from Movies.models import Movies as MovieModel
from slugify import slugify
import numpy as np
from datetime import datetime
import random


apikey = 'e8eff77eaa4fb599fcff9f7459806910'
img = 'http://image.tmdb.org/t/p/original/{your image poster path}'

def MainHome(request):
    tmdb = TMDb()
    tmdb.api_key = apikey
    movie = Movie()

    '''m = movie.details(36668)
    print(m.title)
    print(m.overview)
    print(m.popularity)'''

    mobjten = MovieModel.objects.all()[:20]
    tmvobjten = []
    for i in mobjten:
        m = movie.details(i.tmvdbid)
        tmvobjten.append(m)

    popular = movie.popular()
    pplrobj = []
    for p in popular:
        pplrobj.append(p)


    mobjfft = MovieModel.objects.all()[20:50]
    tmvobjfft = []
    for i in mobjfft:
        m = movie.details(i.tmvdbid)
        tmvobjfft.append(m)

    toprated = movie.top_rated()
    tprobj = []
    for p in toprated:
        tprobj.append(p)

    user = request.user
    context = {
        'tmvobjten': tmvobjten,
        'pplrobj': pplrobj,
        'mobjfft': tmvobjfft,
        'tprobj': tprobj,
    }
    return render(request, 'HomeApp/MainHome.html', context)


def navbar_fun(request):
    try:
        obj = register_model.objects.get(user__username=request.user.username)
        username = obj.usrname
    except:
        username = 'Nothing Broo'

    tempusrnm = username
    print('--->', tempusrnm)

    context = {
        'user': request.user,
        'name': tempusrnm,
    }
    return render(request, 'HomeApp/navbar.html', context)
