class Movie(object):
	'''A movie class that holds information about a movie (title, poster, 
	   rating, etc.)
	'''

	def __init__(self,title,posterUrl,trailerId,rating):
		#Required instance variables
		self.title = title
		self.poster_image_url = posterUrl
		self.trailer_youtube_url = trailerId
		#Optional instance variables
		self.rating = rating #Defaults to None


	#Getters

	@property
	def title(self):
	    return self._title
	
	@property
	def poster_image_url(self):
	    return self._poster_image_url
	
	@property
	def trailer_youtube_url(self):
	    return self._trailer_youtube_url

	@property
	def rating(self):
	    return self._rating

	@property
	def test(self):
	    return self._test
	

	#Setters

	@title.setter
	def title(self,title):
		#Check that the title is always a string (unicode is OK)
		if isinstance(title, basestring): 
			self._title = title
		else:
			print "That is not a string. Variable not set."

	@poster_image_url.setter
	def poster_image_url(self,poster_image_url):
		#Check that the poster_image_url is always a string (unicode is OK)
		if isinstance(poster_image_url, basestring): 
			self._poster_image_url = poster_image_url
		else:
			print "That is not a string. Variable not set."		
	
	@trailer_youtube_url.setter
	def trailer_youtube_url(self,trailer_youtube_url):
		#Check that the trailer_youtube_url is always a string (unicode is OK)
		if isinstance(trailer_youtube_url, basestring): 
			self._trailer_youtube_url = trailer_youtube_url
		else:
			print "That is not a string. Variable not set."

	@rating.setter
	def rating(self,rating):
		'''Change the movie's rating (out of 5 stars)'''
		#Check that the rating is always a string (unicode is OK)
		if isinstance(rating, int) and rating >= 0 and rating <= 5:
			self._rating = rating
		else:
			print ("That is not a proper number (positive integer less than or"
				   "equal to 5). Variable not set.")