import media
import urllib
import fresh_tomatoes

#Movie class objects with movie details

boyka_undisputed=media.Movie("Boyka: Undisputed", "88 Minutes", "Martial Arts Film", "https://images-na.ssl-images-amazon.com/images/M/MV5BNGQ4YjhmNzUtZTI1MC00OTQ3LTk4MTItYWJhNDdmNGZjOWU2XkEyXkFqcGdeQXVyMTA2NjI0MQ@@._V1_UY268_CR0,0,182,268_AL_.jpg","https://www.youtube.com/watch?v=KQtB3-NMfnU", "A fighter tries to save wife of another fighter who he accidently kill in a fight.", "Todor Chapkanov", "Boaz Davidson")

avatar=media.Movie("Avatar", "161 Minutes", "Fantasy/Science Fiction Film", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY", "A Marine on an alien planet", "James Cameron", "James Cameron")

interstellar=media.Movie("Interstellar", "169 Minutes", "Epic Science Fiction Film", "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg", "https://www.youtube.com/watch?v=2LqzF5WauAw", "A EX-Nasa pilot went to search and colonize life in other planet.", "Christopher Nolan", "Emma Thomas")

the_big_sick=media.Movie("The Big Sick", "117 Minutes", "Romantic Comedy Film ", "https://upload.wikimedia.org/wikipedia/en/6/69/The_Big_Sick.jpg", "https://www.youtube.com/watch?v=PJmpSMRQhhs", "Love Story of Pakistani comedian in American", "Michael Showalter", "Judd Apatow")

inception=media.Movie("Inception", "148 Minutes", "Science Fiction Film", "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", "https://www.youtube.com/watch?v=d3A3-zSOBT4", "Creating an idea in other person mind by the help of dream.", "Christopher Nolan", "Emma Thomas")

shutter_island= media.Movie("Shutter Island", "138 Minutes", " Neo-Noir Psychological Thriller", "https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg", "https://www.youtube.com/watch?v=YDGldPitxic", "A us marshal stuck in an Asylum in an island.", "Martin Scorsese", "Mike Medavoy")

#the_accountant=media.Movie("The Accountant", "Story of autism guy as a clever accountant and army skill", "https://upload.wikimedia.org/wikipedia/en/thumb/e/e4/The_Accountant_%282016_film%29.png/220px-The_Accountant_%282016_film%29.png", "https://www.youtube.com/watch?v=DBfsgcswlYQ")

#lucy=media.Movie("Lucy", "A woman's strength and thinking power grow exponentially after the effects of a performance-enhancing drug set in.", "https://upload.wikimedia.org/wikipedia/en/thumb/1/14/Lucy_%282014_film%29_poster.jpg/220px-Lucy_%282014_film%29_poster.jpg", "https://www.youtube.com/watch?v=MVt32qoyhi0")

#the_sixth_sense=media.Movie("The Sixth Sense", "A child psychologist, starts treating a young boy who acts as a medium of communication between Crowe and a slew of unhappy spirits.", "https://upload.wikimedia.org/wikipedia/en/6/66/The_sixth_sense.jpg", "https://www.youtube.com/watch?v=VG9AGf66tXM")

movies=[boyka_undisputed, avatar, interstellar, the_big_sick, inception, shutter_island]#, the_accountant, lucy, the_sixth_sense]

fresh_tomatoes.open_movies_page(movies)