import webbrowser

class movie():
    #initialize class movie which takes in: movie title, synopsis, url for poster image, and url for youtuev trailer
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #this method opens up the trailer for the movie instance in your default web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
