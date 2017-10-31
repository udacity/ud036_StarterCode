from media import MovieMedia
from datetime import date


class Entertainment(object):
    """A class for handling all movie related operations """
    def __init__(self):
        self
    #A method which returns a list of movies which are of MovieMedia type
    def get_movies_list(self):
        movielist = []
        movie = MovieMedia()
        movie.title = "Dangal"
        movie.director = "Nitesh Tiwari"
        movie.story_line = '''Former wrestler Mahavir Singh Phogat and his two
        wrestler daughters struggle towards glory at the Commonwealth Games in 
        the face of societal oppression.'''
        movie.cast = [
            "Aamir Khan", "Sakshi Tanwar", "Fatima Sana Shaikh", 
            "Sanya Malhotra", "Zaira Wasim", "Aparshakti Khurana"
        ]
        movie.release_date = date.today
        movie.movie_trailers=["https://www.youtube.com/watch?v=x_7YlGv9u1g"]
        movie.poster_images = ["https://images-na.ssl-images-amazon.com/images/M/MV5BNmM4YTJiMjQtNjFmMS00NmQ5LWFmZGItYmI0NDQ4ZjBlNmU4XkEyXkFqcGdeQXVyMzgxNjA1NTE@._V1_QL50_.jpg"]
        movielist.append(movie)
        movie2 = MovieMedia()
        movie2.title = "Bahubali 2: The Conclusion"
        movie2.director = "S.S. Rajamouli"
        movie2.story_line = '''When Shiva, the son of Bahubali, learns about 
        his heritage, he begins to look for answers. His story is juxtaposed 
        with past events that unfolded in the Mahishmati Kingdom.'''
        movie2.cast = [
            "Prabhas Raju", "Rana Daggubati", "Anushka Shetty", 
            "Tamannaah Bhatia", "Sathyaraj", "Ramya Krishnan"
        ]
        movie2.release_date = date
        movie2.movie_trailers = ["https://www.youtube.com/watch?v=qD-6d8Wo3do"]
        movie2.poster_images = ["https://images-na.ssl-images-amazon.com/images/M/MV5BMWRjOTAxMmQtMjViMC00OWU2LTlkZTQtNTYyYjhiZjMzYjg4XkEyXkFqcGdeQXVyODA2ODM3NDQ@._V1_QL50_SY1000_CR0,0,696,1000_AL_.jpg"]
        movielist.append(movie2)
        return movielist

