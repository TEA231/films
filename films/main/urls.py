from django.urls import path 

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('films/', views.Films_f.as_view(), name='films'),
    path('series/', views.Series.as_view(), name='series'),
    path('tv/', views.Tv.as_view(), name='tv'),
    path('authorization/', views.auth, name='autorization'),
    path('', views.Main.as_view(), name='main'),
    path('film/<int:film_pk>/', views.Film.as_view(), name='film')
]
