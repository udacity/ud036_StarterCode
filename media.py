import webbrowser

class Movie() :
    """ This a class of the type Movie
        Params :
            title - Title of the movie
            storyline _ Brief synompsis of movie 
            poster image - Image the represents the movie
            movie trailer - Movie trailer URL that can be played

        To create an intance of movie (example)
        avatar = media.Movie("Avatar",
                       "Blue people with bows and arrows",
                       "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                       "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
        
            """
    # list of current movie ratings from MPAA 
    VALID_RATINGS = ["G", "PG", "PG-13", "R", "NC-17"]
    
    # Movie contstructor params defined in docs
    def __init__(self, title, story, poster, trailer) :
        self.title = title
        self.storyline = story
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    # Movie method to play the movie trailer url
    def show_trailer(self) :
        webbrowser.open(self.trailer_youtube_url)
        

    
