# class to create a new movie entry with movie title, poster_image_url, and trailer_youtube_url #
class Movie():
    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        """ This docstring explains the constructor method """
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
