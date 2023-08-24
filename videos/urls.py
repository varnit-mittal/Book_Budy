from django.urls import path
from . import views

urlpatterns=[
    path('video/lobby',views.lobby,name='lobby'),
    path('video/lobby/room',views.room,name='video_room'),
    path('video/get_token/',views.getToken,name='token'),
    path('video/get_creds/',views.getCreds,name='creds'),
    path('video/create',views.create,name='video_create'),
    path('video/create_member/',views.createMember,name='create_member'),
    path('video/get_member/',views.getMember),
    path('video/delete_member/',views.deleteMember),
]