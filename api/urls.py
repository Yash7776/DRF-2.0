
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # For Watchlist Table
    path('all-watchlist', views.All_WatchList.as_view(),name='all-watchlist'),
    path('watchlist-item/<int:pk>', views.WatchListItem.as_view(),name='watchlist-item'),
    # For StreamPlatfrom Table
    path('all-stream', views.All_Strame.as_view(),name='all-stream'),
    path('stream-item/<int:pk>', views.StreamItem.as_view(),name='stream-item'),
    
]
