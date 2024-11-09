from django.db import models
from django.utils import timezone



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
    # image = models.ImageField()


    class Meta:
        db_table = 'movies'

    def __str__(self):
        return self.title