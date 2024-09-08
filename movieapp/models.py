from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
	Movie_Genres = [
        ('Action', 'Action'),
        ('Drama', 'Drama'),
        ('Romance', 'Romance'),
        ('Comedy', 'Comedy'),
        ('Horror', 'Horror'),
    ]
	  
	movie_name =models.CharField(max_length=100)
	movie_description = models.TextField()
	movie_image = models.CharField(max_length=500)
	price = models.IntegerField()
	genres = models.CharField(max_length=7, choices=Movie_Genres)
	
	def __str__(self):
		return self.movie_name
	
