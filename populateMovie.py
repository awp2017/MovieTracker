import csv
import pdb

from datetime import date, datetime
import json
from movie_tracker.models import *


def load_data():
    movies = 'tmdb-5000-movie-dataset/tmdb_5000_movies.csv'
    credits = 'tmdb-5000-movie-dataset/tmdb_5000_credits.csv'
    with open(movies) as movie_file, open(credits) as credits_file:
        reader = csv.DictReader(movie_file)
        # title release data runtime genres budget keywords overview tagline
        return [(movie_dict(row), keywords(row)) for row in reader]


def movie_dict(row):
    return {
        'id': row['id'],
        'title': row['title'],
        'release_date': format_date(row['release_date']),
        'runtime': row['runtime'],
        'overview': row['overview'],
        'tagline': row['tagline'],
        'budget': row['budget'],
        'genres': extract_genres(row['genres']),
    }


def keywords(row):
    return json.loads(row['keywords'])


def format_date(raw_date):
    if raw_date == '':
        return None

    date = datetime.strptime(raw_date, '%Y-%m-%d')
    return date.date()


def extract_genres(data_json):
    genres = json.loads(data_json)

    return ', '.join([genre['name'] for genre in genres])


def main():
    for movie_data, keywords_data in load_data():
        movie = Movie(**movie_data)
        movie.save()

        keywords = []
        for keyword_data in keywords_data:
            keywords.append(Keyword.objects.get_or_create(**keyword_data)[0])
        movie.keywords = keywords
        print 'success'


if __name__ == "__main__":
    main()
