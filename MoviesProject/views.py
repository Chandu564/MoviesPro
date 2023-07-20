from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
def main(request):
    return render(request,'home.html')