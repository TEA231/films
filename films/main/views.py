from django.http import HttpResponse
from django.shortcuts import render

from main.models import *
from main.forms import *

context = {
    'auth': False
}

def register(request):
    return render(request, 'main/register.html', context=context)

def auth(request):
    return render(request, 'main/auth.html', context=context)

def main(request):
    context['form'] = Search_vid()
    if request.method == 'POST':
        context['films_env'] = Films.objects.filter(name=request.POST['name'])
    else:
        context['films_env'] = Films.objects.all()
    return render(request, 'main/main.html', context=context)

def films(request):
    context['form'] = Search_vid()
    context['films_env'] = Films.objects.filter(category='Фильм')
    return render(request, 'main/main.html', context=context)

def series(request):
    context['form'] = Search_vid()
    context['films_env'] = Films.objects.filter(category='Сериал')
    return render(request, 'main/main.html', context=context)

def tv(request):
    context['form'] = Search_vid()
    context['films_env'] = Films.objects.filter(category='Тв')
    return render(request, 'main/main.html', context=context)

def film(request, film_pk):
    context['film_data'] =  Films.objects.get(pk=film_pk)
    context['comments'] = Comments.objects.filter(key=context['film_data'])
    return render(request, 'main/film.html', context=context)
