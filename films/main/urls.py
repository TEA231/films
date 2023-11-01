from django.urls import path 

from main.views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('authorization/', auth, name='autorization'),
    path('', Main.as_view(), name='main'),
    path('films/', Films_f.as_view(), name='films'),
    path('series/', Series.as_view(), name='series'),
    path('tv/', Tv.as_view(), name='tv'),
    path('film/<int:film_pk>/', Film.as_view(), name='film')
]
