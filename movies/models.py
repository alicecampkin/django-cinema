from django.db import models
from autoslug import AutoSlugField


class Genre(models.Model):
    name = models.CharField(max_length=100)
    api_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):

    api_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    slug = AutoSlugField(
        populate_from='title',
        editable=True,
        always_update=True,
        unique=True
    )

    overview = models.TextField(blank=True, null=True)

    popularity = models.FloatField(blank=True, null=True)

    poster_path = models.CharField(max_length=255, blank=True, null=True)
    backdrop_path = models.CharField(max_length=255, blank=True, null=True)

    release_date = models.DateField()
    added = models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    genres = models.ManyToManyField(
        to=Genre, related_name="movies", blank=True
    )

    def __str__(self):
        return self.title
