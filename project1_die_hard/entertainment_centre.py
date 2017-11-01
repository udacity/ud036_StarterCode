# import classes from other files #
import die_hard_movies
import media

# movie objects #
# Die Hard movie: movie title, poster image and movie trailer
die_hard = media.Movie(
    "Die Hard",
    "http://horrornews.net/wp-content/uploads/2016/09/Die-Hard-I-DVD.jpg",  # NOQA
    "https://www.youtube.com/watch?v=-qxBXm7ZUTM"
    )

# Die Harder movie: movie title, poster image and movie trailer
die_hard_2 = media.Movie(
    "Die Harder",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNzM1MzMwNzY2OF5BMl5BanBnXkFtZTgwNzE1MzkyMTE@._V1_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=OyxfXQ4MGLQ"
    )

# Die Hard with a Vengeance movie: movie title, poster image and movie trailer
die_hard_3 = media.Movie(
    "Die Hard with a Vengeance",
    "https://i.jeded.com/i/die-hard-3-die-hard-with-a-vengeance.15819.jpg",  # NOQA
    "https://www.youtube.com/watch?v=gQ0uSh2Hgcs"
    )

# Live Free of Die Hard movie: movie title, poster image and movie trailer
die_hard_4 = media.Movie(
    "Live Free or Die Hard",
    "https://i.pinimg.com/originals/b1/97/90/b197904bb75a1c3c9f55046083a94fa4.jpg",  # NOQA
    "https://www.youtube.com/watch?v=xqjICXgcsZM"
    )

# A Good Day to Die Hard movie: movie title, poster image and movie trailer
die_hard_5 = media.Movie(
    "A Good Day to Die Hard",
    "http://screencrush.com/files/2012/12/die_hard_5_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=L1-_JtvbqRk"
    )
# list of movies #
movies = [die_hard, die_hard_2, die_hard_3, die_hard_4, die_hard_5]

# calls open_movies_page to generate die_hard_movies.htlm file
die_hard_movies.open_movies_page(movies)
