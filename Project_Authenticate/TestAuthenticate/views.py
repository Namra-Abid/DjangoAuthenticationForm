from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import Custom_UserCreationForm
from django.contrib.auth import authenticate,login,logout
def home(request):
    return render(request, 'TestAuthenticate/home.html')

def register(request):
    #form=UserCreationForm
    form=Custom_UserCreationForm()
    if request.method=='POST':
        #form=UserCreationForm(request.POST)
        form=Custom_UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
           # print("****************",user)
            messages.success(request, 'Account created successfully for {}'.format(user) )
            return redirect('TestAuthenticate:loginpage')
    
    context={'formHtml':form}
    return render(request,'TestAuthenticate/register.html',context)

def login(request):
        #form = 'Namra'
        if request.method=="POST":
            name=request.POST.get('username')
            passw=request.POST.get('password')
            user=authenticate (request, username=name,password=passw)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request, 'Username Or Password is incorrect')
                
        context={}
        return render(request, 'TestAuthenticate/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('TestAuthenticate:login')
