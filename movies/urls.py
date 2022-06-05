from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_movies, name='movies'),
    path('<slug:slug>', views.movie_detail, name='movie_detail')
]
