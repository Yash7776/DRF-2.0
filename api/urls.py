
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('all-watchlist', views.All_WatchList.as_view(),name='all-watchlist'),
    path('watchlist-item/<int:pk>', views.WatchListItem.as_view(),name='watchlist-item'),
]
