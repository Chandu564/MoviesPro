from . import views
from django.urls import path,include
#app_name='Movie'
urlpatterns = [
    path('',views.homepage,name='movie'),
    path('<int:mid>',views.movie_id,name='movie_id'),
    path('logout',views.logout,name='logout'),
    path('add',views.add_movie,name='add_movie'),
    path('api/mvs',views.get_all_movies,name='allmovies'),
    path('api/<int:id>',views.get_one_movie_by_id,name='onemovie')
]