from django.db import models
from django.conf import settings

class Genre(models.Model):
  genre = models.CharField(max_length=20)

class Nation(models.Model):
  nation = models.CharField(max_length=20)

class Director(models.Model):
  director = models.CharField(max_length=20)

class Actor(models.Model):
  actor = models.CharField(max_length=20)
 
class Movie(models.Model):
  movieNm = models.CharField(max_length=100)
  movieNmEn = models.CharField(max_length=100)
  showTm = models.IntegerField()
  prdtYear = models.IntegerField()
  directors = models.ManyToManyField(Director)
  actors = models.ManyToManyField(Actor)
  nations = models.ManyToManyField(Nation)
  genres = models.ManyToManyField(Genre)

class Tmdb_Movie(models.Model):
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  adult = models.BooleanField()
  vote_average = models.FloatField()
  overview = models.TextField()
  poster_path = models.TextField(null=True)
  # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

class Comment(models.Model):
  movie = models.ForeignKey(Tmdb_Movie, on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')
  