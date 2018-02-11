import webbrowser

'''This class Movie() is like a blue print with a constructor that creates
instance variables to create an instance of the class Movie(). After an
instance is created, the class constructor gets called. This is the
__init__ method inside the class. This __init__ method initializes all
of the data inside the class. The constuctor uses the key word self.
You can think of the key word self as itself of the instances in question.
So if an instance of Avatar is being created, Avatar is self.'''
class Movie():
    '''This class a way to store my favorite movies and related information'''
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']
    
    '''The variables associated with a specific instance is called instance
    variables. These are unique to an object. They can be access by using the
    self keyword inside the class and the instance name outside the class.'''
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    '''This function inside of the Movie class that has the first argument
    as self is called instance method.'''
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
