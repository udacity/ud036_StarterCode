# Import my media file which contains Movie class (media.py)
import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
                        "https://www.youtube.com/watch?v=VwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", 
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

endersgame = media.Movie("Ender's Game",
                         "Future defense of Earth depends on brilliant young commander.",
                         "https://upload.wikimedia.org/wikipedia/en/8/8c/Ender%27s_Game_poster.jpg", 
                         "https://www.youtube.com/watch?v=vP0cUBi4hwE")

school_of_rock = media.Movie("School of Rock",
                         "Using rock music to learn.",
                         "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", 
                         "https://www.youtube.com/watch?v=3PsUJFEBC74")

avengers = media.Movie("Avengers",
                         "Alien invasion stopped by team of superheros.",
                         "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg", 
                         "https://www.youtube.com/watch?v=E-84FIZ8-Ow")

jesus = media.Movie("Jesus of Nazareth",
                         "The greatest story ever told.",
                         "https://upload.wikimedia.org/wikipedia/en/c/c0/Jesus_of_nazareth.jpg", 
                         "https://pureflix.com/videos/253280294866/play")

# Create Python array for movie instances!
movies = [jesus, toy_story, avatar, endersgame, school_of_rock, avengers]

# print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
# print(media.Movie.__dict__)
print(media.Movie.__name__)
print(media.Movie.__module__)

fresh_tomatoes.open_movies_page(movies)


# Test Code No Longer Used
# print(toy_story.storyline)
# print(avatar.storyline)
# avatar.show_trailer()
# print(endersgame.storyline)
# endersgame.show_trailer()
