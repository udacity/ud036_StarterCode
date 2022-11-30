#Base class
class Video(object):
	'''Base Class contains all the variables and function that is going to be same for its derived class''' #documentation of class
	VALID_RATINGS=["G", "PG", "PG-13", "R"]
	__name__ = "Video"	#defalut variable to name the class

	def __init__(self, title, duration, genre, poster_image, youtube_trailer):
		self.title = title
		self.duration = duration
		self.genre = genre
		self.poster_image_url = poster_image
		self.trailer_youtube_url = youtube_trailer

#Child class inheriting Video
class Movie(Video):
	'''Movie class contains details of movie and inherits Video class'''
	__name__ = "Movie"

	def __init__(self, title, duration, genre, poster_image, youtube_trailer, storyline, director, producer):
		Video.__init__(self, title, duration, genre, poster_image, youtube_trailer) #Calling Base class constructor
		self.storyline = storyline
		self.director = director
		self.producer = producer

#Child class inheriting Video
class MusicVideo(Video):
	'''MusicVideo class contains information of music video and inherits Video class'''
	__name__ = "MusicVideo"

	def __init__(self, title, duration, genre, poster_image, youtube_trailer, artist, director, lable, peak_billboard_position):
		Video.__init__(self, title, duration, genre, poster_image, youtube_trailer) #Calling Base class constructor
		self.artist = artist
		self.director = director
		self.lable = lable
		self.peak_billboard_position = peak_billboard_position

#Child class inheriting Video
class TVShows(Video):
	'''TVShows class have information of TV Series and inherits Video class'''
	__name__ = "TVShows"
	
	def __init__(self, title, duration, genre, poster_image, youtube_trailer, scenario, no_of_seasons, tv_station, created_by):
		Video.__init__(self, title, duration, genre, poster_image, youtube_trailer) #Calling Base class constructor
		self.scenario = scenario
		self.no_of_seasons = no_of_seasons
		self.tv_station = tv_station
		self.created_by = created_by