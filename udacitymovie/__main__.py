"""create movies webpage from command line"""
from . import fresh_tomatoes
from . import media
from . import movie_listing

if __name__ == '__main__':
    movies = [media.Movie(**movie) for movie in movie_listing]
    fresh_tomatoes.open_movies_page(movies)

