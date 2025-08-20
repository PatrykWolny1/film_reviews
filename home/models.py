from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from django.utils import timezone

from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg, Count, Q
from django.utils import timezone

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='movies_imgs/')
    add_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.id} - {self.name}"

    # Live-computed averages (simple & safe)
    @property
    def average_rating(self):
        return self.reviews.aggregate(avg=Avg('rating'))['avg'] or 0

    @property
    def ratings_count(self):
        return self.reviews.aggregate(c=Count('rating'))['c'] or 0


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews',
        null=True, blank=True,
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True, blank=True,   # ← temporarily allow nulls
        help_text="1–5"
    )
    add_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-add_date']
        constraints = [
            # Ensure rating is 1..5 at the DB level too
            models.CheckConstraint(
                check=Q(rating__gte=1) & Q(rating__lte=5),
                name='review_rating_between_1_and_5',
            ),
            # At most one review per (user, movie); allow multiple if user is NULL (guests)
            models.UniqueConstraint(
                fields=['user', 'movie'],
                name='unique_review_per_user_movie',
                condition=Q(user__isnull=False),
            ),
        ]

    def __str__(self):
        user_part = getattr(self.user, 'username', 'Anonymous')
        return f"{self.id} - {user_part} - {self.movie.name}"

    @property
    def image(self):
        return self.movie.image

