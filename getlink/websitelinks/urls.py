from django.urls  import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("websites", views.websites, name="websites"),
    path("movies", views.movies, name="movies"),
    path("musics", views.musics, name="musics"),
    path("games", views.games, name="games"),
    path("images", views.images, name="images"),
    path("animes", views.animes, name="animes"),
    path("book", views.book, name="book"),
    path("check", views.check, name="check"),
    path("animessearch", views.animessearch, name="animessearch"),
    path("gamessearch", views.gamessearch, name="gamessearch"),
    path("moviessearch", views.moviessearch, name="moviessearch"),
    path("musicssearch", views.musicssearch, name="musicssearch"),
    path("imagessearch", views.imagessearch, name="imagessearch")
]