from django.shortcuts import render
from .forms import SignupForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    form=SignupForm(request.POST or None, request.FILES or None)
    # form=UserCreationForm()
    context={
        'form':form,
    }
    if(request.method=='POST'):
        print(1)
        if form.is_valid():
            user_obj=form.save()
            return redirect('/login')
        
    return render(request,'accounts/signup.html',context=context)
        
@csrf_protect
def login_view(request):
    form=AuthenticationForm(request,data=request.POST)
    context={
        'form':form
    }
    if(request.method=="POST"):
        if form.is_valid():
            user=form.get_user()
            context['success']=True
            login(request,user)
            return redirect('/')
    return render(request,'accounts/login.html',context=context)

def logout_view(request):
    context={}
    if(request.method=="POST"):
        logout(request)
        return redirect('/login')
    return render(request,'accounts/logout.html',context=context)

@login_required(login_url='/login')
def profile_view(request):
    
    return render(request,'accounts/profile.html',context={})