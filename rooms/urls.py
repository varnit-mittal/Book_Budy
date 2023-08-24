from django.urls import path, include
from . import views
from django.views.decorators.cache import cache_page

urlpatterns=[
    path('books/home/',cache_page(2)(views.home),name='home'),
    path('books/room/<str:pk>/',views.room,name='room'),
    path('books/create/',views.createRoom,name='create'),
    path('books/delete/<str:rm>/<str:pk>/',views.deleteMessage,name='message_delete'),
]