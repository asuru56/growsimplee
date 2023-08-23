from django.shortcuts import render
from docutils.utils.math.latex2mathml import mo
from scipy.interpolate import interp1d
from Movies.models import Movies as MoviesModel
from Movies.models import SeriesModel
from Movies.models import season as season_model
from .forms import add_movie_form
from Movies.models import Movies as MovieModel
from tmdbv3api import TMDb, Movie, TV, Trending

apikey = 'e8eff77eaa4fb599fcff9f7459806910'
img = 'http://image.tmdb.org/t/p/original/{your image poster path}'
tmdb = TMDb()
tmdb.api_key = apikey
movie = Movie()
tv = TV()

def Movies(request):
    Letest_Movie = MoviesModel.objects.all().order_by('-date')
    context = {
        'letest_movie': Letest_Movie,
    }
    return render(request, '../templates/Movies/Movies.html')

def add_movie(request):
    if request.method == 'POST':
        form = add_movie_form(request.POST)
        print('This Is Shitty Thumbnail :',)
    else:
        form = add_movie_form()
    context = {
        'form': form
    }
    return render(request, '../templates/Movies/add_movie.html', context)


def movie_details(request, movie_id):
    movobj = movie.details(movie_id)

    similar = movie.similar(movie_id)
    smlrobj = []
    for result in similar:
        smlrobj.append(result)

    context = {
        'movobj': movobj,
        'smlrobj': smlrobj,
    }
    return render(request, '../templates/Movies/movie_details.html', context)

def search_details(request):
    searchinput = request.GET.get('searchinput')
    search = movie.search(searchinput)

    srchobjmovie = []
    for res in search:
        if res:
            srchobjmovie.append(res)
        else:
            pass


    show = tv.search('Breaking Bad')
    srchobjtv = []
    for result in show:
        if result:
            srchobjtv.append(result)
        else:
            pass

    srchobj = []
    for i in srchobjmovie:
        srchobj.append(i)
    for i in srchobjtv:
        srchobj.append(i)

    context = {
        'srchobj': srchobj
    }
    return render(request, '../templates/Movies/search_details.html', context)
