import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://www.crankycritic.com/archive/posters/toystory.jpg","https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A Marine on an alien planet", "https://www.movieposter.com/posters/archive/main/101/MPW-50968", "https://youtu.be/5PSNL1qE6VY")

top_gun = media.Movie("Top Gun", "A Navy pilot and RIO enter the Navy's elite figher school", "http://img.moviepostershop.com/top-gun-movie-poster-1986-1010468870.jpg", "https://youtu.be/iCrUqt9Uf3E")

school_of_rock = media.Movie("School of Rock", "Using rock music to learn", "https://images-na.ssl-images-amazon.com/images/I/51v8TQDTF-L.jpg", "https://youtu.be/3PsUJFEBC74")

midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet authors", "https://images-na.ssl-images-amazon.com/images/I/61uuYEUFw4L._SY450_.jpg", "https://youtu.be/FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games", "A really real reality show", "https://2982-presscdn-29-70-pagely.netdna-ssl.com/wp-content/uploads/2015/11/The-Hunger-Games-Poster1.jpg", "https://youtu.be/PbA63a7H0bo")


movies = [toy_story, avatar, top_gun, school_of_rock, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
