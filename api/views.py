from rest_framework.response import Response
from django.shortcuts import render
from .models import WatchList,StreamPlatform
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import WatchListSerializer,StreamPlatformSerializer


# For WatchList Table
class All_WatchList(APIView):
    def get(self, request, format=None):
        movies=WatchList.objects.all()
        serializer=WatchListSerializer(movies,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchListItem(APIView):
    def get(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        serializer=WatchListSerializer(movie)
        return Response(serializer.data)
    
    def put(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        serializer=WatchListSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        movie.delete()
        return Response({'msg':"Data Deleted Suceefully"})

# For StreamPlatform Table

class All_Strame(APIView):

    def get(self,request):
       allstream= StreamPlatform.objects.all()
       serializer=StreamPlatformSerializer(allstream,many=True)
       return Response(serializer.data)
    
    def post(self,request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class StreamItem(APIView):

    def get(self,request,pk):
        getStream=StreamPlatform.objects.get(pk=pk)
        serializer=StreamPlatformSerializer(getStream)
        return Response(serializer.data)
    
    def put(self,request,pk):
        getStream=StreamPlatform.objects.get(pk=pk)
        serializer=StreamPlatformSerializer(getStream,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request,pk):
        getStream=StreamPlatform.objects.get(pk=pk)
        getStream.delete()
        return Response({'Msg':"Massage Deleted Sucessfully"})