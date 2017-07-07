import media
import fresh_tomatoes

#Below we define instances of class "movie" for each movie that will be in our website
#Class media.movie has the following four variables: Movie title, description of movie, url for poster, url for trailer
trainspotting_2 = media.movie("T2: Trainspotting","First there was an opportunity......then there was a betrayal.","https://upload.wikimedia.org/wikipedia/en/1/1c/T2_%E2%80%93_Trainspotting_poster.jpg","https://youtu.be/EsozpEE543w")
Babadook = media.movie("Babadook","A mother, a son, a children's book, and a monster","https://upload.wikimedia.org/wikipedia/en/d/d7/The-Babadook-Poster.jpg","https://www.youtube.com/watch?v=szaLnKNWC-U")
The_Room = media.movie("The Room","What a story, Mark","https://upload.wikimedia.org/wikipedia/en/e/e1/TheRoomMovie.jpg","https://youtu.be/EE6RQ8rC8hc")
SpaceOdd = media.movie("2001:a space odyssey","An epic drama of adventure and exploration","https://upload.wikimedia.org/wikipedia/en/a/a7/2001_A_Space_Odyssey_%281968%29_theatrical_poster_variant.jpg","https://www.youtube.com/watch?v=lfF0vxKZRhc")

#Insert movie instances into a list for method open_movies_page in fresh_tomatoes.py
movies = [trainspotting_2, Babadook,The_Room,SpaceOdd]

#Pass list "movies" to method open_movies_page to generate trailer website
fresh_tomatoes.open_movies_page(movies)
