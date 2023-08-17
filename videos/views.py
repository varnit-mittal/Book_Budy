from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your views here.

@login_required(login_url='/login')
def lobby(request):
    context={}
    user=User.objects.get(username=request.user)
    if (user.payment==False):
        context['error']=True
    return render(request,'video/lobby.html',context=context)


@login_required(login_url='/login')
def room(request):
    context={}
    user=User.objects.get(username=request.user)
    if (user.payment==False):
        context['error']=True
    return render(request,'video/room.html',context=context)    