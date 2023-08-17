from django.urls import path
from . import views

urlpatterns=[
    path('video/lobby',views.lobby,name='lobby'),
    path('video/lobby/room',views.room,name='video_room'),
]