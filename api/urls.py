
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('all-movies', views.AllMovies.as_view(),name='all-movies'),
    path('movie/<int:pk>', views.Movies.as_view(),name='movies'),
]
