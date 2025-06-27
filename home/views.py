from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm

def index(request):
    return render(request, 'home/index.html')

def films(request):
    template_data = {}
    template_data['title'] = 'Movies'
    template_data['movies'] = Movie.objects.all()
    return render(request, 'home/films.html', {'template_data': template_data})

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('films')
    else:
        form = MovieForm()
    
    return redirect('films')

def reviews(request):
    return render(request, 'reviews.html')

def best_movies(request):
    return render(request, 'home/best_movies.html')

# Buttons description and review
def movie_description(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    return render(request, 'movie_details.html', {'movie': movie})

def movie_reviews(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.reviews.all()  # related_name='reviews'

    return render(request, 'movie_reviews.html', {
        'movie': movie,
        'reviews': reviews,
    })

