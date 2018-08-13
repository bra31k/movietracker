import csv, sys, os

project_dir = "movietracker"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from movies.models import Film

data = csv.reader(open('movies_metadata.csv', encoding='utf-8'),delimiter=",")

for row in data:
    if row[0] != 'adult':
        film = Film()
        print(len(row))
        if 3 <= len(row):
            film.genres = row[3]
        else:
            continue
        if 5 <= len(row):
            film.id_movie = row[5]
        else:
            continue
        if 8 <= len(row):
            film.original_title = row[8]
        else:
            continue
        if 11 <= len(row):
            film.poster_path = row[11]
        else:
            continue
        if 13 <= len(row):
            film.production_countries = row[13]
        else:
            continue
        if 14 <= len(row):
            film.release_date = row[14]
        else:
            continue
        film.save()
