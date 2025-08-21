from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Review
from .forms import MovieForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Avg, Count

def index(request):
    return render(request, 'home/index.html')

def films(request):
    movies_qs = (
        Movie.objects
        .annotate(
            avg_rating=Avg('reviews__rating'),
            reviews_count=Count('reviews__rating')
        )
        .order_by('-add_date')
    )
    paginator = Paginator(movies_qs, 7)
    page_number = request.GET.get('page')
    movies = paginator.get_page(page_number)

    return render(request, 'home/films.html', {
        'title': 'Movies',
        'movies': movies,
    })

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('films')
    else:
        form = MovieForm()
    
    return redirect('films')
    
@login_required
def add_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user  # preferred
            # If you still have a `name` field:
            if hasattr(obj, "name") and not obj.name:
                obj.name = request.user.username
            obj.save()
            return redirect("reviews")
    else:
        form = ReviewForm()
        # If the form still includes 'name', set it (and it’s HiddenInput anyway)
        if "name" in form.fields:
            form.fields["name"].initial = request.user.username

    return redirect('reviews')


def reviews(request):
    movies = Movie.objects.all().order_by("name")
    reviews = (Review.objects
            .select_related("movie", "user")  
            .order_by("-add_date")) 
    paginator = Paginator(reviews, 4)  # 4 reviews per page
    page_number = request.GET.get('page')
    reviews = paginator.get_page(page_number)
          
    return render(request, 'home/reviews.html', {'movies' : movies, 'reviews' : reviews})

def best_movies(request):
    return render(request, 'home/best_movies.html')

# Buttons description and review
def movie_description(request, movie_id):
    movie = (
        Movie.objects
        .annotate(
            avg_rating=Avg('reviews__rating'),
            reviews_count=Count('reviews__rating')
        )
        .get(id=movie_id)
    )
    return render(request, 'home/movie_description.html', {'movie': movie})

def movie_reviews(request, movie_id):
    movie = (
        Movie.objects
        .annotate(
            avg_rating=Avg('reviews__rating'),
            reviews_count=Count('reviews__rating')
        )
        .get(id=movie_id)
    )
    reviews = movie.reviews.all().order_by("-add_date")  # newest first
    return render(request, "home/movie_reviews.html", {"movie": movie, "reviews": reviews})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # auto login after signup
            return redirect('films')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # auto login after signup
            return redirect('films')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def best_movies(request):
    movies = (
        Movie.objects
        .annotate(
            avg_rating=Avg('reviews__rating'),
            review_count=Count('reviews')
        )
        .filter(review_count__gt=0)  # only movies with reviews
        .order_by('-avg_rating', '-review_count')[:5]  # top 5
    )
    return render(request, 'home/best_movies.html', {'movies': movies})