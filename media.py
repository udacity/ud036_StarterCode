#media module that defines Movie class
import webbrowser

# define movie class 
class Movie():
    """This class contains information about movies """
    # the above is a documentation string that gets into pre-defined instance variable
    # called __doc__
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    #VALID_RATINGS is a constant instance variable for Movie class.

    #Constructor that initializes movie instance.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        #initialize all attributes of the class instance with the argument values
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # method that opens a youtube url and plays the trailer.        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url);
