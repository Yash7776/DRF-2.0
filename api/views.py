from rest_framework.response import Response
from django.shortcuts import render
from .models import Movie
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import MovieSerializer



class AllMovies(APIView):
    def get(self, request, format=None):
        print("movies")
        movies=Movie.objects.all()
        print(movies)
        serializer=MovieSerializer(movies,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



class Movies(APIView):
    def get(self,request,pk):
        movie=Movie.objects.get(pk=pk)
        serializer=MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self,request,pk):
        movie=Movie.objects.get(pk=pk)
        serializer=MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        movie=Movie.objects.get(pk=pk)
        movie.delete()
        return Response({'msg':"Data Deleted Suceefully"})


