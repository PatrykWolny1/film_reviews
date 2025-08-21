from django.contrib import admin
from django.db.models import Avg, Count
from .models import Movie, Review


class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']                     # keep your ordering
    search_fields = ['name']                # keep your search
    list_display = ('id', 'name', 'avg_rating', 'ratings_count', 'add_date')
    list_per_page = 25

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # annotate once so list_display can use the values without extra queries
        return qs.annotate(_avg=Avg('reviews__rating'), _cnt=Count('reviews__rating'))

    def avg_rating(self, obj):
        val = getattr(obj, '_avg', 0) or 0
        return f"{val:.2f}"
    avg_rating.short_description = 'Avg rating'
    avg_rating.admin_order_field = '_avg'

    def ratings_count(self, obj):
        return getattr(obj, '_cnt', 0)
    ratings_count.short_description = '# ratings'
    ratings_count.admin_order_field = '_cnt'


admin.site.register(Movie, MovieAdmin)


class ReviewAdmin(admin.ModelAdmin):
    # use newest first; change to ['add_date'] if you truly want ascending
    ordering = ['-add_date']
    # your previous 'name' doesn't exist on Review; use these instead:
    search_fields = ['movie__name', 'user__username', 'review']
    list_display = ('id', 'movie', 'user', 'rating', 'short_review', 'add_date')
    list_filter = ('rating', 'add_date', 'movie')
    list_select_related = ('movie', 'user')
    autocomplete_fields = ('movie', 'user')  # nice UX when you have many rows
    list_per_page = 25

    def short_review(self, obj):
        text = obj.review or ''
        return (text[:60] + '…') if len(text) > 60 else text
    short_review.short_description = 'Review (preview)'


admin.site.register(Review, ReviewAdmin)
