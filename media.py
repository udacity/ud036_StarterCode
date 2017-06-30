# coding = utf-8
"""
Module to display movie object, attributes, and instances
"""

import webbrowser

# The movie blueprint
class Movie():
    """
    Class object stores movie related information
    """
    
    # Create 4 properties or parameters for the movie
    def __init__(self, title, storyline, poster_image, trailer_youtube):
        """
        Initialize instances of class Movie
        
        :param title: title
        :param storyline: storyline
        :param poster_image_url: poster_image_url
        :param trailer_youtube_url: trailer_youtube
        """
        
        self.title = title
        self.storyine = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Open the youtube trailer in a browser
    def open_browser(self):
        """
        Initialize instances for opening youtube trailer

        :return: webbrowser to play trailer
        """
        
        webbrowser.open(self.trailer_youtube_url)
        
