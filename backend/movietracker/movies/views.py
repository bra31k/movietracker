from django.shortcuts import render

from rest_framework import viewsets

from .models import Film
from .serializers import FilmSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all().order_by('-release_date')[1:9]
    serializer_class = FilmSerializer
# Create your views here.
