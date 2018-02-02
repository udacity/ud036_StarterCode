import webbrowser


# create Movie class with initial variables
# define show_trailer function

class Movie ():
    """docstring for Movie """
    def __init__(self, title, poster, trailer):
        self.title = title
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
