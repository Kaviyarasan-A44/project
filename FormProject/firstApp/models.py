from django.db import models

class Movie(models.Model):
    release_date = models.DateField()
    movie_name = models.CharField(max_length=100)
    director_name = models.CharField(max_length=100)
    imdb_rating = models.IntegerField()
