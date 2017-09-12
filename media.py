import webbrowser

class Movie():
    """ This class provide a way to store movie related information """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    
    def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster = movie_poster
        self.trailer = movie_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
    
