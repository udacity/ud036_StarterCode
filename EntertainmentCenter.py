import media
import fresh_tomatoes
# Creating movie instances of Class Movie
the_dark_knight = media.Movie(
    "The Dark Knight",
    "A man protecting his city disguised in bat suite",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3vVwDZYVjhrZsXQjhLkdZQAT9S6Irp6wSZhjO9S0rZZ-wjjPn",  # Noqa
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

up = media.Movie(
    "UP",
    "An old man who is on the quest fo fulfilling his dead wife's" +
    " wish and a kid who is struck around the old man are " +
    "doing adventure things",
    "https://vignette.wikia.nocookie.net/disney/images/a/a6/Up_Poster_Run.jpg/revision/latest?cb=20160202180816",  # Noqa
    "https://www.youtube.com/watch?v=ZE_V0g9q4g0")

the_impossible = media.Movie(
    "The impossible",
    "How a family is getting reunited after Tsunami disaster ",
    "https://upload.wikimedia.org/wikipedia/en/b/b8/The_Impossible.jpg",
    "https://www.youtube.com/watch?v=Bgw394ZKsis")

harry_potter = media.Movie(
    "The Harry Potter And The Sorcerer's Stone",
    "A kid famous in wizard world attending wizard school",
    "https://static.rogerebert.com/uploads/movie/movie_poster/harry-potter-and-the-sorcerers-stone-2001/large_uLGaJ9FgPWf7EUgwjp9RTmHemw8.jpg",  # Noqa
    "https://www.youtube.com/watch?v=PbdM1db3JbY")

the_zootopia = media.Movie(
    "The Zootopia",
    "A bunny cop and wolf trying to catch the criminal gang",
    "https://www.flayrah.com/sites/default/files/u/crossaffliction/zootopialittlegoldenbook.jpg",  # Noqa
    "https://www.youtube.com/watch?v=jWM0ct-OLsM")

the_lord_of_rings = media.Movie(
    "The_Lord_of_the_Rings: The_Fellowship_of_the_Ring",
    "The fate of Middle-earth hangs in the balance as Frodo and " +
    "eight companions who form the Fellowship of the Ring begin " +
    "their journey to Mount Doom in the land of Mordor",
    "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",  # Noqa
    "https://www.youtube.com/watch?v=V75dMMIW2B4")

# Movies array, contains the list of movies as input, which
# is passed to the function "open_movies_page". This function
# translates this list into a web page when we run the
# "EntertainmentCenter.py" file.

movies = [the_dark_knight,
          up,
          the_impossible,
          harry_potter,
          the_zootopia,
          the_lord_of_rings]
# Creating wepage with the movie instances to play trailer
fresh_tomatoes.open_movies_page(movies)
