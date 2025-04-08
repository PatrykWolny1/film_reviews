from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def films(request):
    return render(request, 'home/films.html')

def reviews(request):
    return render(request, 'home/reviews.html')

def best_movies(request):
    return render(request, 'home/best_movies.html')