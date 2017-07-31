import media
import fresh_tomatoes
""" This python script creates 6 movie instances into an array of movies
    and supplies the list to fresh_tomatoes, which presents the movies in an
    html page, that can be interacted with.

    cmd line: Python entertainment.py"""


# create several instances of class movie 
beetlejuice = media.Movie("Beetlejuice",
                       "Beetlejuice is the ghostus with the mostus",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BZDdmNjBlYTctNWU0MC00ODQxLWEzNDQtZGY1NmRhYjNmNDczXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_SX670_AL_.jpg",
                       "https://www.youtube.com/watch?v=2hovKm9oFiM")

potter = media.Movie("Harry Potter - Sorcerer's Stone",
                       "Magic boy finally gets cake",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BNjQ3NWNlNmQtMTE5ZS00MDdmLTlkZjUtZTBlM2UxMGFiMTU3XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_.jpg",
                       "https://www.youtube.com/watch?v=K1KPcXRMMo4")

school = media.Movie("School of Rock",
                    "Rock music is fun to learn from",
                    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                    "https://www.youtube.com/watch?v=3PsUJFEBC74")

spawn = media.Movie("Spawn",
                    "A funny clown helps burn victims, but is misunderstood",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BN2ZkMWFlODEtNzIyOC00NmU2LTg5MDQtYWQxY2UyYmQxZGJlL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,678,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=5KMYx8lG59A")

labyrinth = media.Movie("Labyrinth",
                    "A girl trying to save her brother from the goblin king",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM2MDE4OTQwOV5BMl5BanBnXkFtZTgwNjgxMTg2NzE@._V1_SY1000_CR0,0,648,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=_8ZmiqLiZbk")

btlc = media.Movie("Big trouble in little China",
                    "Rescue girl from evil chinese mob boss",
                    "http://www.theofficialjohncarpenter.com/wp-content/uploads/2016/01/john-carpenter-big-trouble-in-little-china-poster.jpg",
                    "https://www.youtube.com/watch?v=592EiTD2Hgo")

# create the list of movies for fresh_tomatoes
movies = [beetlejuice, school, spawn, labyrinth, btlc, potter]

# call launch tomatoes with list of movies created above.
fresh_tomatoes.open_movies_page(movies)
