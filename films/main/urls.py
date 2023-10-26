from django.urls import path 

from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('films/', films, name='films'),
    path('series/', series, name='series'),
    path('tv/', tv, name='tv'),
    path('authorization/', auth, name='autorization'),
    path('', main, name='main'),
    path('film/<int:film_pk>/', film, name='film')
]  

