from django.http import HttpResponse
from django.shortcuts import render

context = {
    'auth': False
}

def register(request):
    return render(request, 'main/register.html', context=context)

def main(request):
    return render(request, 'main/main.html', context=context)

def auth(request):
    return render(request, 'main/auth.html', context=context)

def history(request):
    return render(request, 'main/history.html', context=context)
