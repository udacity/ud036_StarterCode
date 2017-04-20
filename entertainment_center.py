import media
import fresh_tomatoes

pursuit_of_happyness = media.Movie("Pursuit of happyness","Life is a struggle for single father Chris Gardner (Will Smith). Evicted from their apartment, he and his young son (Jaden Christopher Syre Smith) find themselves alone with no place to go. Even though Chris eventually lands a job as an intern at a prestigious brokerage firm, the position pays no money. The pair must live in shelters and endure many hardships, but Chris refuses to give in to despair as he struggles to create a better life for himself and his son.","http://www.impawards.com/2006/posters/pursuit_of_happyness.jpg","https://www.youtube.com/watch?v=SIZKoak6gp8")
forrest_gump = media.Movie("Forrest Gump","--","https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_UY268_CR10,0,182,268_AL_.jpg","https://www.youtube.com/watch?v=EtYNngO7eq4")
hachi = media.Movie("Hachi","A Dog's tale","http://www.sonypictures.com/movies/hachiadogstale/assets/images/onesheet.jpg","https://www.youtube.com/watch?v=JImj5lV7al4")
panda = media.Movie("Kung fu Panda","--","https://resizing.flixster.com/nA0UOjQRyo3nZmtiMD1b5rQGe6g=/206x305/v1.bTsxMTE3Nzg0MztqOzE3MzY0OzEyMDA7ODAwOzEyMDA","https://www.youtube.com/watch?v=tuOA5WZVQRQ")
walter_mitty = media.Movie("The secret life of Walter Mitty","--","https://resizing.flixster.com/FEIILRoZa_GsQOIW_Z9Gwyh1whQ=/206x305/v1.bTsxMTE3NzM1NDtqOzE3MzY0OzEyMDA7ODAwOzEyMDA","https://www.youtube.com/watch?v=5I6T_WztBXg")
hunger_games = media.Movie("Hunger Games","----","https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg","https://www.youtube.com/watch?v=FovFG3N_RSU")

#print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)

movies = [pursuit_of_happyness,forrest_gump,hachi,panda,walter_mitty,hunger_games]
fresh_tomatoes.open_movies_page(movies)
