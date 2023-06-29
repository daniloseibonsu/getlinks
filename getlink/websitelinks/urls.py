from django.urls  import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("websites", views.websites, name="websites"),
    path("movies", views.movies, name="movies"),
    path("music", views.music, name="music"),
    path("games", views.games, name="games"),
    path("images", views.images, name="images"),
    path("animes", views.animes, name="animes"),
    path("animessearch", views.animessearch, name="animessearch")
]