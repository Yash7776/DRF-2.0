
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('all-movies', views.all_movies,name='all-movies'),
    path('movie/<int:pk>', views.movie,name='movie'),
]
