from django.contrib import admin
from .models import Movie, Review

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']

admin.site.register(Movie, MovieAdmin)

class ReviewAdmin(admin.ModelAdmin):
    ordering = ['add_date']
    search_fields = ['name']

admin.site.register(Review, ReviewAdmin)