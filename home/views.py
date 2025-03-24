from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def films(request):
    return render(request, 'home/films.html')