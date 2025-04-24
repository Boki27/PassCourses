from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

# Create your views here.


def index(request):
    movies = Movie.objects.all()

    # select from movies_movie
    # Movie.objects.filter(release_year=1986)
    # select from movies_move where realease year equals 1986
    # Movie.objects.get(id=1)
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
