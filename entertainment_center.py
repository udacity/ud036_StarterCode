'''
Project_name: movie_website
Author: Yuhan Lin
Description: This is a main fuction.
             Allow user to create instances of Movie.
             And use open_movies_page(movies) to create movie website
Last_update:4/18/2017
'''
import media
import fresh_tomatoes

# create instances of Movie
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/ToyStory4poster.jpg/200px-ToyStory4poster.jpg",
                        "https://youtu.be/Bj4gS1JQzjk")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/H9S-K71JD_E")

warcraft = media.Movie("Warcraft",
                       "Draenor, the homeworld of the orcs, is being torn apart by a mysterious force known as fel magic.",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Warcraft_Teaser_Poster.jpg/220px-Warcraft_Teaser_Poster.jpg",
                       "https://youtu.be/RhFMIRuHAL4")

# create a list to store the movies
movies = [toy_story, avatar, warcraft]

# use open_movies_page(movies) to create movie website
fresh_tomatoes.open_movies_page(movies)
