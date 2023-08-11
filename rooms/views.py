from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from django.http import HttpResponseRedirect
from .models import Room, Message
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .forms import RoomForm
import typing
from transformers import pipeline

User=get_user_model()

import transformers

from transformers import pipeline

def recommend_genres_for_movie(movie_title):
    nlp = pipeline("zero-shot-classification",model='roberta-large-mnli')

    genres = ["Action", "Comedy", "Drama", "Horror", "Romance", "Science Fiction",'Crime','Detective','Thriller','Fantasy','Political Fiction']
    recommended_genre=[]

    for x in movie_title:
        prompt = f"Which genre does the movie '{x}' belong to: {', '.join(genres)}?"
        genre_result = nlp(prompt, genres)

        for i in range(0,2):
            if genre_result["labels"][i] not in recommended_genre:
                recommended_genre.append(genre_result['labels'][i])

    return recommended_genre

# Create your views here.
@login_required(login_url='/login')
def home(request):
    user=request.user
    books=str(user.fav_books)
    books=list(books.split(','))
    temp=recommend_genres_for_movie(books)
    q=request.GET.get('q') if request.GET.get('q')!=None else ''

    rooms=Room.objects.filter(
        Q(name__icontains=q)
    )

    recommend=[]

    for x in rooms:
        if(x.name in temp):
            recommend.append(x)
    room_count=rooms.count()
    context={
        "rooms":rooms,
        'recommends':recommend,
        'user':user
    }
    return render(request,'rooms/home.html',context=context)

@csrf_protect
@login_required(login_url='/login/')
def room(request,pk,*args,**kwargs):
    room=Room.objects.get(id=pk)
    room_messages=room.message_set.all()
    participants=room.participants.all()
    if request.method=='POST':
        message=Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room',pk=room.id)

    context={
        'enter_user':request.user,
        'room':room,
        'room_messages':room_messages,
        'participants':participants
    }

    return render(request, 'rooms/room.html', context=context)

@login_required(login_url='/login')
@csrf_protect
def createRoom(request):
    superuser=User.objects.filter(is_superuser=True)
    form=RoomForm(request.POST)
    context={
        'form':form,
    }
    if request.user in superuser:
        if request.method=='POST':
            Room.objects.create(
                name=request.POST.get('name')
            )
            return redirect('home')
    else:
        context['error']=True
    return render(request,'rooms/create.html',context=context)

@login_required(login_url='/login/')
@csrf_protect
def deleteMessage(request,rm,pk):
    message=Message.objects.get(id=pk)
    if request.user!=message.user:
        return HttpResponse("You are not allowed here!!")
    
    if request.method=='POST':
        if request.POST.get('yes'):
            message.delete()
        return redirect('room',pk=rm)
    
    return render(request,'rooms/delete.html',{'obj':message})

