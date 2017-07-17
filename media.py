import webbrowser

class Movie():
    """This is Najah's Movie class used by instances of this class to initialize
    common variables that all movies share"""
    VALID_RATINGS = ["R", "PG"]
    def __init__(self,title,storyline,poster_image_url,trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
