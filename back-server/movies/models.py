from django.db import models

# TMDB 데이터
 
class Movie(models.Model):
  movieNm = models.CharField(max_length=100)
  movieNmEn = models.CharField(max_length=100)
  showTm = models.IntegerField()
  prdtYear = models.IntegerField()
  nations = models.TextField()
  genres = models.TextField()
  directors = models.TextField()
  actors = models.TextField()

class Tmdb_Movie(models.Model):
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  adult = models.BooleanField()
  vote_average = models.FloatField()
  overview = models.TextField()
  poster_path = models.TextField(null=True)

class Comment(models.Model):
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  