
class Video(object):
	VALID_RATINGS=["G", "PG", "PG-13", "R"]

	def __init__(self, title, duration, genre, poster_image, youtube_trailer):
		self.title = title
		self.duration = duration
		self.genre = poster_image
		self.youtube_trailer = youtube_trailer

class Movie(Video):

	def __init__(self, title, duration, genre, poster_image, youtube_trailer, storyline, director, producer):
		Video.__init__(self, title, duration, genre, poster_image, youtube_trailer)
		self.storyline = storyline
		self.director = director
		self.producer = producer

class MusicVideo(Video):
	
	def __init__(self, title, duration, genre, poster_image, youtube_trailer, artist, director, lable, peak_billboard_position):
		Video.__init__(self, title, duration, genre, poster_image, youtube_trailer)
		self.artist = artist
		self.director = director
		self.lable = lable
		self.peak_billboard_position = peak_billboard_position

class TVShows(Video):
	
	def __init__(self, title, duration, genre, poster_image, youtube_trailer, scenario, no_of_seasons, tv_station, created_by):
		Video.__init__(self, title, duration, genre, poster_image, youtube_trailer)
		self.scenario = scenario
		self.no_of_seasons = no_of_seasons
		self.tv_station = tv_station
		self.created_by = created_by