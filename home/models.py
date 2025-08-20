from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from django.utils import timezone

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='movies_imgs/')  # ⚠️ better: use MEDIA, not static
    add_date = models.DateTimeField(default=timezone.now)  # auto-set when created

    def __str__(self):
        return f"{self.id} - {self.name}"


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
    add_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.id} - {self.user.username} - {self.movie.name}"

    @property
    def image(self):
        return self.movie.image
