from django.shortcuts import render
from django.db.models.functions import Concat
from django.db.models import F, Value
from .models import Movie

# Create your views here.


def list_movies(request):

    movies = Movie.objects.all().order_by("-popularity").annotate(
        thumbnail_url=Concat(
            Value("https://image.tmdb.org/t/p/w500"), F("poster_path"))
    )

    context = {
        "movies": movies
    }

    return render(request, "movies/list_movies.html", context)


def movie_detail(request, slug):
    movie = Movie.objects.get(slug=slug)

    backdrop_path = f"https://image.tmdb.org/t/p/original{movie.backdrop_path}"
    poster_path = f"https://image.tmdb.org/t/p/w500{movie.poster_path}"

    context = {
        "movie": movie,
        "backdrop": backdrop_path,
        "poster_path": poster_path
    }

    return render(request, "movies/movie_detail.html", context)