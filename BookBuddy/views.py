from django.http import HttpResponse
import random
from django.template.loader import render_to_string
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


def home_view(request,*args,**kwargs):
    return render(request,'landingPage/index.html',{})