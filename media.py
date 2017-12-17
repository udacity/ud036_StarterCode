import webbrowser

class Movie(object):
    """This class has the information about the movies 
       self.title = Movie title
       self.story_line = story line of the movie
       self.poster_image_url = poster image of the movie
       self.trailer_youtube_url = movie youtube trailer link"""
    def __init__(self, movie_title, story_line, movie_img, youtube_url):
        self.title = movie_title
        self.story_line = story_line
        self.poster_image_url = movie_img
        self.trailer_youtube_url = youtube_url

