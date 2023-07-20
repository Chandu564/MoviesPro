from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from . models import Movie
from movie.movieform import MovieForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .movieSerializer import MovieSerializerClass
def homepage(request):
    movies=Movie.objects.all()

    return render(request,'index.html',{'movies':movies})
def movie_id(request,mid):
    movie=Movie.objects.filter(id=mid)[0]
    print(type(movie))
    if movie:
        mvs=request.session.setdefault('recent_movies',{})
        mvs[movie.id]=movie.title
        request.session['recent_movies']=mvs
        return render(request,'movie_details.html',{'movie':movie})
def logout(request):
    auth.logout(request)
    return redirect('/')
def add_movie(request):
    if request.method=='POST':
        form=MovieForm(request.POST,request.FILES)
        print('files ',request.POST,request.FILES)
        print('end of print')
        if form.is_valid():
            form.save()
            return redirect('movie')
        else:
            messages.info(request,'Error while creating Movie ')
            return redirect('add_movie')
    else:
        return render(request,'movieForm.html',{'form':MovieForm()})
@api_view(['GET'])
def get_all_movies(request):
    mvs=Movie.objects.all()
    serializer=MovieSerializerClass(mvs,many=True)
    return Response(serializer.data)
@api_view(['GEt'])
def get_one_movie(request,id):
    mvs=Movie.objects.filter(id=id)
    ser=MovieSerializerClass(mvs)
    return Response(ser.data)
# Create your views here.
