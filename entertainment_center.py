import media
import urllib
import fresh_tomatoes

#Movie class objects with movie details

boyka_undisputed = media.Movie("Boyka: Undisputed", "88 Minutes", "Martial Arts Film", "https://images-na.ssl-images-amazon.com/images/M/MV5BNGQ4YjhmNzUtZTI1MC00OTQ3LTk4MTItYWJhNDdmNGZjOWU2XkEyXkFqcGdeQXVyMTA2NjI0MQ@@._V1_UY268_CR0,0,182,268_AL_.jpg","https://www.youtube.com/watch?v=KQtB3-NMfnU", "A fighter tries to save wife of another fighter who he accidently kill in a fight.", "Todor Chapkanov", "Boaz Davidson")

avatar = media.Movie("Avatar", "161 Minutes", "Fantasy/Science Fiction Film", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY", "A Marine on an alien planet", "James Cameron", "James Cameron")

interstellar = media.Movie("Interstellar", "169 Minutes", "Epic Science Fiction Film", "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg", "https://www.youtube.com/watch?v=2LqzF5WauAw", "A EX-Nasa pilot went to search and colonize life in other planet.", "Christopher Nolan", "Emma Thomas")

the_big_sick = media.Movie("The Big Sick", "117 Minutes", "Romantic Comedy Film ", "https://upload.wikimedia.org/wikipedia/en/6/69/The_Big_Sick.jpg", "https://www.youtube.com/watch?v=PJmpSMRQhhs", "Love Story of Pakistani comedian in American", "Michael Showalter", "Judd Apatow")

inception = media.Movie("Inception", "148 Minutes", "Science Fiction Film", "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", "https://www.youtube.com/watch?v=d3A3-zSOBT4", "Creating an idea in other person mind by the help of dream.", "Christopher Nolan", "Emma Thomas")

shutter_island = media.Movie("Shutter Island", "138 Minutes", " Neo-Noir Psychological Thriller", "https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg", "https://www.youtube.com/watch?v=YDGldPitxic", "A us marshal stuck in an Asylum in an island.", "Martin Scorsese", "Mike Medavoy")

movies = [boyka_undisputed, avatar, interstellar, the_big_sick, inception, shutter_island] #List of movies to pass to fresh_tomatoes

#TVShows class objects with TV Show details

game_of_thrones = media.TVShows("Game of Thrones", "50-80 Minutes", "Fantasy Drama", "https://upload.wikimedia.org/wikipedia/en/d/d8/Game_of_Thrones_title_card.jpg", "https://www.youtube.com/watch?v=Egy5A070cbA&index=24&list=PLh8jmroR-sdjN2mWAylt5gBJ5mEQapAfN", "Several royal families desire the Iron Throne to gain control of Westeros. Whilst kingdoms fight each other for power, a sinister force lurks beyond the Wall in the north.", "7", "HBO", "David Benioff, D. B. Weiss")

westworld = media.TVShows("Westworld", "57-91 Minutes", "Science Fiction Western Thriller", "https://upload.wikimedia.org/wikipedia/en/e/eb/Westworld_%28TV_series%29_title_card.jpg", "https://www.youtube.com/watch?v=IuS5huqOND4", "In a futuristic Western-themed amusement park, Westworld, the visitors interact with automatons. However, all hell breaks loose when the automatons begin malfunctioning.", "1", "HBO", "Jonathan Nolan, Lisa Joy")

silicon_valley = media.TVShows("Silicon Valley", "28-39 Minutes", "Comedy Television Series", "https://upload.wikimedia.org/wikipedia/en/3/33/Silicon_valley_title.png", "https://www.youtube.com/watch?v=69V__a49xtw", "Set amidst the high-tech world of the Silicon Valley in USA, the series revolves around the struggles of six programmers who are trying to make a mark in the big, bad world of programming.", "4", "HBO", "Mike Judge, John Altschuler, Dave Krinsky")

tv = [game_of_thrones, westworld, silicon_valley] #List of TV Shows to pass to fresh_tomatoes

#MusicVideo class objects with Music Video details

blank_space = media.MusicVideo("Blank Space", "4:33 Minutes", "Electropop", "https://upload.wikimedia.org/wikipedia/en/7/7c/Taylor_Swift_-_Blank_Space_%28Official_Single_Cover%29.png", "https://www.youtube.com/watch?v=e-ORhEE9VVg", "Taylor Swift", "Joseph Kahn", "Big Machine, Republic", "1")

we_dont_talk_anymore = media.MusicVideo("We Don't Talk Anymore", "3:51 Minutes", "Pop", "https://upload.wikimedia.org/wikipedia/en/4/40/Charlie_Puth_Feat._Selena_Gomez_-_We_Don%27t_Talk_Anymore_%28Official_Single_Cover%29.png", "https://www.youtube.com/watch?v=3AtDnEC4zak", "Charlie Puth Feat Selena Gomez", "Phil Pinto", "Atlantic", "9")

back_to_you = media.MusicVideo("Back to You", "3:18 Minutes", "Pop", "https://upload.wikimedia.org/wikipedia/en/6/6e/Louis_Tomlinson_-_Back_to_You_%28Single_Cover%29.jpeg", "https://www.youtube.com/watch?v=-HjpL-Ns6_A", "Louis Tomlinson Feat Bebe Rexha", "Craig Moore", "78 Productions, Epic", "40")

music = [blank_space, we_dont_talk_anymore, back_to_you]
#fresh_tomatoes.open_movies_page(movies)