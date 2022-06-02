import requests
import logging

from typing import List

from datetime import datetime

from .the_movie_db_api import Endpoint
from .models import Genre, Movie


def fetch_genres() -> None:
    response = requests.get(Endpoint.GET_GENRES)

    data = response.json()
    genres = data["genres"]

    for genre in genres:
        obj, created = Genre.objects.get_or_create(
            api_id=genre["id"],
            name=genre["name"]
        )
        if created:
            logging.info(f"Added Genre: {obj.name} ({obj.api_id})")


def fetch_movies() -> None:

    # first check our genres are up to date:
    fetch_genres()

    # Get movie data
    response = requests.get(Endpoint.GET_MOVIES)
    data = response.json()

    movies: List[dict] = data["results"]

    for movie in movies:
        obj, created = Movie.objects.get_or_create(
            api_id=movie["id"],
            title=movie["title"]
        )

        obj.poster_path = movie.get("poster_path", None)
        obj.backdrop_path = movie.get("backdrop_path", None)
        obj.release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")
        obj.popularity = movie.get("popularity", None)
        obj.overview = movie.get("overview", None)

        obj.save()

        genres = Genre.objects.filter(api_id__in=movie["genres"])

        for genre in genres:
            obj.genres.add(genre)
