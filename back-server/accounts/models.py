from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator


class User(AbstractUser):
  followings = models.ManyToManyField(
    'self', 
    symmetrical=False, 
    related_name='followers',
    default=[])

  def __str__(self):
    return self.username