from . import views
from django.urls import path, include

urlpatterns = [
    path('movie/',include('movie.urls')),
    path('register', views.registration,name='reg'),
    path('login',views.login,name='signin'),
]