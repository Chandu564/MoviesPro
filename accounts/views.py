from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
def registration(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        password1=request.POST['password1']
        email=request.POST['email']
        if password==password1:
            if(not User.objects.filter(username=username).exists()):
                if(not User.objects.filter(email=email).exists()):
                    user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    print('user created')
                    return redirect('signin')
                else:
                    messages.info(request,'email exists')
                    return redirect('reg')
            else:
                messages.info(request, 'username exists')
                return redirect('reg')
        else:
            messages.info(request, 'Password not matched')
            return redirect('reg')
    else:
        return render(request,'register.html')
def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    else:
        uname=request.POST['username']
        pwd=request.POST['password']
        user=auth.authenticate(username=uname,password=pwd)
        if user:
            auth.login(request,user)
            return redirect('movie')
        else:
            messages.info(request,"Invaid Credentials")
            return redirect('signin')

# Create your views here.
