from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('films/', views.films, name='films'),
    path('films/add-movie/', views.add_movie, name='add_movie'),
    path('films/add-review/', views.add_review, name='add_review'),
    path('reviews/', views.reviews, name='reviews'),
    path('best_movies/', views.best_movies, name='best_movies'),
    path('movie/<int:movie_id>/description/', views.movie_description, name='movie_description'),
    path('movie/<int:movie_id>/reviews/', views.movie_reviews, name='movie_reviews'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)