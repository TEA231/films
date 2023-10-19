from django.http import HttpResponse
from django.shortcuts import render

from main.models import *

context = {
    'auth': False
}

def register(request):
    return render(request, 'main/register.html', context=context)

def main(request):
    context['films_env'] = Films.objects.filter(category='Фильм')
    return render(request, 'main/main.html', context=context)

def auth(request):
    return render(request, 'main/auth.html', context=context)

def history(request):
    return render(request, 'main/history.html', context=context)

def film(request, film_pk):
    context['film_data'] =  Films.objects.get(pk=film_pk)
    return render(request, 'main/film.html', context=context)
