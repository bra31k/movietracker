from rest_framework import serializers

from .models import Film


class FilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = ('genres', 'id_movie', 'original_title', 'poster_path', 'production_countries', 'release_date')