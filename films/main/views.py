from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from main.models import *
from main.forms import *

context_g = {
    'auth': False
}

def register(request):
    return render(request, 'main/register.html', context=context_g)

def auth(request):
    return render(request, 'main/auth.html', context=context_g)

class Main(ListView):
    model = Films
    template_name = 'main/main.html'
    context_object_name = 'films_env'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Search_vid()
        return context


#def main(request): 
#    context['form'] = Search_vid()
#    if request.method == 'POST':
#        context['films_env'] = Films.objects.filter(name=request.POST['name'])
#    else:
#        context['films_env'] = Films.objects.all()
#    return render(request, 'main/main.html', context=context)

class Films_f(ListView):
    model = Films
    template_name = 'main/main.html'
    context_object_name = 'films_env'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Search_vid()
        return context
    
    def get_queryset(self):
        return Films.objects.filter(category='Фильм')


class Series(ListView):
    model = Films
    template_name = 'main/main.html'
    context_object_name = 'films_env'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Search_vid()
        return context
    
    def get_queryset(self):
        return Films.objects.filter(category='Сериал')


class Tv(ListView):
    model = Films
    template_name = 'main/main.html'
    context_object_name = 'films_env'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Search_vid()
        return context
    
    def get_queryset(self):
        return Films.objects.filter(category='Тв')


def film(request, film_pk):
    if request.method == 'POST':
        c = Comments.objects.create(text=request.POST['text'], key=Films.objects.get(pk=film_pk))
    context_g['form'] = AddComment()
    context_g['film_data'] =  Films.objects.get(pk=film_pk)
    context_g['comments'] = Comments.objects.filter(key=context_g['film_data'])
    return render(request, 'main/film.html', context=context_g)