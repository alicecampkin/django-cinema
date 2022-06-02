from django.contrib import admin

from .models import Movie, Genre


class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "release_date", "active", "deleted", "api_id"]


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
