# importing the fresh_tomatoes file
import fresh_tomatoes
# importing the media file
import media
# I created six movies  (title, subtitle and image)
avatar = media.Movie ("Avatar", "A marine on an alient planet",
                      "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
                      "https://www.youtube.com/watch?v=5PSNL1qE6VY")

Tomb_Raider = media.Movie ("Tom Raider", "Lara Croft, the fiercely independent daughter of a missing adventurer, must push herself beyond her limits when she finds herself on the island where her father disappeared",
                           "https://upload.wikimedia.org/wikipedia/en/b/bd/Tomb_Raider_%282018_film%29.png",
                           "https://www.youtube.com/watch?v=dBBu6czCJRI")
Matrix = media.Movie ("Matrix", "Matrix, By day he is an average computer programmer and by night a hacker known as Neo.",
                    "https://www.movieposter.com/posters/archive/main/9/A70-4902",
                    "https://www.youtube.com/watch?v=m8e-FF8MsqU")
Planet_Earth2 = media.Movie ("Planet Earth 2", "10 years ago Planet Earth changed our view of the world. Now we take you closer than ever before. This is life in all its wonder.",
                    "https://blackwells.co.uk/jacket/l/9781849909655.jpg",
                    "https://www.youtube.com/watch?v=c8aFcHFu8QM")
Legend_of_Tarzan = media.Movie ("Legend of Tarzan", "Tarzan, having acclimated to life in London, is called back to his former home in the jungle to investigate the activities at a mining encampment.",
                    "http://de.web.img3.acsta.net/c_300_300/pictures/16/06/10/18/05/357067.jpg",
                    "https://www.youtube.com/watch?v=dLmKio67pVQ")
Fifty_Shades_of_Grey = media.Movie ("Fifty Shades of Grey", "The film is based on the 2011 novel of the same name by British author E. L. James and stars Dakota Johnson as Anastasia Steele, a college graduate who begins a sadomasochistic relationship with young business magnate Christian Grey, played by Jamie Dornan.",
                    "https://upload.wikimedia.org/wikipedia/en/7/73/Fifty_Shades_of_Grey_poster.jpg",
                    "https://www.youtube.com/watch?v=SfZWFDs0LxA")
# I wrapped the movies in a list
movies = [avatar, Tomb_Raider, Matrix, Planet_Earth2, Legend_of_Tarzan, Fifty_Shades_of_Grey]
# Open movies page function, with movies as argument
fresh_tomatoes.open_movies_page (movies)
