from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginUserForms
def login_request(request):
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method=='POST':
        form=LoginUserForms(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
              login(request,user)
              return redirect("index")
            else:
                return render(request,"account/login.html",{"form":form})
        else:
            return render(request,"account/login.html",{"form":form})
    else:
        form=LoginUserForms()
        return render(request,"account/login.html",{"form":form})
    
           
def register_request(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        repassword=request.POST['password2']
        email=request.POST['email']
    
        if password==repassword:
            if User.objects.filter(username=username).exists():
                return render(request,"account/register.html",{"error":"aynı isimden var"})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request,"account/register.html",{"error":"aynı mailden var"})
                else:
                    user= User.objects.create_superuser(username=username,email=email,password=password)
                    user.save()
                    return redirect("login")
        else:
         return render(request,"account/register.html",{"error":"sifreler ayni"})


    else:
       return render(request,"account/register.html")

def logout_request(request):
    messages.error(request,"uygulamadan çıkıldı")
    logout(request)
    return render(request,"account/login.html")