from django.db import models
from django.conf import settings
from django_random_queryset import RandomManager


class Genre(models.Model):
  genre = models.CharField(max_length=20)

  def __str__(self):
    return self.genre

class Nation(models.Model):
  nation = models.CharField(max_length=20)

  def __str__(self):
    return self.nation

class Director(models.Model):
  director = models.CharField(max_length=20)

  def __str__(self):
    return self.director

class Actor(models.Model):
  actor = models.CharField(max_length=20)

  def __str__(self):
    return self.actor
 
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
  wantlist = models.ManyToManyField(settings.AUTH_USER_MODEL)

class Comment(models.Model):
  movie = models.ForeignKey(Tmdb_Movie, on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')
  author = models.CharField(max_length=20)

class award_Movie(models.Model):
  titel = models.CharField(max_length=50)
  adult = models.BooleanField()
  vote_average = models.FloatField()
  overview =  models.TextField()
  poster_path = poster_path = models.TextField(null=True)
  release_date = models.CharField(max_length=4)
  festival_name = models.CharField(max_length=20)
  objects = RandomManager()