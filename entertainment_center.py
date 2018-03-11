# importing the fresh_tomatoes file
import fresh_tomatoes
# importing the media file
import media
avatar = media.Movie ("Avatar", "A marine on an alient planet",
                      "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
                      "https://www.youtube.com/watch?v=5PSNL1qE6VY")

Tomb_Raider = media.Movie ("Tom Raider", "Lara Croft, the fiercely independent daughter of a missing adventurer, must push herself beyond her limits when she finds herself on the island where her father disappeared",
                           "https://upload.wikimedia.org/wikipedia/en/b/bd/Tomb_Raider_%282018_film%29.png",
                           "https://www.youtube.com/watch?v=dBBu6czCJRI")
Matrix = media.Movie ("Matrix", "Matrix, By day he is an average computer programmer and by night a hacker known as Neo.",
                    "https://www.movieposter.com/posters/archive/main/9/A70-4902",
                    "https://www.youtube.com/watch?v=m8e-FF8MsqU")
movies = [avatar, Tomb_Raider, Matrix]
fresh_tomatoes.open_movies_page (movies)
