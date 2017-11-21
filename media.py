import webbrowser


class Movie():
    """
    Movie class to store the details of movie
    """
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """
        Assign the movie instance variables with the given values
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster = poster_image
        self.trailer = trailer_youtube

    def show_trailor(self):
        """
        Open the trailer of the calling movie instance
        """
        webbrowser.open(self.trailer)
