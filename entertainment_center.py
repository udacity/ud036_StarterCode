import media
import fresh_tomatoes
'''
    This script produce movie site.
    Includes instances of the class Movie with movie data,
    list of movies that is used by fresh_tomatoes,
    function open_movies_page from fresh_tomatoes
    that creates html webpage with our movies.
'''
# Blade Runner 2049
blade_runner_2049 = media.Movie("BladeRunner2049",
                                "https://image.tmdb.org/t/p/w500/c0jCZGc0XMW1TpRP2nRCrwY3Tex.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=gCcx85zbxz4")
# Goodfellas
goodfellas = media.Movie("Goodfellas",
                         "https://image.tmdb.org/t/p/w500/pwpGfTImTGifEGgLb3s6LRPd4I6.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=qo5jJpHtI1Y")
# Godfather
godfather = media.Movie("The Godfather",
                        "https://image.tmdb.org/t/p/w500/rPdtLWNsZmAtoZl9PK7S2wE3qiS.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=w0VGcWHkNeA")
# Apocalypse Now
apocalypse_now = media.Movie("Apocalypse Now",
                             "https://image.tmdb.org/t/p/w500/jcvJ2xcVWU9Wh0hZAxcs103s8nN.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=IkrhkUeDCdQ")
# The Departed
departed = media.Movie("The Departed", "https://image.tmdb.org/t/p/w500/tGLO9zw5ZtCeyyEWgbYGgsFxC6i.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=n4O3x5BH18E")
# The Shawshank Redemption
shawshank = media.Movie("The Shawshank Redemption", "https://image.tmdb.org/t/p/w500/9O7gLzmreU0nGkIB6K3BsJbzvNv.jpg",   # NOQA
                        "https://www.youtube.com/watch?v=K_tLp7T6U1c")
# list of movies
movies = [blade_runner_2049, goodfellas, godfather,
          apocalypse_now, departed, shawshank]
# function from fresh_tomatoes for creating webpage
fresh_tomatoes.open_movies_page(movies)

