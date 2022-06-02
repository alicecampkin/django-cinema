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

    featured_movie = movies.first()

    context = {
        "featured_movie": featured_movie,
        "featured_movie_image": f"https://image.tmdb.org/t/p/original{featured_movie.backdrop_path}",
        "movies": movies[1:]
    }

    return render(request, "list_movies.html", context)
