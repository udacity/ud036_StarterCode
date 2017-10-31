from datetime import date


class MovieMedia(object):
    """A class for defining properties of a movie :
    title: A string representing a title of a movie
    release date: A date representing a release/released date of a movie
    genres: An array of strings represting genres of a movie
    story line: A string representing summary of a movie
    director: A string representing a director of a movie
    cast: An array of strings represting crew who was acted in a movie
    poster images: An array of urls representing posters of a movie
    movie trailers: An array of urls representing trailers of a movie
    """

# Initializes all internal variables with default values
    def __init__(self):
        self._title = ""
        self._release_date = date.today
        self._genres = []
        self._story_line = ""
        self._director = ""
        self._cast = []
        self._poster_images = []
        self._movie_trailers = []

# Property for setting and getting title
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        self._title = value

# Property for setting and getting release/released date
    @property
    def release_date(self):
        return self._release_date
    
    @release_date.setter
    def release_date(self, value):
        self._release_date = value

# Property for setting and getting release/released date
    @property
    def genres(self):
        return self._genres
    
    @genres.setter
    def genres(self, value):
        self._genres = value

# Property for setting and getting summary of movie
    @property
    def story_line(self):
        return self._story_line
    
    @story_line.setter
    def story_line(self, value):
        self._story_line = value

# Property for setting and getting director of movie
    @property
    def director(self):
        return self._director
    
    @director.setter
    def director(self, value):
        self._director = value

# Property for setting and getting cast of movie
    @property
    def cast(self):
        return self._cast
    
    @cast.setter
    def cast(self, value):
        self._cast = value

# Property for setting and getting movie poster images
    @property
    def poster_images(self):
        return self._poster_images
    
    @poster_images.setter
    def poster_images(self, value):
        self._poster_images = value

# Property for setting and getting movie trailer urls
    @property
    def movie_trailers(self):
        return self._movie_trailers
    
    @movie_trailers.setter
    def movie_trailers(self, value):
        self._movie_trailers = value
