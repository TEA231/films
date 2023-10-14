from django.http import HttpResponse
from django.shortcuts import render

def register(request):
    return render(request, 'main/register.html', {'auth': False})

def main(request):
    return render(request, 'main/main.html', {'auth': False})

def auth(request):
    return render(request, 'main/auth.html', {'auth': False})

def history(request):
    return render(request, 'main/history.html', {'auth': False})
