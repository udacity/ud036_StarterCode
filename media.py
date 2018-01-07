import webbrowser

class Movie():
    """ This class provides a way to store movie related information. """  
    # Only if placed directly below class statement does get picked up by "__doc__"

    # If you change all occurrences of the word "self" to
    # another word, say "udacity" in the media.py file, the
    # code will still work. Go ahead, try it out.
    #
    # Even though self is not a keyword, it is a convention
    # that is used by most Python programmers. Using the word
    # self will make your code more readable to other programmers.
    # So we encourage that you do so.

    # Class variable because outside all functions
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
