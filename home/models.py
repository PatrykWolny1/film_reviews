from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='static/css/img/')

    def __str__(self):
        return str(self.id) + ' - ' + self.name

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')  # use this
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()

    def __str__(self):
        return f"{self.id} - {self.user.username} - {self.movie.name}"

    @property
    def image(self):
        return self.movie.image