from django.urls import path 

from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('', main, name='main'),
    path('authorization/', auth, name='autorization'),
    path('history/', history, name='history'),
    path('film/<int:film_pk>/', film, name='film')
]

    