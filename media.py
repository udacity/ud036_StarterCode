'''
Project_name: movie_website
Author: Yuhan Lin
Description: this is a Movie class. Allow user to create instances of Movie.
Last_update:4/18/2017
'''

import webbrowser


class Movie():
    """ this is a Movie class. Allow user to create instances of Movie.  """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """
         
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ open browser to load the URL """
        webbrowser.open(self.trailer_youtube_url)