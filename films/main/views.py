from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from typing import Any
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views import View

from main.models import *
from main.forms import *
from main.utils import *


def logout_user(request):
    logout(request)
    return redirect('autorization')

class Register(CreateView):
    form_class = Register_form
    template_name = 'main/register.html'
    success_url = reverse_lazy('autorization')

    def get_context_object_name(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['auth'] = False
        return context
    

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/auth.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_success_url(self):
        return reverse_lazy('main')


class Main(View):
    context = {'form': Search_vid()}
    template_name = 'main/main.html'

    def get(self, request, *args, **kwargs):
        self.context['films_env'] = Films.objects.all()
        return render(request, self.template_name, self.context)
    
    def post(self, request, *args, **kwargs):
        self.context['form'] = Search_vid(request.POST)
        self.context['films_env'] = Films.objects.filter(name__contains=request.POST['name'])
        return render(request, self.template_name, self.context)


class Films_f(FilmsMixin, ListView):
    model = Films
    template_name = 'main/main.html'
    context_object_name = 'films_env'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Films.objects.filter(category='Фильм')


class Series(FilmsMixin, ListView):
    model = Films
    template_name = 'main/main.html'
    context_object_name = 'films_env'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Films.objects.filter(category='Сериал')


class Tv(FilmsMixin, ListView):
    model = Films
    template_name = 'main/main.html'
    context_object_name = 'films_env'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Films.objects.filter(category='Тв')


class Film(DetailView):
    model = Films
    template_name = 'main/film.html'
    pk_url_kwarg = 'film_pk'
    context_object_name = 'film_data'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddComment()
        context['comments'] = Comments.objects.filter(key=context['film_data'])
        return context

    def post(self, request, *args, **kwargs):
        film_pk = self.model.objects.get(pk=kwargs.get('film_pk'))
        text = request.POST['text']
        c = Comments.objects.create(text=request.POST['text'], key=Films.objects.get(pk=kwargs.get('film_pk')))
        return redirect('/film/' + str(kwargs.get('film_pk')) + '/')
