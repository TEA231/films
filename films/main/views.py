from django.http import HttpResponse
from django.shortcuts import render

def register(request):
    return HttpResponse('Страница регистрации')

def main(request):
    return HttpResponse('Главная страница')
