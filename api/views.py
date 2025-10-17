from rest_framework.response import Response
from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.decorators import api_view


@api_view()
def all_movies(request):
    movies=Movie.objects.all()
    serializer=MovieSerializer(movies,many=True)
    return Response(serializer.data)

@api_view()
def movie(request,pk):
    movie=Movie.objects.get(pk=pk)
    serializer=MovieSerializer(movie)
    return Response(serializer.data)