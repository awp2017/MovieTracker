import csv
import pdb

from datetime import date, datetime
import json
from movie_tracker.models import *
import pandas as pd

MOVIES = 'tmdb-5000-movie-dataset/tmdb_5000_movies.csv'
CREDITS = 'tmdb-5000-movie-dataset/tmdb_5000_credits.csv'


def load_data():
    movies_data = pd.read_csv(MOVIES)

    # movies_data = decode_data(movies_data)

    movies = load_movies(movies_data)
    keywords = load_keywords(movies_data)

    credits = pd.read_csv(CREDITS)
    # credits = decode_data(credits)

    credits['id'] = credits['movie_id']
    movies_data = pd.merge(movies_data, credits, on = ['id', 'title'])

    actors = load_actors(movies_data)

    return pd.DataFrame({ 'movies': movies, 'keywords': keywords, 'actors': actors })


def decode_data(data):
    for k in data.select_dtypes(['object']).keys():
        data[k] = data[k].apply(lambda x: x.decode('utf-8').strip())

    return data


def load_keywords(movies):
    return movies['keywords'].apply(lambda row: json.loads(row))


def load_actors(movies):
    return movies['cast'].apply(lambda row: parse_actors(row))


def parse_actors(row):
    actors = json.loads(row)

    return [{ 'name': actor['name'], 'character': actor['character'] } for actor in actors]


def load_movies(movies):
    movies['genres'] = movies['genres'].apply(
        lambda row: ', '.join([genre['name'] for genre in json.loads(row)]))

    movies['release_date'] = movies['release_date'].dropna().apply(lambda row: format_date((row)))

    movies['movie'] = movies.apply(lambda row: {
        'id': row['id'],
        'title': row['title'],
        'release_date': row['release_date'],
        'runtime': row['runtime'],
        'overview': row['overview'],
        'tagline': row['tagline'],
        'budget': row['budget'],
        'genres': row['genres'],
    }, axis = 1)

    return movies['movie']


def format_date(raw_date):
    if raw_date == '':
        return None

    date = datetime.strptime(raw_date, '%Y-%m-%d')
    return date.date()


def create_objects(row):
    movie_data = row['movies']
    keywords_data = row['keywords']
    actors_data = row['actors']

    movie = Movie(**movie_data)
    movie.save()

    keywords = []
    for keyword_data in keywords_data:
        keywords.append(Keyword.objects.get_or_create(**keyword_data)[0])
    movie.keywords = keywords

    actors = []
    for actor_data in actors_data:
        actor = Actor.objects.get_or_create(name = actor_data['name'])[0]
        actors.append(actor)
        # ActorMovie(actor_id=actor.id, movie_id=movie.id, character=actor_data['character']).save()

    movie.actors = actors
    movie.save()


def main():
    data = load_data()[:500]
    for index, row in data.iterrows():
        print('start for {0}'.format(index))
        create_objects(row)


if __name__ == "__main__":
    main()
