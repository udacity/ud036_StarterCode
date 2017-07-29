import fresh_tomatoes
import media

terminator_2 = media.Movie("Terminator 2",
                          "https://upload.wikimedia.org/wikipedia/en/8/85/Terminator2poster.jpg",
                          "https://www.youtube.com/watch?v=VVZQ39i5G1s")

inception = media.Movie("Inception",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=W7OTkEY1tMI")

batman = media.Movie("The Dark Knight",
                     "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                     "https://www.youtube.com/watch?v=_PZpmTj1Q8Q")


movies = [terminator_2, inception, batman]
fresh_tomatoes.open_movies_page(movies)
