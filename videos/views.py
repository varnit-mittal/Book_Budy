from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
import random
import time
import json
from .models import Channel,roomMember
from django.views.decorators.csrf import csrf_exempt

User=get_user_model()

# Create your views here.

def getToken(request):
    appId='4327bff84d2f4b8bab98d752f8c1aae9'
    appCertificate='a27e644e085d440f9a8cd585e669a072'
    channelName= request.GET.get('channel')
    uid=random.randint(1,230)
    expireTS=3600*24*60
    curr=time.time()
    privilegeExpiredTs=curr+expireTS
    role=1
    Newuser=str(request.user)
    token=RtcTokenBuilder.buildTokenWithUid(appId=appId,appCertificate=appCertificate,channelName=channelName,uid=uid,role=role,privilegeExpiredTs=privilegeExpiredTs)
    Channel.objects.create(name=channelName,token=token,uid=uid)
    return JsonResponse({'token':token,'uid':uid,'user':Newuser},safe=False)

def getCreds(request):
    channelName=request.GET.get('channel')
    obj=Channel.objects.get(name=channelName)
    appId='4327bff84d2f4b8bab98d752f8c1aae9'
    appCertificate='a27e644e085d440f9a8cd585e669a072'
    uid=random.randint(1,230)
    expireTS=3600*24*60
    curr=time.time()
    privilegeExpiredTs=curr+expireTS
    role=1
    token=RtcTokenBuilder.buildTokenWithUid(appId=appId,appCertificate=appCertificate,channelName=channelName,uid=uid,role=role,privilegeExpiredTs=privilegeExpiredTs)
    user=str(request.user)
    return JsonResponse({'name':obj.name,'token':token,'uid':uid,'Newuser':user},safe=False)


@login_required(login_url='/login')
def lobby(request):
    context={}
    rooms=list(Channel.objects.all())
    context['rooms']=rooms
    uid=random.randint(1,230)
    user=User.objects.get(username=request.user)
    context['diff_uid']=uid
    if (user.payment==False):
        context['error']=True
    return render(request,'video/lobby.html',context=context)


@login_required(login_url='/login')
def room(request):
    context={}
    context['user']=request.user
    user=User.objects.get(username=request.user)
    if (user.payment==False):
        context['error']=True
    return render(request,'video/room.html',context=context)

@login_required(login_url='/login')
def create(request):
    context={}
    user=User.objects.get(username=request.user)
    if (user.payment==False):
        context['error']=True
    return render(request,'video/create.html',context=context)


@csrf_exempt
def createMember(request):
    data=json.loads(request.body)
    member,created=roomMember.objects.get_or_create(
        name=data['user'],
        uid=data['uid'],
        room_name=data['channelName']
    )
    return JsonResponse({'name':data['user']}, safe=False)

def getMember(request):
    uid=request.GET.get('uid')
    room_name=request.GET.get('room_name')

    member= roomMember.objects.get(
        uid=uid,
        room_name=room_name
    )
    return JsonResponse({'name':member.name},safe=False)

@csrf_exempt
def deleteMember(request):
    data=json.loads(request.body)
    member= roomMember.objects.get(
        name=data['user'],
        uid=data['uid'],
        room_name=data['room_name']
    )

    member.delete()
    return JsonResponse('Member was deleted', safe=False)