from django.http import HttpResponse
from django.shortcuts import render

def register(request):
    return render(request, 'main/register.html')

def main(request):
    return render(request, 'main/main.html')
