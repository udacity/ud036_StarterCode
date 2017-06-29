import webbrowser

# The movie blueprint
class Movie():
    # Create 4 properties or parameters for the movie
    def __init__(self, title, storyline, poster_image, trailer_youtube):
        self.title = title
        self.storyine = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Open the youtube trailer in a browser
    def open_browser(self):
        webbrowser.open(self.trailer_youtube_url)
        
