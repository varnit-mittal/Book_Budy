from django.urls import path, include
from . import views

urlpatterns=[
    path('books/home/',views.home,name='home'),
    path('books/room/<str:pk>/',views.room,name='room'),
    path('books/create/',views.createRoom,name='create'),
    path('books/delete/<str:rm>/<str:pk>/',views.deleteMessage,name='message_delete'),
]