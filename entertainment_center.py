# Entertainment center app. Creates a webpage for favourite movies trailers.
# import required modules
import fresh_tomatoes
import media

# create different Movie instances

toy_story = media.Movie("ToyStory",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

panda = media.Movie("Kungfu Panda",
                    "A panda who becomes a master",
                    "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg",
                    "https://www.youtube.com/watch?v=PXi3Mv6KMzY")

nemo = media.Movie("Find Nemo",
                  "A father's adventure searching for his missing son",
                  "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
                  "https://www.youtube.com/watch?v=wZdpNglLbt8")

rat = media.Movie("Ratatouille",
                  "A rat who is interested in coocking",
                  "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                  "https://www.youtube.com/watch?v=c3sBBRxDAqk")

rings = media.Movie("Lord of the Rings",
                    "The fellowship of the ring",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/8/87/Ringstrilogyposter.jpg/330px-Ringstrilogyposter.jpg",
                    "https://www.youtube.com/watch?v=Pki6jbSbXIY")


tomorrow = media.Movie("Tomorrow Land",
                        "A futuristic paranormal activity",
                       "https://upload.wikimedia.org/wikipedia/en/8/80/Tomorrowland_poster.jpg",
                       "https://www.youtube.com/watch?v=0sH0__SpV88")

# create a list of all movie instances
movies = [toy_story, avatar, panda, nemo, rat, rings, tomorrow]

#Create a webpage and open it in browser
fresh_tomatoes.open_movies_page(movies)

