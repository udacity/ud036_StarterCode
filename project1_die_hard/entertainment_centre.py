### import classes from other files ####
import die_hard_movies
import media
### create list of movies ###
die_hard = media.Movie("Die Hard",
                       "http://horrornews.net/wp-content/uploads/2016/09/Die-Hard-I-DVD.jpg",
                       "https://www.youtube.com/watch?v=-qxBXm7ZUTM")

die_hard_2 = media.Movie("Die Hard 2",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BNzM1MzMwNzY2OF5BMl5BanBnXkFtZTgwNzE1MzkyMTE@._V1_.jpg",
                         "https://www.youtube.com/watch?v=OyxfXQ4MGLQ")

die_hard_3 = media.Movie("Die Hard with a Vengeance",
                         "https://i.jeded.com/i/die-hard-3-die-hard-with-a-vengeance.15819.jpg",
                         "https://www.youtube.com/watch?v=gQ0uSh2Hgcs")

die_hard_4 = media.Movie("Live Free or Die Hard",
                         "https://i.pinimg.com/originals/b1/97/90/b197904bb75a1c3c9f55046083a94fa4.jpg",
                         "https://www.youtube.com/watch?v=xqjICXgcsZM")

die_hard_5 = media.Movie("A Good Day to Die Hard",
                         "http://screencrush.com/files/2012/12/die_hard_5_poster.jpg",
                         "https://www.youtube.com/watch?v=L1-_JtvbqRk")

movies = [die_hard, die_hard_2, die_hard_3, die_hard_4, die_hard_5]
die_hard_movies.open_movies_page(movies)
