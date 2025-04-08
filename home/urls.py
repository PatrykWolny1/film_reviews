from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home.index'),
    path('films/', views.films, name='home.films'),
    path('reviews/', views.reviews, name='home.reviews'),
    path('best_movies/', views.best_movies, name='home.best_movies'),
]