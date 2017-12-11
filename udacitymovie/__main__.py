import fresh_tomatoes
import media
from movie_listing import movie_listing

if __name__ == '__main__':
    movies = [media.Movie(**movie) for movie in movie_listing]
    fresh_tomatoes.open_movies_page(movies)

