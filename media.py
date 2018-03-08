import webbrowser


class Movie():
    """
        Class that gives a way to store movie data.
    """
    # constructor of the class Movie
    def __init__(self, movie_title, poster, movie_trailer):
        self.title = movie_title
        self.poster_image_url = poster
        self.trailer_youtube_url = movie_trailer

