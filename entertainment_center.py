from media import Movie
from fresh_tomatoes import open_movies_page

movies_meta = [
  {
    'title': 'The Shawshank Redemption',
    'poster_image_url': 'https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg',
    'trailer_youtube_url': 'https://www.youtube.com/watch?v=RQSmfzfg2MY'
  },
  {
      'title': 'The God Father',
      'poster_image_url': 'https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg',
      'trailer_youtube_url': 'https://www.youtube.com/watch?v=sY1S34973zA'
  },
  {
      'title': '12 Angry Men',
      'poster_image_url': 'https://upload.wikimedia.org/wikipedia/en/9/91/12_angry_men.jpg',
      'trailer_youtube_url': 'https://www.youtube.com/watch?v=Dosg0p7LAB4'
  },
  {
      'title': 'Schindler\'s List',
      'poster_image_url': 'https://upload.wikimedia.org/wikipedia/en/3/38/Schindler%27s_List_movie.jpg',
      'trailer_youtube_url': 'https://www.youtube.com/watch?v=M5FpB6qDGAE'
  },
]

def make_movies(movies_meta):
  movies = []
  for movie in movies_meta:
    title, poster_image_url, trailer_youtube_url = movie.values()
    movies.append(Movie(title, poster_image_url, trailer_youtube_url))
  return movies


open_movies_page(make_movies(movies_meta))
