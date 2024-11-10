from django.db import models
from django.utils import timezone
from apps.user.models import User


class Genre(models.Model):
    title = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'genres'

    def __str__(self):
        return self.title



class Movie(models.Model):

    title = models.CharField(max_length=150)
    genre = models.ManyToManyField(Genre, related_name='movies')
    director = models.CharField(max_length=50)
    imdb_rating = models.FloatField()
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)


    class Meta:
        db_table = 'movies'

    def __str__(self):
        return self.title