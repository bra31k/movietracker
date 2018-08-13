from django.db import models

class Film(models.Model):
    genres = models.CharField(max_length=999)
    id_movie = models.CharField(max_length=999)
    original_title = models.CharField(max_length=999)
    poster_path = models.CharField(max_length=999)
    production_countries = models.CharField(max_length=999)
    release_date = models.CharField(max_length=999)



# Create your models here.
